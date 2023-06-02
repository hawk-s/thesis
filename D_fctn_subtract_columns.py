import pandas as pd

def subtract_columns(df, column1, column2, result_column='subtraction'):
    """
    Calculates the subtraction of one column from another in a Pandas DataFrame and adds a new column.
    
    Parameters:
        df (pandas.DataFrame): The input DataFrame.
        column1 (str): The name of the column from which subtraction will be performed.
        column2 (str): The name of the column to subtract.
        result_column (str, optional): The name of the resulting column (default is 'subtraction').
        
    Returns:
        pandas.DataFrame: A modified DataFrame with an additional column that contains
                          the subtraction of the specified columns.
    """
    # Perform the subtraction and assign it to a new column with the specified name
    df[result_column] = df[column1] - df[column2]
    
    return df
