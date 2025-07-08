from scripts.chroma import ChromaDb
from scripts.text_processor import ProcessText
from chromadb.errors import NotFoundError
from dotenv import load_dotenv

import os
load_dotenv()
HOST = os.getenv('CHROMADB_HOST')
PORT = os.getenv('CHROMADB_PORT')
COLLECTION = 'complaints'
EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
class Retrival:
    """
    The Retrival class is responsible for connecting to a ChromaDB instance
    and retrieving semantically similar documents based on a given complaint.
    It utilizes a pre-defined collection ('complaints') and a text processing
    utility to prepare queries.
    """
    def __init__(self):
        self.chroma = ChromaDb(HOST, PORT)
        self.collection = self.chroma.get_collection(COLLECTION)
        if self.collection == None:
            raise NotFoundError('Collection not found please run ingestion or check chromadb configuration')
    def retrive_documents(self, complaint:str, k:int=5):
        """
        Retrieves the top 'k' most semantically similar documents from the
        'complaints' collection based on the provided 'complaint' text.

        The input complaint text is first preprocessed before being used
        to query the vector database. Results include the document content,
        their similarity distances, and associated metadata.

        Args:
            complaint (str): The input text representing the complaint to search for.
            k (int, optional): The number of top similar documents to retrieve.
                               Defaults to 5.

        Returns:
            dict: A dictionary containing the query results from ChromaDB.
                  This typically includes:
                  - 'documents': A list of lists, where the inner list contains the text of the retrieved documents.
                  - 'distances': A list of lists, where the inner list contains the similarity distances.
                  - 'metadatas': A list of lists, where the inner list contains the metadata dictionaries.
        """
        process = ProcessText()
        processed_complaint = process.prepare_text(complaint)
        results = self.collection.query(query_texts=[processed_complaint], n_results=k, include=['documents','distances','metadatas'])
        for i, doc_text in enumerate(results['documents'][0]):
                distance = results['distances'][0][i]
                metadata = results['metadatas'][0][i]
                print(f"  {i+1}. Document: '{doc_text}'")
                print(f"     Distance: {distance:.4f}, Metadata: {metadata}")
        return results
    

if __name__ == "__main__":
    retrive = Retrival()
    retrive.retrive_documents('I received a notice from XXXX  that an account was just opened under my name.')