
# Project Overview

This project, "Intelligent Complaint Analysis for Financial Services," leverages real-world complaint data from the Consumer Financial Protection Bureau (CFPB) to analyze and gain insights into customer issues across various financial products such as credit cards, personal loans, savings accounts, BNPL, and money transfers.

## Setup Instructions

1. **Clone the Repository**
    ```
    git clone https://github.com/yourusername/Intelligent-Complaint-Analysis-for-Financial-Services.git
    cd Intelligent-Complaint-Analysis-for-Financial-Services
    ```

2. **Create and Activate a Virtual Environment**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Download the Dataset**
    - Download the CFPB complaint dataset from the official [CFPB website](https://www.consumerfinance.gov/data-research/consumer-complaints/).
    - Place the dataset file in the `data/` directory.

5. **Run the Analysis**
    - Execute the main analysis script:
    ```
     jupyter notebook notebooks/eda_analysis.ipynb
    ```

## Project Structure

- `data/` - Contains the raw and processed datasets.
- `notebooks/` - Jupyter notebooks for exploratory data analysis and prototyping.
- `src/` - Source code for data processing, modeling, and evaluation.
- `main.py` - Entry point for running the analysis pipeline.
- `requirements.txt` - List of Python dependencies.

## Requirements

- Python 3.8+
- See `requirements.txt` for additional dependencies.

## Usage

After setup, you can run the analysis pipeline or explore the data and models using the provided notebooks.

