from scripts.text_processor import ProcessText
import pandas as pd

CHUNK_SIZE=100
CHUNK_OVERLAY=100
DATA_FOLDER = 'data'
class Ingest:
    def __init__(self, is_query:bool=False):
        self.is_query = is_query
        self.data = None
        if is_query == False:
            self.data = pd.read_csv(f'{DATA_FOLDER}/filtered_complaints.csv')
            
