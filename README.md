HW_1 Ml Ops Project
--------

# Basic info:

1) Project architecture notes are contained in file ```architecture.md``` and written in pull-request.

2) Estimation of done work is described in file ```self_esimation.md```.

3) Shortly: There are two ways of model fitting. The first one is based on transformed data, another on raw. You can
   choose the way of data preparation and model fitting via configuration files.

4) Dataset is taken from here:


https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci


And saved in the folder ``` /data/raw/heart_cleveland_upload.csv```.

# Project starting:

### 1. Install dependencies.

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. To create test and train datasets run:

```
python ml_project/data/make_dataset.py SOME_YAML_CONFIG.yaml
```

#### Examples:

#### a. On data without transformations:

```
python ml_project/data/make_dataset.py config/data_creation_config.yaml
```

Output files will be stored at ```data/processed/not_transformed```.

#### b. On data with transformations:

```
python ml_project/data/make_dataset.py config/data_creation_transformed_config.yaml
```

Output files will be stored at ```data/processed/transformed```.

### 3. To fit model:

```
python ml_project/models/train_model.py SOME_YAML_CONFIG.yaml
```

#### Examples:

#### a. On not transformed data run:

```
python ml_project/models/train_model.py config/train_config.yaml
```

#### b. On transformed data run:

```
python ml_project/models/train_model.py config/train_config_on_transformed.yaml
```

Fitted model will be stored at ```/models/```.

### 4. To predict result run:

```
python ml_project/models/predict.py SOME_MODEL.joblib YOUR_DATAFRAME.csv PATH_TO_STORE_PREDICTED_RESULT 
```

#### Example on transformed data:

```
python ml_project/models/predict_model.py models/linear_model_on_transformed.joblib data/processed/transformed/x_train.csv ml_project/predictions/y_predicted.csv
```

Result will be stored at ```/ml_project/predictions/y_predicted.csv```.

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data    
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── predictions        <- Predictions of model
    │
    ├── logs               <- Logs of all the project 
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    ├── ml_project                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   └── models         <- code to train models and then use trained models to make
    │   

--------
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>



