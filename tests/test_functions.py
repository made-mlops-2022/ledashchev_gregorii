import pytest
import pandas as pd
import numpy as np
from ml_project.data.data_processing_functions import get_train_test, get_columns


def test_get_train_test():
    with pytest.raises(AttributeError):
        get_train_test(0, 0)
    data = pd.DataFrame(np.zeros((10, 6)))
    data_train, data_test = get_train_test(data, 0.2)
    assert len(data_train) == 8
    assert len(data_test) == 2


def test_get_columns():
    data = pd.DataFrame(np.zeros((10, 6)),
                        columns=[str(_) for _ in range(6)])
    columns = get_columns(data, ['1', '2'], '5')
    assert columns == ['0', '3', '4']
