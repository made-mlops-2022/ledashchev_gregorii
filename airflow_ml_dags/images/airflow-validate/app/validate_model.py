import os
import click
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def save_figure(y, y_predicted, output_dir, name):
    fig, ax = plt.subplots()
    matrix_train = confusion_matrix(y, y_predicted)
    plt.figure(figsize=(10, 7))
    sns.heatmap(matrix_train, annot=True)
    ax.plot()
    plt.savefig(os.path.join(output_dir, f"confusion_matrix_{name}.png"))


def save_text_validation(output_dir, y_pairs):
    with open(os.path.join(output_dir, "validation_results.txt"), 'w') as validation_file:
        for y_true, y_predicted, name in y_pairs:
            print(f"{name} accuracy = {accuracy_score(y_true, y_predicted)}", file=validation_file)


@click.command("validation")
@click.option("--input-data-dir")
@click.option("--input-model-dir")
@click.option("--output-dir")
def validation(input_data_dir: str, input_model_dir: str, output_dir: str):
    x_train = pd.read_csv(os.path.join(input_data_dir, "x_train.csv"))
    x_test = pd.read_csv(os.path.join(input_data_dir, "x_test.csv"))
    y_train = pd.read_csv(os.path.join(input_data_dir, "y_train.csv"))
    y_test = pd.read_csv(os.path.join(input_data_dir, "y_test.csv"))
    model = joblib.load(os.path.join(input_model_dir, "model.joblib"))
    os.makedirs(output_dir, exist_ok=True)
    y_train_predicted = model.predict(x_train)
    y_test_predicted = model.predict(x_test)

    save_text_validation(output_dir, (
        (y_train, y_train_predicted, 'train'),
        (y_test, y_test_predicted, 'test')
    ))

    save_figure(y_train, y_train_predicted, output_dir, 'train')
    save_figure(y_test, y_test_predicted, output_dir, 'test')


if __name__ == '__main__':
    validation()
