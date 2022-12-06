import os
import click
import joblib
import pandas as pd


@click.command("prediction")
@click.option("--input-data-dir")
@click.option("--input-model-dir")
@click.option("--output-dir")
def prediction(input_data_dir: str, input_model_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_data_dir, "data.csv"))
    model = joblib.load(os.path.join(input_model_dir, "model.joblib"))
    os.makedirs(output_dir, exist_ok=True)
    y_predicted = pd.DataFrame(model.predict(data))
    y_predicted.to_csv(os.path.join(output_dir, "predictions.csv"), index=False)


if __name__ == '__main__':
    prediction()
