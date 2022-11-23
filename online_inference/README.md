Online API for predicting
----
# Start without docker
```commandline
pip install -r requirements.txt
cd app
uvicorn main:app --reload    
```

# Docker

### Build from local
#### Build:
```commandline
docker build -t predict_image .
```

#### Run:
```commandline
docker run -d --rm --name predict_container -p 80:80 predict_image
```
### Get from hub
#### Pull:
```commandline
docker pull gregor256/predict_image
```
#### Run:
```commandline
docker run -d --rm --name predict_container -p 80:80 gregor256/predict_image
```
# Convenient usage
API structure: it runs on
`http://127.0.0.1:80/`
There are two endpoints
`/predict` and `/health`.
Both can receive http POST-requests.
To use API run 
``` 
python client/send_request.py [ENDPOINT] [PATH_TO_DATA] [OUTPUT]
```

```[ENDPOINT] ``` might be `predict` or `health` <br>
`/health` receives empty request and return 200 in case API is ready, so it doesn't require any parameter. <br>
```[PATH_TO_DATA]``` is path to DATAFRAME.csv you want to predict. For example `data/x_test.csv` <br>
```[OUTPUT]``` path to file where you want to save model predict. By default, standard output. <br>
e.i.
```
python client/send_request.py predict data/x_test.csv
```
# Hardcore Usage
`/predict` receives request with json-body `{"datarfame": YOUR_DATAFRAME}`. 
Where YOUR_DATAFRAME is 
```
\"sex\":{\"0\":0.0,\"1\":1.0,\"2\":1.0},
\"trestbps\":{\"0\":0.5283018868,\"1\":0.2452830189,\"2\":0.1320754717},
\"chol\":{\"0\":0.2933025404,\"1\":0.2263279446,\"2\":0.4110854503},
\"restecg\":{\"0\":1.0,\"1\":1.0,\"2\":0.0},
\"exang\":{\"0\":0.0,\"1\":1.0,\"2\":0.0},
\"oldpeak\":{\"0\":0.4193548387,\"1\":0.4193548387,\"2\":0.0},
\"slope\":{\"0\":0.5,\"1\":0.5,\"2\":0.0},
\"ca\":{\"0\":0.6666666667,\"1\":0.6666666667,\"2\":0.0},
\"thal\":{\"0\":1.0,\"1\":1.0,\"2\":1.0}}"
```
This json is a result of ```DataFrame.to_json()```.
# Testing
Run
```python -m pytest```
# Project structure
```
.
├── app                  <--- main application folder                                            
│    ├── __init__.py 
│    ├── main.py         <--- main file containing API starting
│    └── models          <--- folder with serialized ML model
│        └── linear_model_on_not_transformed.joblib
├── client
│    └── send_request.py <--- script for API requesting
├── data                 <--- csv files to test API
│    └── x_test.csv
├── Dockerfile           <--- Dockerfile
├── README.md
├── requirements.txt    <--- python packages
└── test_app            <--- tests
    │    ├── __init__.cpython-310.pyc
    │    └── test_main.cpython-310-pytest-7.2.0.pyc
    └── test_main.py
```