#specific fction for converting praha 7,...praha 1 to praha and keeping praha and districts praha-vychod etc...


import pandas as pd
import numpy as np

def process_municipality(df):
    """
    Process the 'municipality' column in the given DataFrame.

    Parameters:
        df (pandas.DataFrame): Input DataFrame containing the 'municipality' column.

    Returns:
        pandas.DataFrame: Processed DataFrame with an additional column 'processed_municipality'.

    Raises:
        ValueError: If the 'municipality' column is not found in the DataFrame.

    Examples:
        >>> df = pd.DataFrame({'municipality': ['Praha 2', 'Praha 8', 'Praha', 'Praha-východ', 'Praha-západ', np.nan]})
        >>> processed_df = process_municipality(df)
        >>> print(processed_df)
          municipality processed_municipality
        0       Praha 2                  Praha
        1       Praha 8                  Praha
        2         Praha                  Praha
        3  Praha-východ         Praha-východ
        4   Praha-západ          Praha-západ
        5           NaN                   NaN
    """
    if 'municipality' not in df.columns:
        raise ValueError("The 'municipality' column is not found in the DataFrame.")

    # Create a new column 'processed_municipality' initialized with the values from 'municipality' column
    df['processed_municipality'] = df['municipality']

    # Identify rows where the value starts with 'Praha ' (e.g., 'Praha 2', 'Praha 8')
    mask_praha_number = df['municipality'].str.startswith('Praha ', na=False)

    # Identify rows where the value ends with '-východ' or '-západ'
    mask_vychod_zapad = df['municipality'].str.endswith(('-východ', '-západ'), na=False)

    # Update 'processed_municipality' column based on the identified masks
    df.loc[mask_praha_number, 'processed_municipality'] = 'Praha'
    df.loc[mask_vychod_zapad, 'processed_municipality'] = df['municipality']

    return df
