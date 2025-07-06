import chromadb
from chromadb.errors import NotFoundError, ChromaError

class ChromaDb:
    def __init__(self, host:str, port:int):
        self.client = self.connect(host, port)

    def connect(self, host:str, port:int):
        chroma_client = chromadb.HttpClient(host=host, port=port)
        print(f'{chroma_client.get_version()}')
        return chroma_client
    def check_status(self):
        if self.client.heartbeat():
            return True
        return False

    def create_collection(self, collection_name:str='complaints'):
        if self.check_status():
            try:
                return self.client.create_collection(collection_name)
            except ChromaError:
                print('Collection already exists')
        return None
    
    def get_collection(self, collection_name:str):
        if self.check_status():
            try:
                return self.client.get_collection(collection_name)
            except NotFoundError:
                print('Collection does not exist')
        return None
    
    def delete_collection(self, collection_name:str):
        try:
            return self.client.delete_collection(collection_name)
        except NotFoundError:
            print('Collection does not exist')
        return None
    
    
            
        



