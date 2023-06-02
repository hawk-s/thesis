def join_columns(dataset, column1, column2, new_column):
    """
    Joins two columns of a dataset into a new column.

    Args:
        dataset (pandas.DataFrame): The dataset containing the columns.
        column1 (str): The name of the first column to be joined.
        column2 (str): The name of the second column to be joined.
        new_column (str): The name of the new column to be created.

    Returns:
        pandas.DataFrame: The dataset with the new column added.

    Raises:
        ValueError: If either 'column1' or 'column2' is not found in the dataset.

    Example:
        >>> import pandas as pd
        >>> data = {'Name': ['Alice', 'Bob', 'Charlie'],
        ...         'Age': [25, 30, 35]}
        >>> df = pd.DataFrame(data)
        >>> df
             Name  Age
        0    Alice   25
        1      Bob   30
        2  Charlie   35
        >>> join_columns(df, 'Name', 'Age', 'NameAge')
             Name  Age    NameAge
        0    Alice   25   Alice25
        1      Bob   30     Bob30
        2  Charlie   35  Charlie35
    """
    if column1 not in dataset.columns:
        raise ValueError(f"Column '{column1}' not found in the dataset.")
    if column2 not in dataset.columns:
        raise ValueError(f"Column '{column2}' not found in the dataset.")

    dataset[new_column] = dataset[column1].astype(str) + dataset[column2].astype(str)
    return dataset
