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
    def __init__(self):
        self.chroma = ChromaDb('localhost', 8000);
        self.data = pd.read_csv(f'{DATA_FOLDER}/filtered_complaints.csv')
        print(f'Data loaded from {DATA_FOLDER}/filtered_complaints.csv')

    
    def process_embedding(self):
        print('Processing embeddings started...')
        
        processtext = ProcessText(CHUNK_SIZE, CHUNK_OVERLAY,["\n\n", "\n", ".", " ", ""])
        self.data[SAVE_CHUNK] = self.data[TARGET_COL].apply(processtext.run_all)
        print('Processing embeddings completed')
        collection = self.chroma.create_collection(COLLECTION_NAME)
        self.data[META_COLS+[SAVE_CHUNK]].apply(lambda row:self.save(row), axis=1)
        print('Saving embedings completed')

    def save(self,content):
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