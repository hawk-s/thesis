import pandas as pd

def save_dataframe_to_json(df, file_path, orient='records', force_ascii=False, encoding='utf-8'):
    """
    Save a Pandas DataFrame as a JSON file.
    
    Parameters:
        df (pandas.DataFrame): The DataFrame to be saved.
        file_path (str): The path to save the JSON file.
        orient (str, default='records'): The orientation of the JSON file.
            - 'records': Each row of the DataFrame is saved as a separate JSON object.
            - 'index': The DataFrame is saved with the index as keys.
        force_ascii (bool, default=False): Whether to escape non-ASCII characters.
        encoding (str, default='utf-8'): The encoding to use when saving the file.
    
    Returns:
        None
    """
    with open(file_path, 'w', encoding=encoding) as file:
        df.to_json(file, orient=orient, force_ascii=force_ascii)

