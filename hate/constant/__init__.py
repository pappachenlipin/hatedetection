from datetime import datetime
import os

# Define all the constant values

TIMESTAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
BUCKET_NAME = "hatedetection"
ARTIFACTS_DIR = os.path.join("artifacts",TIMESTAMP)
ZIP_FILE_NAME = "dataset.zip"

#Define the Data Ingestion constants

DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_RAW_DATA_DIR = "labeled_data.csv"

# Define the Data Transformation constants

DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
TRANSFORMED_FILE_NAME = 'Clean.csv'
TEXT_COL = 'tweet'
AXIS = 1
INPLACE = True
DROP_COLUMNS = ['Unnamed: 0','count','hate_speech','offensive_language','neither']

# Define the Model Training Params

NUMBER_OF_EPOCHS = 2
TRAIN_TEST_SPLIT_RATIO = 0.20
MODEL_TRAIN_ARTIFACTS_DIR = "ModelTrainArtifacts"
TRAINED_MODEL_NAME = "HateModel"
BATCH_SIZE = 32
X_TRAIN_FILE_NAME = "train_x.csv"
Y_TRAIN_FILE_NAME = "train_y.csv"
X_TEST_FILE_NAME = "test_x.csv"
Y_TEST_FILE_NAME = "test_y.csv"
VALIDATION_SPLIT = 0.2

# Define the Model Params

EMBEDDING_SIZE = 100
MAX_SEQ_LENGTH = 10
NUM_OF_LAYERS = 1
DROP_OUT = 0.2
VOCAB_SIZE = 50000
OUTPUT_SIZE =1
ACTIVATION = 'sigmoid'
METRICS = ['accuracy']
LOSS = 'binary_crossentropy'


# Define the evaluation params

MODEL_EVAL_ARTIFACTS_DIR = "ModelEvalArtifacts"
BEST_MODEL_DIR ="BestModel"
MODEL_EVALUATION_FILE_NAME  = "loss.csv"

#Define the model push params



