import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def plot_boxplot(df:pd.DataFrame, cols:list[str]):
    """
    Plots boxplots for the specified columns in a pandas DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        cols (list[str]): List of column names to plot. If empty, all columns are considered.

    Notes:
        - Only numeric columns are plotted.
        - Each boxplot is displayed in a separate figure.
    """
    if len(cols) == 0:
        cols = df.columns
    for col in cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            plt.boxplot(df[col])
            plt.xlabel(col, fontsize=8)
            plt.figure(figsize=(10,7))
            plt.show()

def plot_histogram(df:pd.DataFrame,cols:list[str]):
    """
    Plots histograms for numeric columns and count plots for categorical columns in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the data to plot.
        cols (list[str]): List of column names to plot. If empty, all columns in the DataFrame are considered.

    Behavior:
        - For each column in `cols`:
            - If the column is numeric, plots a histogram with a KDE curve.
            - If the column is categorical, plots a count plot showing the frequency of each category.
        - Each plot is displayed immediately after creation.
        - Handles missing values in numeric columns by default (can be modified with dropna()).
        - Customizes plot titles, axis labels, and tick parameters for readability.
    """
    i = 0
    if len(cols) == 0:
        cols = df.columns
    for col in cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(df[col], kde=True) # dropna() to handle missing values
            plt.title(f'Distribution of {col}', fontsize=10)
            plt.xlabel(col, fontsize=8)
            plt.ylabel('Frequency', fontsize=8)
            plt.tick_params(axis='both', which='major', labelsize=7)
        else:
            # Use value_counts() to get counts for each category
            sns.countplot(data=df, x=col, order=df[col].value_counts().index, palette='viridis', hue=col)
            plt.title(f'Counts of {col}', fontsize=10)
            plt.xlabel(col, fontsize=8)
            plt.ylabel('Count', fontsize=8)
            plt.xticks(rotation=45, ha='right', fontsize=7)
            plt.tick_params(axis='y', which='major', labelsize=7)
        plt.show()
        i=+1
def correlation_matrix(df:pd.DataFrame, cols:list, name:str):
    """
    Generates and displays a correlation matrix heatmap for the specified columns of a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        cols (list): List of column names to include in the correlation matrix.
        name (str): A name or label to use in the plot title.

    Displays:
        A heatmap plot of the correlation matrix for the specified columns.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title(f'Correlation Matrix for {name}')
    plt.show()
   


