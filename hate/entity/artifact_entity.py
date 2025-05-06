import os
from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    FileList: list

@dataclass
class DataTransformationArtifacts:
    transformed_file: str

@dataclass
class ModelTrainArtifacts:
    trained_model_path:str
    x_test_path: list
    y_test_path: list

@dataclass
class ModelEvalArtifacts:
    is_model_accepted:bool

@dataclass
class ModelPushArtifacts:
    bucket_name:str
