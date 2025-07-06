## Project Structure

- **scripts/**
  - [`text_processor.py`](scripts/text_processor.py): Utilities for cleaning and splitting complaint text ([`ProcessText`](scripts/text_processor.py)).
  - [`chroma.py`](scripts/chroma.py): Wrapper for interacting with a Chroma vector database ([`ChromaDb`](scripts/chroma.py)).
  - [`plots.py`](scripts/plots.py): Functions for visualizing data distributions and correlations.

- **tests/**
  - Contains unit tests for the processing modules, e.g., [`test_text_processor.py`](tests/test_text_processor.py).

- **data/**
  - Place your raw and processed data files here.



