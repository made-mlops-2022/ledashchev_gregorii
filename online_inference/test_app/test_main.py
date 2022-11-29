from fastapi.testclient import TestClient
import pandas as pd
from app.main import app
import pytest

client = TestClient(app)


@pytest.mark.filterwarnings("ignore:joblib")
def test_main():
    data = pd.read_csv(r'data/x_test.csv')
    sending_data = {"dataframe": data.to_json()}
    response = client.post(
        "/predict",
        json=sending_data)
    print(response)
    assert response.text == '"1,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,' \
                            '0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0"'
