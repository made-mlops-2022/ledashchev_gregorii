from sklearn.linear_model import LogisticRegression
import click
import pandas as pd
from load_training_params import read_model_training_params, ModelFittingParams
import logging
import os
from pathlib import Path
import joblib
import numpy as np


@click.command(name="fit_model")
@click.argument('path')
def fit_model(path: str):
    model = LogisticRegression(max_iter=1000, tol=1e-6)
    params = read_model_training_params(path)
    x_train = pd.read_csv(f'{params.path_to_data}x_train.csv')
    y_train = pd.read_csv(f'{params.path_to_data}y_train.csv')
    model.fit(x_train, np.array(y_train).ravel())
    with open(params.report_file, 'w') as report_file:
        for column, coefficient in zip(x_train.columns, model.coef_.ravel()):
            print(f"{column}:{coefficient}", file=report_file)
    joblib.dump(model, params.path_to_model)
    logger = logging.getLogger(__name__)
    logger.info('Model fitted')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    project_dir = Path(__file__).resolve().parents[2]
    logging.basicConfig(level=logging.INFO,
                        format=log_fmt,
                        filename=os.path.join(project_dir, r'log/my_project.log'))
    error_logger = logging.getLogger(__name__)
    try:
        fit_model()
    except Exception as err:
        error_logger.error(f'Error while Fitting model: {err}')
