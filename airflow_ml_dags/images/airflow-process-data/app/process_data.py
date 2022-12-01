import os
import click
import pandas as pd


@click.command("process_data")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--process-target")
def process_data(input_dir: str, output_dir: str, process_target: str):
    x = pd.read_csv(os.path.join(input_dir, "data.csv"))
    y = None
    if process_target == 'true':
        y = pd.read_csv(os.path.join(input_dir, "target.csv"))
    os.makedirs(output_dir, exist_ok=True)
    x['dummy_column'] = 1
    x.to_csv(os.path.join(output_dir, "data.csv"), index=False)
    if process_target == 'true':
        y.to_csv(os.path.join(output_dir, "target.csv"), index=False)


if __name__ == '__main__':
    process_data()
