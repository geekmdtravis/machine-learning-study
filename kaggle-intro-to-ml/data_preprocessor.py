
import pandas as pd

def process(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Preprocesses the data.
    - Converts column names to lowercase
    - Drops rows with missing values
    '''
    df.columns = df.columns.str.lower()
    df.dropna(axis=0, inplace=True)
    return df