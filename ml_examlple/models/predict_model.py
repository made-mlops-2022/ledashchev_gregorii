import click
import pandas as pd
import joblib


@click.command(name="model_predict")
@click.argument('serialized_model_path')
@click.argument('x_test_path')
def model_predict(serialized_model_path, x_test_path):
    x_test = pd.read_csv(x_test_path)
    model = joblib.load(serialized_model_path)
    y_predicted = model.predict(x_test)
    pd.DataFrame(y_predicted).to_csv('reports/y_predicted.csv', index=False)


if __name__ == '__main__':
    model_predict()
