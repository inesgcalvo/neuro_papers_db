import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Functions for DataFrames
    
def view_nan(df: pd.DataFrame) -> None:
    """
    Visualize the NaN values per column in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    None
    """
    plt.figure(figsize = (10, 6), facecolor = 'none') 
    sns.heatmap(df.isna(),           
                yticklabels = False,  
                cmap = 'magma',     
                cbar = False)
    plt.show();

    
    
def low_variance(df):
    """
    Find columns in the DataFrame with low variance.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    list: A list of column names with low variance.
    """
    low_variance = []
    for col in df.select_dtypes(include = np.number): 
        minimo = df[col].min()
        maximo = df[col].max()
        per_90 = np.percentile(df[col], 90)
        per_10 = np.percentile(df[col], 10)
        if minimo == per_90 or maximo == per_10:
            low_variance.append(col)
    return low_variance



def constant_columns(df):
    """
    Identify constant columns in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    tuple: Two lists of names of constant columns (numeric and string types).
    """
    cte_cols = []
    cte_str_cols = []
    for col in df.select_dtypes(include=np.number):
        if len(df[col].apply(lambda x: tuple(x) if isinstance(x, list) else x).unique()) == 1:
            cte_cols.append(col)
    for col in df.select_dtypes(include='object'):
        if len(df[col].apply(lambda x: tuple(x) if isinstance(x, list) else x).unique()) == 1:
            cte_str_cols.append(col)
    return cte_cols, cte_str_cols



def find_special_chars(df, patron = r'[?¿*$%&]'):
    '''
    Find special characters in the DataFrame's string columns.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    patron (str): The regular expression pattern to search for special characters.

    Returns:
    None
    '''
    try:
        for col in df.select_dtypes(include = 'object').columns:
            for i in range(len(df)):
                value = df.loc[i, col]
                weird_chars = re.findall(patron, value)
                if weird_chars:
                    print(f"Columna: {col} | Fila: {i} | Caracteres raros: {weird_chars}")
    except:
        pass