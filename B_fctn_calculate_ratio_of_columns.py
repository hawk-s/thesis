'''
import pandas as pd

def calculate_archeo_share(filename):
    """
    Calculate the share of archeological sites in an area.

    This function reads an Excel file containing data about archeological sites and area measurements. It calculates
    the share of archeological sites in the given area and adds a new variable called 'archeo_share' to the DataFrame.

    Args:
        filename (str): The name of the Excel file (.xlsx) containing the data.

    Returns:
        pandas.DataFrame: The DataFrame with the added 'archeo_share' variable.

    Example:
        filename = 'summed_areas_pocet_final.xlsx'
        result_df = calculate_archeo_share(filename)
        print(result_df)
    """
    df = pd.read_excel(filename)
    df.drop(columns=['Unnamed: 0_x', 'Unnamed: 0', 'Unnamed: 0_y'], inplace=True)
    df['archeo_share'] = df['pocet_lokalit'] / df['vymera_y']
    return df
'''
import pandas as pd

def calculate_ratio(df, numerator_column, denominator_column, result_column):
    """
    Calculate the ratio of two columns and create a new column in the DataFrame.

    This function calculates the ratio of a numerator column divided by a denominator column in the given DataFrame.
    It creates a new column in the DataFrame to store the calculated ratios.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        numerator_column (str): The name of the column to be used as the numerator.
        denominator_column (str): The name of the column to be used as the denominator.
        result_column (str): The name of the column to be created for storing the calculated ratios.

    Returns:
        pandas.DataFrame: The DataFrame with the added column for the calculated ratios.

    Example:
        df = pd.read_excel('summed_areas_pocet_final.xlsx')
        result_df = calculate_ratio(df, 'pocet_lokalit', 'vymera_y', 'archeo_share')
        print(result_df)
    """
    df[result_column] = df[numerator_column] / df[denominator_column]
    return df
