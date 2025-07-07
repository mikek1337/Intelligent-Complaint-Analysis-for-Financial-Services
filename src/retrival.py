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
    def __init__(self):
        self.chroma = ChromaDb(HOST, PORT)
        self.collection = self.chroma.get_collection(COLLECTION)
        if self.collection == None:
            raise NotFoundError('Collection not found please run ingestion or check chromadb configuration')
    def retrive_documents(self, complaint:str, k:int=5):
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