import os
import sys
from hate.entity.artifact_entity import DataIngestionArtifacts
from hate.entity.config_entity import DataIngestionConfig
from hate.logger import logging
from hate.exception import CustomException
from hate.constant import *
from hate.components.data_ingestion import DataIngestion
class Train_pipeline():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start data ingestion utility from pipeline")
        try:
            logging.info("Initialize the data ingestion object")
            data_ingestion = DataIngestion(dataingestionconfig=self.data_ingestion_config)
            logging.info("Call the Initiate Data Ingestion function")
            artifacts = data_ingestion.initiate_data_ingestion()
            return artifacts
        except Exception as e:
            raise CustomException(e,sys) from e

    def run_pipeline(self):
        logging.info("Starting run pipleine process")
        try:
            artifacts = self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys) from e
