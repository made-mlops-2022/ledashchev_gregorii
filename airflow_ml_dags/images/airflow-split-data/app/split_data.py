import os
import click
from sklearn.model_selection import train_test_split
import pandas as pd


@click.command("split_data")
@click.option("--input-dir")
@click.option("--output-dir")
def split_data(input_dir: str, output_dir: str):
    x = pd.read_csv(os.path.join(input_dir, "data.csv"))
    y = pd.read_csv(os.path.join(input_dir, "target.csv"))
    os.makedirs(output_dir, exist_ok=True)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.33, random_state=42)
    for data, filename in (
            (x_train, 'x_train'),
            (x_test, 'x_test'),
            (y_train, 'y_train'),
            (y_test, 'y_test'),
    ):
        data.to_csv(os.path.join(output_dir, f"{filename}.csv"), index=False)


if __name__ == '__main__':
    split_data()
