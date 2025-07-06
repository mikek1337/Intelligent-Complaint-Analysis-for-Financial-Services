from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
class ProcessText:
    """
    ProcessText is a utility class for preprocessing and splitting textual data, particularly for complaint analysis.
    Attributes:
        text_splitter (RecursiveCharacterTextSplitter): An instance used to split text into chunks based on specified parameters.
    Args:
        chunk_size (int, optional): The maximum size of each text chunk. Defaults to 100.
        chunk_overlap (int, optional): The number of overlapping characters between chunks. Defaults to 10.
        separators (list[str], optional): List of separator strings to use for splitting text. Defaults to an empty list.
    Methods:
        split(content: str) -> list[str]:
            Splits the given content into chunks using the configured text splitter.
        prepare_text(text: str) -> str:
            Preprocesses the input text by lowercasing, removing boilerplate complaint phrases, removing special characters and numbers, and normalizing whitespace.
        run_all(content: str) -> list[str]:
            Applies text preprocessing and then splits the filtered text into chunks.
    """
    def __init__(self, chunk_size:int=100, chunk_overlap:int=10, separators:list[str]=[]):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap,length_function=len,separators=separators)

    def split(self,content:str):
        """
        Splits the given text content into smaller segments using the configured text splitter.

        Args:
            content (str): The text content to be split.

        Returns:
            list: A list of text segments resulting from the split operation.
        """
        return self.text_splitter.split_text(content)
    
    
    def prepare_text(self, text:str):
        """
        Preprocesses the input text by applying several normalization steps:
        1. Converts text to lowercase.
        2. Removes common boilerplate phrases typically found in CFPB complaints.
        3. Removes special characters and numbers, retaining only letters and spaces.
        4. Collapses multiple whitespaces into a single space and trims leading/trailing spaces.

        Args:
            text (str): The input text to preprocess.

        Returns:
            str: The cleaned and normalized text.
        """
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
        """
        Processes the input text by preparing and splitting it.

        Args:
            content (str): The raw text content to be processed.

        Returns:
            list: A list of text segments resulting from splitting the filtered text.
        """
        filtered_text = self.prepare_text(content)
        return self.split(filtered_text)


