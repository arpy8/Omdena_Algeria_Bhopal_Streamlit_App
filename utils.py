import numpy as np
import pandas as pd
from datetime import timedelta
from typing import Union, Optional, Any
from sklearn.base import BaseEstimator, TransformerMixin
from sktime.transformations.series.summarize import WindowSummarizer

from config import LAG_SIZE


class DateTimeFeatures(BaseEstimator, TransformerMixin):
    """
    DateTimeFeatures extracts date and time features from datetime variables, 
    adding new columns to dataset. DatetimeFeatures can extract datetime 
    information from existing datetime variables or from the dataframe index.
    """

    def __init__(self, variables: Union[None, str] = None) -> None:
        self.variables = variables
        
    def fit(self, X: pd.DataFrame, y: Optional[pd.Series]=None) -> Any:
        """
        This transformer does not learn any parameter.
        """
        if self.variables==None and not np.issubdtype(X.index.dtype, np.datetime64):
            raise TypeError("Index should have datetime type")
        if self.variables!=None and not np.issubdtype(df[self.variables].dtype, np.datetime64):
            raise TypeError("Column should have datetime type")
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Extract the date and time features and add them to the dataframe.
        """
        if self.variables==None:
            date_series = X.index.to_series()
        else:
            date_series = X[self.variables]
        X = X.assign(         
            day = date_series.dt.day,
            month = date_series.dt.month,
            #year = date_series.dt.year,
            day_of_year = date_series.dt.day_of_year,
            sin_day_of_year = np.sin(np.pi*date_series.dt.day_of_year/183),
            cos_day_of_year = np.cos(np.pi*date_series.dt.day_of_year/183),
            sin_month = np.sin(np.pi*date_series.dt.month/6),
            cos_month = np.cos(np.pi*date_series.dt.month/6),  
        )
        return X
    
def preprocessing_data(df: pd.DataFrame, target_column: str, target: bool = True) -> Any:
    """
    Perform preprocessing on the input DataFrame.

    Parameters:
    df : pd.DataFrame
        The input DataFrame containing the data.
    target_column : str
        name of target column
    target : bool, optional
        Whether to include the target variable target in the output.

    Returns:
    Any
        If target is True, returns a tuple containing the preprocessed features DataFrame
        and the target Series. If target is False, returns the preprocessed features DataFrame only.
    """

    lag_list = [i for i in range(1, LAG_SIZE+1)]
    window_list = [[1, i] for i in range(2, LAG_SIZE+1)]
    lag_window_feats = WindowSummarizer(
        lag_feature={
            "lag": lag_list,
            "mean": window_list,
            "min": window_list,
            "max": window_list,
            "sum": window_list,
            "var": window_list,
        },
        #truncate="bfill",  # Backfill missing values from lagging and windowing.
    )
    df_lag = lag_window_feats.fit_transform(df[target_column])

    # Compute Time-Features
    dtf = DateTimeFeatures()
    df_dtf = dtf.fit_transform(df)

    df_concat = pd.concat([df_dtf, df_lag], axis=1)
    if target:
        y = df_concat[target_column]
        df_concat.drop([target_column], axis=1, inplace=True)
        df_concat.dropna(axis=0, inplace=True)
        y = y[-df_concat.shape[0]:]
        return df_concat, y
    else:
        df_concat.drop([target_column], axis=1, inplace=True)
        df_concat.dropna(axis=0, inplace=True)
        return df_concat

def recursive_multi_step_forecasting_monthly(X: pd.DataFrame, target_column: str, model, days: int = 100) -> pd.DataFrame:
    """
    Perform multi-step recursive forecasting using the provided model.

    Args:
        X (pd.DataFrame): Historical data for forecasting.
        target_column (str): Name of the target column to forecast.
        model: Trained forecasting model.
        days (int): Number of days to forecast.

    Returns:
        pd.DataFrame: DataFrame containing forecasted values.
    """

    start_date = (X.index.date[-1] + timedelta(days=1)) if len(X) > 0 else pd.to_datetime('today')

    end_date = start_date + timedelta(days=days)
    date_range = pd.date_range(start=start_date, end=end_date, freq='MS')
    empty_df = pd.DataFrame(index=date_range)
    empty_df[target_column] = 0

    df_forecast = pd.concat([X[-LAG_SIZE:], empty_df], axis=0)

    for index, row in empty_df.iterrows():
        X_input = preprocessing_data(df_forecast[:index], target_column, False)
        prediction = model.predict(X_input)
        df_forecast.loc[index] = prediction[-1]
        
    return df_forecast[LAG_SIZE:]