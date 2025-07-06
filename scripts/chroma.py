import chromadb
from chromadb.errors import NotFoundError, ChromaError

class ChromaDb:
    """
    ChromaDb provides a wrapper for interacting with a Chroma database instance over HTTP.
    Attributes:
        client: An instance of the Chroma HTTP client.
    Methods:
        __init__(host: str, port: int):
            Initializes the ChromaDb instance and connects to the Chroma server.
        connect(host: str, port: int):
            Connects to the Chroma server using the provided host and port.
            Returns the Chroma HTTP client instance.
        check_status():
            Checks if the Chroma server is reachable and responsive.
            Returns True if the server is alive, otherwise False.
        create_collection(collection_name: str = 'complaints'):
            Creates a new collection with the specified name.
            Returns the created collection object, or None if creation fails or the collection already exists.
        get_collection(collection_name: str):
            Retrieves an existing collection by name.
            Returns the collection object, or None if the collection does not exist.
        delete_collection(collection_name: str):
            Deletes the specified collection.
            Returns the result of the deletion, or None if the collection does not exist.
    """
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
    
    
            
        



