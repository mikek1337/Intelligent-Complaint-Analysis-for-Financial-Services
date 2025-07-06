import sys
sys.path.append('../scripts')
from scripts.text_processor import ProcessText
from scripts.chroma import ChromaDb
from chromadb import Documents, Collection
import pandas as pd
import uuid

CHUNK_SIZE=100
CHUNK_OVERLAY=100
DATA_FOLDER = 'data'
COLLECTION_NAME = 'complaints'
META_COLS = ['Company','Issue','Product','Submitted via', 'Date sent to company', 'Complaint ID', 'Date received']
TARGET_COL = 'cleaned_narrative'
SAVE_CHUNK = 'narrative_chunks'
class Ingest:
    """
    Ingest class for processing and storing complaint data embeddings.
    Attributes:
        chroma (ChromaDb): Instance for interacting with the Chroma database.
        data (pd.DataFrame): DataFrame containing complaint data loaded from CSV.
    Methods:
        __init__():
            Initializes the Ingest class, loads complaint data from CSV, and sets up the ChromaDb connection.
        process_embedding():
            Processes the complaint text into embeddings, chunks the text, and saves the embeddings and metadata to the Chroma collection.
        save(content):
            Saves the generated chunks and associated metadata for a single complaint entry into the Chroma collection.
        get_embeddings():
            Retrieves and prints the current Chroma collection for inspection.
    """
    def __init__(self):
        self.chroma = ChromaDb('localhost', 8000);
        self.data = pd.read_csv(f'{DATA_FOLDER}/filtered_complaints.csv')
        print(f'Data loaded from {DATA_FOLDER}/filtered_complaints.csv')

    
    def process_embedding(self):
        """
        Processes text data to generate embeddings and saves them to a Chroma collection.
        This method performs the following steps:
        1. Initializes a ProcessText object to chunk and preprocess the target text column.
        2. Applies the text processing to the target column and stores the resulting chunks in a new column.
        3. Creates a new Chroma collection for storing embeddings.
        4. Iterates over each row of the DataFrame, saving the processed text and associated metadata to the collection.
        Prints progress messages at each major step.
        Assumes the following instance variables and constants are defined:
            - self.data: pandas DataFrame containing the data.
            - CHUNK_SIZE, CHUNK_OVERLAY: parameters for text chunking.
            - TARGET_COL: name of the column containing the text to process.
            - SAVE_CHUNK: name of the column to store processed text chunks.
            - META_COLS: list of metadata column names.
            - COLLECTION_NAME: name of the Chroma collection.
            - self.chroma: object with a create_collection method.
            - self.save: method to save a row to the collection.
        """
        print('Processing embeddings started...')
        
        processtext = ProcessText(CHUNK_SIZE, CHUNK_OVERLAY,["\n\n", "\n", ".", " ", ""])
        self.data[SAVE_CHUNK] = self.data[TARGET_COL].apply(processtext.run_all)
        print('Processing embeddings completed')
        collection = self.chroma.create_collection(COLLECTION_NAME)
        self.data[META_COLS+[SAVE_CHUNK]].apply(lambda row:self.save(row), axis=1)
        print('Saving embedings completed')

    def save(self,content):
        """
        Saves the provided content into the Chroma collection by splitting it into chunks and associating metadata.

        Args:
            content (dict): A dictionary containing the complaint data. It must include the keys specified in SAVE_CHUNK and META_COLS.

        Side Effects:
            - Prints the 'Complaint ID' from the content.
            - Adds each chunk of the content to the Chroma collection with a unique UUID and associated metadata.

        Raises:
            KeyError: If required keys are missing from the content dictionary.
        """
        chunks = content[SAVE_CHUNK]
        print(content['Complaint ID'])
        metaData = {col:content[col] for col in META_COLS}
        ids = [str(uuid.uuid4()) for _ in chunks]
        meta = [metaData]*len(chunks)
        collection = self.chroma.get_collection(COLLECTION_NAME)
        collection.add(
            ids=ids,
            documents=chunks,
            metadatas=meta
        )

    def get_embeddings(self):
        collection = self.chroma.get_collection(COLLECTION_NAME)
        print(collection)


if __name__ == "__main__":
    ingest = Ingest()
    ingest.process_embedding()
    # ingest.get_embeddings()