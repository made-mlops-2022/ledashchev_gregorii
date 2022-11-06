HW_1 Mlops Project
--------
There are two ways of model fitting. The first one is based on transformed data, another on raw. You can choose the way of data preparation and model fitting via configuration files.

Project starting:
-------

### 1. Dataset is taken from here:
```
https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci
```
And saved in the folder ``` /data/raw/heart_cleveland_upload.csv```.

### 2. To create test and train datasets run:
#### a. On data withonut transformations:
```
python ml_examlple/data/make_dataset.py config/data_creation_config.yaml
```
Output files will be stored at ```data/processed/not_transformed```.

#### b. On data with transformations:
```
python ml_examlple/data/make_dataset.py config/data_creation_transformed_config.yaml
```
Output files will be stored at ```data/processed/transformed```.

### 3. To fit model :
#### a. On not transformed data run:
```
python ml_examlple/models/train_model.py config/train_config.yaml
```

#### b. On transformed data run:
```
python ml_examlple/models/train_model.py config/train_config_on_transformed.yaml
```

Model will be stored at ```/models/```.

### 4. To predict result:
```
```
Result and report will be stored at ```/reports/```.

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
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── logs               <- Logs of all the project 
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    ├── ml_example                <- Source code for use in this project.
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



