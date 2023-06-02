import pandas as pd
import numpy as np

def create_sum_column(df, column1, column2):
    """
    Create a new column in the DataFrame that contains the sums of two specified columns, handling NaN values accordingly.
    
    The function creates a new column named 'sum_column' in the provided DataFrame by summing the values in the specified
    columns. It handles NaN values as follows:
    - If both values are NaN, the sum is NaN.
    - If one value is NaN and the other is a number, the NaN value is treated as 0 and the sum is calculated accordingly.
    - If both values are numbers, the sum is calculated as usual.
    
    Parameters:
    - df (DataFrame): The input DataFrame.
    - column1 (str): The name of the first column.
    - column2 (str): The name of the second column.
    
    Returns:
    - DataFrame: The updated DataFrame with the new 'sum_column' added.
    """
    
    # Create the new column based on the conditions
    df['sum_column'] = np.where(
        df[column1].isnull() & df[column2].isnull(),  # NaN and NaN
        np.nan,  # If both values are NaN, set the sum to NaN
        df[column1].fillna(0) + df[column2].fillna(0)  # Otherwise, calculate the sum (treat NaN as 0)
    )
    
    return df


# Example usage
'''
data = {
    'rate_nalezy_dummy': [0.0, 0.0, 1.0, 0.0, 1.0],
    'rate_mince_dummy': [0.0, 0.0, 0.0, np.nan, 1.0]
}

df = pd.DataFrame(data)

df = create_sum_column(df, 'rate_nalezy_dummy', 'rate_mince_dummy')

print(df)
'''