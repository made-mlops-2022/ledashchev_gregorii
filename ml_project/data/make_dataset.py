import click
from load_data_processing_params import read_data_creating_params, DataCreatingParams
import logging
import os
from pathlib import Path
import pandas as pd
from data_processing_functions import get_train_test, \
    get_columns, get_transform_options, transform


def process_data(dataframe: pd.DataFrame, params: DataCreatingParams) -> (pd.DataFrame, pd.DataFrame,
                                                                          pd.DataFrame, pd.DataFrame):
    df_train, df_test = get_train_test(dataframe, params.test_ratio)
    default_columns = get_columns(dataframe, params.drop_cols, params.target_name)
    x_train, y_train, scaler, useful_columns = \
        get_transform_options(df_train, default_columns, params.target_name, params.outlier_border, params.lasso_alpha)
    x_test, y_test = transform(df_test, default_columns, scaler, useful_columns, params.target_name)
    return x_train, y_train, x_test, y_test


@click.command(name="process_data")
@click.argument('path')
def dump_processed_data(path: str):
    """
     Runs data processing scripts to turn raw data from (/data/raw) into
        cleaned data ready to be analyzed (saved in data/processed).
    """
    params = read_data_creating_params(path)
    dataframe = pd.read_csv(params.input_filepath)
    filenames = ('x_train', 'y_train', 'x_test', 'y_test')
    for dataframe, filename in zip(process_data(dataframe, params), filenames):
        dataframe.to_csv(f"{params.output_filepath}/{filename}.csv", index=False)

    logger = logging.getLogger(__name__)
    logger.info('Making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    project_dir = Path(__file__).resolve().parents[2]
    logging.basicConfig(level=logging.INFO,
                        format=log_fmt,
                        filename=os.path.join(project_dir, r'log/my_project.log'))
    error_logger = logging.getLogger(__name__)
    try:
        dump_processed_data()
    except Exception as err:
        error_logger.error(f'Error while processing dataset: {err}')
