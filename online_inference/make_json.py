import json


def csv_to_json(_table: pd.DataFrame) -> str:
    dict_data = {
        column_name: tuple(_table[column_name]) for column_name in _table.columns
    }
    return json.dumps(dict_data)


input_dataFrame = pd.read_csv(r'data/my_data.csv')
print(csv_to_json(input_dataFrame))
