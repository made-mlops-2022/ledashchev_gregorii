import unittest
import pandas as pd
import numpy as np
from ml_examlple.data.data_processing_functions import get_train_test, get_columns


class TestingDataProcessing(unittest.TestCase):
    def test_get_train_test(self):
        data = pd.DataFrame(np.zeros((10, 6)))
        data_train, data_test = get_train_test(data, 0.2)
        self.assertEqual(len(data_train), 8)
        self.assertEqual(len(data_test), 2)

    def test_get_columns(self):
        data = pd.DataFrame(np.zeros((10, 6)),
                            columns=[str(_) for _ in range(6)])
        columns = get_columns(data, ['1', '2'], '5')
        self.assertListEqual(columns, ['0', '3', '4'])




if __name__ == '__main__':
    unittest.main()
