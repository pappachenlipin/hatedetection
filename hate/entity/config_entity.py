import os
from hate.constant import *
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.ARTIFACTS_DIR = ARTIFACTS_DIR
        self.ZIP_FILE_NAME = ZIP_FILE_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR,self.ZIP_FILE_NAME)

@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRANSFORMED_FILE_PATH = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,TRANSFORMED_FILE_NAME)
        self.DROP_COLUMNS = DROP_COLUMNS
        self.AXIS = AXIS
        self.INPLACE = INPLACE
        self.TEXT_COL = TEXT_COL

@dataclass
class ModelConfig:
    def __init__(self):
        self.EMBEDDING_SIZE = EMBEDDING_SIZE
        self.MAX_SEQ_LENGTH = MAX_SEQ_LENGTH
        self.NUM_OF_LAYERS = NUM_OF_LAYERS
        self.VOCAB_SIZE = VOCAB_SIZE
        self.DROP_OUT = DROP_OUT
        self.OUTPUT_SIZE = OUTPUT_SIZE
        self.ACTIVATION = ACTIVATION
        self.METRICS = METRICS
        self.LOSS = LOSS


@dataclass 
class ModelTrainConfig:
    def __init__(self):
        self.NUMBER_OF_EPOCHS = NUMBER_OF_EPOCHS
        self.TRAIN_TEST_SPLIT_RATIO = TRAIN_TEST_SPLIT_RATIO
        self.MODEL_TRAIN_ARTIFACTS_DIR = MODEL_TRAIN_ARTIFACTS_DIR
        self.MODEL_TRAIN_ARTIFACTS_PATH = os.path.join(os.getcwd(),ARTIFACTS_DIR,MODEL_TRAIN_ARTIFACTS_DIR)
        self.TRAINED_MODEL_NAME = TRAINED_MODEL_NAME
        self.X_TRAIN_FILE_NAME = X_TRAIN_FILE_NAME
        self.Y_TRAIN_FILE_NAME = Y_TRAIN_FILE_NAME
        self.X_TEST_FILE_NAME = X_TEST_FILE_NAME
        self.Y_TEST_FILE_NAME = Y_TEST_FILE_NAME
        self.BATCH_SIZE = BATCH_SIZE
        self.X_TRAIN_FILE_PATH = os.path.join(self.MODEL_TRAIN_ARTIFACTS_PATH,X_TRAIN_FILE_NAME)
        self.X_TEST_FILE_PATH = os.path.join(self.MODEL_TRAIN_ARTIFACTS_PATH,X_TEST_FILE_NAME)
        self.VALIDATION_SPLIT = VALIDATION_SPLIT
        self.Y_TEST_FILE_PATH = os.path.join(self.MODEL_TRAIN_ARTIFACTS_PATH,Y_TEST_FILE_NAME)

@dataclass
class ModelEvalConfig:
    def __init__(self):
        self.MODEL_EVAL_ARTIFACTS_DIR = MODEL_EVAL_ARTIFACTS_DIR
        self.MODEL_EVAL_ARTIFACTS_PATH = os.path.join(os.getcwd(),ARTIFACTS_DIR,self.MODEL_EVAL_ARTIFACTS_DIR)
        self.BEST_MODEL_DIR = os.path.join( self.MODEL_EVAL_ARTIFACTS_PATH,BEST_MODEL_DIR)
        self.MODEL_EVALUATION_FILE_NAME = MODEL_EVALUATION_FILE_NAME
        self.BUCKET_NAME = BUCKET_NAME
        self.MODEL_NAME = TRAINED_MODEL_NAME

@dataclass
class ModelPushConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.MODEL_NAME = TRAINED_MODEL_NAME
        self.MODEL_TRAIN_ARTIFACTS_PATH =  os.path.join(os.getcwd(),ARTIFACTS_DIR,MODEL_TRAIN_ARTIFACTS_DIR)