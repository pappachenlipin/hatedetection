from ast import Try
from math import e
import os
import sys
from zipfile import ZipFile
from hate.constant import *
from hate.entity.config_entity import DataIngestionConfig
from hate.configuration.gccloud_syncer import GCCloud
from hate.logger import logging
from hate.exception import CustomException
from hate.entity.artifact_entity import DataIngestionArtifacts

class DataIngestion:
    def __init__(self, dataingestionconfig:DataIngestionConfig):
        self.dataingestionconfig = dataingestionconfig
        self.gccloud = GCCloud()
    def get_data_from_gcp(self):

        logging.info("Entering get data from gcp to pull data from gcp")
        #Create a new directory under Artificats
        try:
            os.makedirs(self.dataingestionconfig.DATA_INGESTION_ARTIFACTS_DIR, exist_ok = True)
            self.gccloud.get_data_from_gccloud(self.dataingestionconfig.BUCKET_NAME,self.dataingestionconfig.ZIP_FILE_NAME,
                                           self.dataingestionconfig.DATA_INGESTION_ARTIFACTS_DIR)
           
            logging.info("Existing get data from gcp to pull data from gcp")
        except Exception as e:
            raise CustomException(e, sys) from e

    def unzip_and_clean(self):
        logging.info("Entered the unzip and clean of Data Ingestion class")
        try:
            with ZipFile(self.dataingestionconfig.ZIP_FILE_PATH, mode = 'r') as zip_ref:
                zip_ref.extractall(self.dataingestionconfig.ZIP_FILE_DIR)
            artifact_files = [os.path.join(self.dataingestionconfig.ZIP_FILE_DIR, i) for i in zip_ref.namelist()]
            logging.info("Existed the unzip and clean of Data Ingestion class")
            return artifact_files
        except Exception as e:
            raise CustomException(e, sys) from e
    def initiate_data_ingestion(self)->DataIngestionArtifacts:
        """
        Method initiates the data ingestion process with first pulling the data from gcp"""
        logging.info("Starting the Data Ingestion Pipeline")
        try:
            self.get_data_from_gcp()
            logging.info("Fetched the data from GCP")
            logging.info("Calling unzip and clean data")
            artifact_files = self.unzip_and_clean()
            data_ingestion_artifacts = DataIngestionArtifacts(artifact_files)
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e

     

