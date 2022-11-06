from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class DataCreatingParams:
    input_filepath: str
    output_filepath: str
    lasso_alpha: float
    outlier_border: float
    test_ratio: float
    drop_cols: list
    target_name: str


DataCreatingParamsSchema = class_schema(DataCreatingParams)


def read_data_creating_params(path: str) -> DataCreatingParams:
    with open(path, "r") as input_stream:
        schema = DataCreatingParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
