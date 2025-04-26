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