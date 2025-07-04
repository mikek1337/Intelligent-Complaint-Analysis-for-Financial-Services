from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
class ProcessText:
    def __init__(self, chunk_size:int, chunk_overlap:int, separators:list[str]):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap,length_function=len,separators=separators)

    def split(self,content:str):
        return self.text_splitter.split_text(content)
    
    
    def prepare_text(self, text:str):
        # 1. Lowercasing text
        text = text.lower()

        # 2. Removing boilerplate text (common CFPB phrases)
        # Examples: "i am writing to file a complaint", "this is a complaint regarding"
        boilerplate_patterns = [
            r"i am writing to file a complaint (about|regarding|against)",
            r"this is a complaint regarding",
            r"to whom it may concern",
            r"i would like to file a complaint",
            r"my complaint is regarding",
            r"i am filing this complaint to address",
            r"my concern is regarding",
            r"i am contacting you regarding"
            # Add more patterns as you identify common boilerplate in your data
        ]
        for pattern in boilerplate_patterns:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)

        # 3. Removing special characters and numbers (keeping only letters and spaces)
        # This keeps alphanumeric characters and spaces
        text = re.sub(r'[^a-zA-Z\s]', '', text)

        # Remove extra whitespaces
        text = re.sub(r'\s+', ' ', text).strip()

        return text
    
    def run_all(self, content:str):
        filtered_text = self.prepare_text(content)
        return self.split(filtered_text)


