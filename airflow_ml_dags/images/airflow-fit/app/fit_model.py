import os
import joblib
import click
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


@click.command("fit_model")
@click.option("--input-dir")
@click.option("--output-dir")
def fit_model(input_dir: str, output_dir: str):
    x = pd.read_csv(os.path.join(input_dir, "x_train.csv"))
    y = pd.read_csv(os.path.join(input_dir, "y_train.csv"))
    os.makedirs(output_dir, exist_ok=True)
    model = DecisionTreeClassifier(random_state=0)
    model.fit(x, y)
    joblib.dump(model, os.path.join(output_dir, "model.joblib"))


if __name__ == '__main__':
    fit_model()
