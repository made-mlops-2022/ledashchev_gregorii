from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class ModelFittingParams:
    path_to_data: str
    iterations: int
    C: float
    path_to_model: str
    report_file: str


ModelFittingParamsSchema = class_schema(ModelFittingParams)


def read_model_training_params(path: str) -> ModelFittingParams:
    with open(path, "r") as input_stream:
        schema = ModelFittingParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
