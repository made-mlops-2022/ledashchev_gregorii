import numpy as np
from sklearn.linear_model import Lasso
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def get_train_test(df: pd.DataFrame, test_ratio: float) -> (pd.DataFrame, pd.DataFrame):
    """ Train-test split"""
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    test_border = int(len(df) * (1 - test_ratio))
    df_train = df.iloc[:test_border, :]
    df_test = df.iloc[test_border:, :]
    return df_train, df_test


def delete_outliers(df_train: pd.DataFrame, columns: list, border: float = 0) -> pd.DataFrame:
    """
    border is value of quantile of feature values that are assumed as outlier.
    Return rows from dataframe, where values are in interval (border, 1 - border)
    """
    outliers = {}
    for col in columns:
        outliers[col] = (np.quantile(df_train[col], border),
                         np.quantile(df_train[col], 1 - border))
    df_train_no_outliers = df_train.copy()
    for col in columns:
        df_train_no_outliers = df_train_no_outliers[
            (outliers[col][0] <= df_train_no_outliers[col]) &
            (df_train_no_outliers[col] <= outliers[col][1])]
    return df_train_no_outliers


def get_useful_columns(x_train: pd.DataFrame, y_train: pd.DataFrame, columns: list,
                       lasso_alpha: float) -> list:
    """
    Using l1-regularization for feature selection
    """
    model = Lasso(alpha=lasso_alpha, max_iter=1000)
    model.fit(x_train, y_train)
    useful_cols = []
    for column, coefficient in zip(columns, model.coef_.ravel()):
        if coefficient > 0:
            useful_cols.append(column)
    return useful_cols


def get_columns(df: pd.DataFrame, drop_columns: list, target_name: str) -> list:
    """
    Drop some columns and drop target column.
    """
    columns = list(df.columns)
    columns.remove(target_name)
    for to_drop in drop_columns:
        columns.remove(to_drop)
    return columns


def get_transform_options(df_train: pd.DataFrame, default_columns: list, target_name: str,
                          outlier_border: float, lasso_alpha: float) -> \
        (pd.DataFrame, pd.DataFrame, MinMaxScaler, list):
    """
    This function tries to solve two separate problems:
    1. Crate x_test and y_test
    2. Using x_test create instances for future data transforming pipeline:
        a. MinMaxScaler
        b. Selected features
    Since x_test is calculated while pipeline instances are creating
    it is returned as result of the function.
    """
    df_train_no_outliers = delete_outliers(df_train, default_columns, outlier_border)
    x_train, y_train = df_train_no_outliers[default_columns], df_train_no_outliers[target_name]
    scaler = MinMaxScaler()
    scaler.fit(x_train)
    x_train = pd.DataFrame(scaler.transform(x_train), columns=default_columns)
    useful_columns = get_useful_columns(x_train, y_train, default_columns, lasso_alpha)
    return x_train[useful_columns], y_train, scaler, useful_columns


def transform(df_test: pd.DataFrame, default_columns: list, scaler: MinMaxScaler,
              useful_columns: list, target_name: str) -> (pd.DataFrame, pd.DataFrame):
    """
    Transform data
    """
    x_test = pd.DataFrame(
        scaler.transform(df_test[default_columns]), columns=default_columns)[useful_columns]
    return x_test, df_test[target_name]
