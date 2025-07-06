# Exploratory Data Analysis (EDA) Notebook

This notebook (`eda_analysis.ipynb`) provides a comprehensive exploratory data analysis workflow for consumer complaint data in the financial services domain. The analysis is designed to help you understand the structure, distribution, and temporal trends of complaints, as well as to prepare the data for downstream text analysis and modeling.

## Main Steps Covered

1. **Data Loading and Setup**
   - Loads complaint data from a CSV file.
   - Imports necessary libraries (`pandas`, `seaborn`, `matplotlib`, and custom scripts).

2. **Product Distribution Analysis**
   - Examines how complaints are distributed across different financial products.
   - Visualizes the number of complaints per product using bar plots.

3. **Handling and Analyzing Complaint Narratives**
   - Fills missing values in the `Consumer complaint narrative` column.
   - Calculates and analyzes the word count of each narrative.
   - Visualizes the distribution of narrative lengths and identifies very short or long narratives.

4. **Quantifying Narratives**
   - Counts the number of complaints with and without narrative text.
   - Reports the total number of complaints.

5. **Filtering for Target Products and Non-Empty Narratives**
   - Filters the dataset to include only specified financial products.
   - Removes records with empty complaint narratives.
   - Reports the number of records before and after filtering.

6. **Text Cleaning and Standardization**
   - Cleans complaint narratives by:
     - Lowercasing text.
     - Removing boilerplate phrases.
     - Removing special characters and numbers.
     - Normalizing whitespace.
   - Stores cleaned text in a new column and displays examples.

7. **Temporal Analysis**
   - Parses and cleans the `Date received` column.
   - Extracts temporal features (year, month, day of week).
   - Analyzes and visualizes complaint volume over time (monthly, by product, by seasonality).
   - Identifies trends and patterns in complaint submissions.

8. **Saving the Filtered Dataset**
   - Exports the cleaned and filtered dataset for further analysis.

## Usage

- Run the notebook step by step to reproduce the analysis.
- Modify filtering criteria or cleaning functions as needed for your specific dataset.
- Use the resulting visualizations and cleaned data for further modeling or reporting.

## Output

- Visualizations of complaint distributions and trends.
- Cleaned and filtered dataset saved as `filtered_complaints.csv`.

---

This notebook is a practical starting point for understanding and preparing consumer complaint data for advanced analytics and machine learning