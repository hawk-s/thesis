import pandas as pd
import statsmodels.api as sm
'''
def ols_analysis(data, target_col, feature_cols):
    """
    Perform an Ordinary Least Squares (OLS) analysis using specified columns.

    Parameters:
        - data (pandas.DataFrame): The input DataFrame containing the data.
        - target_col (str): The name of the target variable column.
        - feature_cols (list): A list of column names to be used as features.

    Returns:
        - model_summary (statsmodels.iolib.summary.Summary): Summary of the OLS model.

    Usage:
        data = pd.read_csv('data.csv')
        target_col = 'target_variable'
        feature_cols = ['feature1', 'feature2', 'feature3']
        model_summary = ols_analysis(data, target_col, feature_cols)
    """
    # Extract the target variable and feature columns from the DataFrame
    y = data[target_col]
    X = data[feature_cols]

    # Add a constant column to the features (intercept term)
    X = sm.add_constant(X)

    # Fit the OLS model
    model = sm.OLS(y, X)
    results = model.fit()

    # Get the summary of the OLS model
    model_summary = results.summary()

    return model_summary
'''

import pandas as pd
import statsmodels.api as sm

def ols_analysis(data, target_col, feature_cols):
    """
    Perform an Ordinary Least Squares (OLS) analysis using specified columns,
    while checking for potential issues in the data.

    Parameters:
        - data (pandas.DataFrame): The input DataFrame containing the data.
        - target_col (str): The name of the target variable column.
        - feature_cols (list): A list of column names to be used as features.

    Returns:
        - model_summary (statsmodels.iolib.summary.Summary): Summary of the OLS model.

    Usage:
        data = pd.read_csv('data.csv')
        target_col = 'target_variable'
        feature_cols = ['feature1', 'feature2', 'feature3']
        model_summary = ols_analysis(data, target_col, feature_cols)
    """

    # Check for missing values
    if data[target_col].isnull().any() or data[feature_cols].isnull().any().any():
        raise ValueError("Missing values found in the target or feature columns.")

    # Check data types
    if not pd.api.types.is_numeric_dtype(data[target_col]) or not all(pd.api.types.is_numeric_dtype(data[col]) for col in feature_cols):
        raise ValueError("Target or feature columns contain non-numeric data.")

    # Data preprocessing
    # You can add your own preprocessing steps here, such as handling missing values or scaling features.
    # Make sure to modify the code based on your specific preprocessing needs.

    # Extract the target variable and feature columns from the DataFrame
    y = data[target_col]
    X = data[feature_cols]

    # Add a constant column to the features (intercept term)
    X = sm.add_constant(X)

    # Fit the OLS model
    model = sm.OLS(y, X)
    results = model.fit()

    # Get the summary of the OLS model
    model_summary = results.summary()

    return model_summary
