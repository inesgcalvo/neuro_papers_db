import re
import asyncio
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Functions for DataFrames

def remove_spaces_column_names(df):
    '''
    Remove leading and trailing spaces from the column names.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    pandas.Index: DataFrame column names without empty spaces.
    '''
    df.columns = df.columns.str.strip()
    return df.columns

def remove_spaces_columns(df):
    '''
    Remove leading and trailing spaces from the entries in the DataFrame columns.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    pandas.DataFrame: DataFrame with no empty spaces in column cells.
    '''
    for col in df.select_dtypes(include = 'object'):
        df[col] = df[col].str.strip()
    return df

def any_duplicate(df):
    '''
    Check if there are any duplicate rows in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    bool: Boolean value representing whether there are any duplicate rows.
    '''
    return df.duplicated().any()

def specific_duplicates(df, cols):
    '''
    Extract a DataFrame of specific duplicated rows based on the specified columns.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    cols (list): A list of column names to check for duplicates.

    Returns:
    pandas.DataFrame: DataFrame with the specified duplicates.
    '''
    duplicates = df.duplicated(subset = cols, keep = False)
    return df[duplicates]

def drop_duplicates(df):
    '''
    Drop duplicate rows from the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    None
    '''
    return df.drop_duplicates(inplace = True)

def nan(df):
    '''
    Count the number of NaN values in each column of the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    pandas.Series: A series containing the column names and the amount of NaN values.
    '''
    return df.isna().sum().sort_values(ascending = False)

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
    for col in df.select_dtypes(include = np.number):
        if len(df[col].unique()) == 1:
            cte_cols.append(col)          
    for col in df.select_dtypes(include = 'object'):
        if len(df[col].unique()) == 1:
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

def unique_values(df):
    '''
    Find the number of unique values in each column of the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    list: A list of tuples containing the column name and the count of unique values in each column.
    '''
    return sorted([(col, len(df[col].unique())) for col in df.columns], key = lambda x: x[1])


# Asincrono

def asincrono(funcion):
    '''
    Asynchronous decorator to execute the given function.

    Parameters:
    funcion (function): The function to be executed asynchronously.

    Returns:
    function: Asynchronously executed function.
    '''
    def eventos(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, funcion, *args, **kwargs)
    
    return eventos