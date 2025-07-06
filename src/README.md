# Ingest Module

This module (`ingest.py`) provides a pipeline for processing, chunking, and storing consumer complaint data into a Chroma vector database for downstream analysis and retrieval.

## Main Features

- **Data Loading:**  
  Loads preprocessed and cleaned complaint data from `data/filtered_complaints.csv` into a pandas DataFrame.

- **Text Chunking and Processing:**  
  Uses the `ProcessText` utility to split and clean complaint narratives into manageable text chunks suitable for embedding and storage.

- **Chroma Database Integration:**  
  Connects to a Chroma vector database (via the `ChromaDb` wrapper) to store text chunks and their associated metadata.

- **Metadata Handling:**  
  Associates each text chunk with relevant metadata fields (such as company, issue, product, submission method, dates, and complaint ID) for efficient retrieval and analysis.

- **Batch Processing:**  
  Processes all complaint records, chunks their narratives, and saves them (along with metadata) into the Chroma collection.

- **Unique Identification:**  
  Each text chunk is assigned a unique UUID to ensure traceability and prevent duplication.

## Main Classes and Methods

- **Ingest**
  - `__init__`: Initializes the Chroma database connection and loads the complaint data.
  - `process_embedding`: Processes the complaint narratives, chunks the text, and saves the results to the Chroma collection.
  - `save`: Saves the generated text chunks and associated metadata for each complaint into the Chroma collection.
  - `get_embeddings`: Retrieves and prints the current Chroma collection for inspection.

## Usage

To process and ingest complaint data, run the script directly:

```sh
python [ingest.py](http://_vscodecontentref_/0)