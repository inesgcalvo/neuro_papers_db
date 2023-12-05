import pandas as pd

# Functions to create a database from a folder

def create_dictio(df):
    '''
    Create a dictionary of column names and their corresponding SQL data types based on the provided DataFrame.

    Parameters:
    - df (pandas.DataFrame): The DataFrame for which the dictionary is created.

    Returns:
    - dict: A dictionary where keys are column names, and values are their corresponding SQL data types.
    '''
    column_types= {}
    for e in df:
        if ('float' in str(df[e].dtype)):
            column_types[e]='FLOAT'
        elif ('int' in str(df[e].dtype)):
            column_types[e]='INT'
        else:
            column_types[e]='VARCHAR'
    return column_types



def create_table(table_name, column_names_types, cursor):
    '''
    Create a SQL table with the specified table name and column names and types.

    Parameters:
    - table_name (str): The name of the table to be created.
    - column_names_types (dict): A dictionary where keys are column names, and values are their corresponding SQL data types.
    - cursor (cursor): The cursor object to execute SQL queries.

    Returns:
    - None
    '''
    cursor.execute(f'DROP TABLE IF EXISTS `{table_name}`;\n')
    query = f'CREATE TABLE `{table_name}`('
    for key, value in column_names_types.items():
        query += f'{key} {value}, '
    cursor.execute(query[:-2] + ');')



def create_tables(db_structure, cursor):
    '''
    Create SQL tables based on the specified database structure and insert values from corresponding CSV files.

    Parameters:
    - db_structure (dict): A dictionary defining the structure of the database, including table names, primary keys, and foreign keys.
    - cursor (cursor): The cursor object to execute SQL queries.

    Returns:
    - None
    '''
    for table, keys in db_structure.items():
        df = pd.read_csv(f'../../data/neuropapers_db/{table}.csv')
        # Call create_table
        create_table(table, create_dictio(df), cursor)
        if 'primary_keys' in keys:
            primary_keys_str = ', '.join([f'`{pk}`' for pk in keys['primary_keys']])
            primary_key_query = f'ALTER TABLE `{table}` ADD PRIMARY KEY ({primary_keys_str});'
            cursor.execute(primary_key_query)
        if 'foreign_keys' in keys:
            for fk_info in keys['foreign_keys']:
                foreign_key_str = ', '.join([f'`{fk}`' for fk in fk_info['fk']])
                reference_str = f"`{fk_info['reference_table']}` (`{fk_info['reference_column']}`)"
                foreign_key_query = f'ALTER TABLE `{table}` ADD FOREIGN KEY ({foreign_key_str}) REFERENCES {reference_str};'
                cursor.execute(foreign_key_query)
        # Call insert_values
        insert_values(table, df, cursor)



def insert_values(table_name, df, cursor):
    '''
    Insert values into a SQL table based on the specified DataFrame.

    Parameters:
    - table_name (str): The name of the table to insert values into.
    - df (pandas.DataFrame): The DataFrame containing the values to be inserted.
    - cursor (cursor): The cursor object to execute SQL queries.

    Returns:
    - None
    '''
    column_names = ','.join(df.columns)
    for i in range(df.shape[0]):     
        values = tuple(df.iloc[i].values)   
        cursor.execute(f'insert into `{table_name}` ({column_names}) values {values};')