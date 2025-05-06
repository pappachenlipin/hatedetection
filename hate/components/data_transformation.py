import os
import sys
import nltk 
import re
from nltk.corpus import stopwords
nltk.download("stopwords")
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from hate.logger import logging
from hate.constant import *
from hate.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from hate.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts
from hate.exception import CustomException


class DataTransformation:
    def __init__(self, datatransformationconfig:DataTransformationConfig, dataingestionartifact:DataIngestionArtifacts):
        self.datatransformationconfig = datatransformationconfig
        self.dataingestionartifacts = dataingestionartifact
        assert len(self.dataingestionartifacts.FileList) == 1, "There is only one file available"
        self.ingestedfilename = self.dataingestionartifacts.FileList[0]

    def processingestedfile(self):
        logging.info("Started processing of the file")
        try:
            df = pd.read_csv(self.ingestedfilename)
            df.drop(self.datatransformationconfig.DROP_COLUMNS,
                    axis = self.datatransformationconfig.AXIS,
                    inplace = self.datatransformationconfig.INPLACE)
            
            logging.info("Finished processing of the file")
            return df
        except Exception as e:
            raise CustomException(e, sys) from e

    def clean_text(self, words):
        #logging.info("Started cleaning of the text files")
        stemmer = nltk.SnowballStemmer("english")
        stopword = set(stopwords.words("english"))
        words = str(words).lower()
        words = re.sub('\[.*?\]','',words)
        words = re.sub('https?://\S+|www\.\S+', '', words)
        words = re.sub('<.*?>+', '', words)
        words = re.sub('[%s]' % re.escape(string.punctuation), '', words)
        words = re.sub('\n', '', words)
        words = re.sub('\w*\d\w*', '', words)
        words = [stemmer.stem(word) for word in words.split(' ')]
        words = " ".join(words)
        words = [word for word in words.split(' ') if word not in stopword]
        words = " ".join(words)
        #logging.info("Stopped cleaning of the text files")
        return words
        

    def initiate_data_transformation(self)->DataTransformationArtifacts:
        logging.info("Entering initiate Data Transformation")
        try:
            raw_data = self.processingestedfile()
            raw_data[self.datatransformationconfig.TEXT_COL] = raw_data[self.datatransformationconfig.TEXT_COL].apply(self.clean_text)
            os.makedirs(self.datatransformationconfig.DATA_TRANSFORMATION_ARTIFACTS_DIR, exist_ok = True)
            raw_data.to_csv(self.datatransformationconfig.TRANSFORMED_FILE_PATH,index = False, header = True)
            data_transformation_artifact = DataTransformationArtifacts(transformed_file =self.datatransformationconfig.TRANSFORMED_FILE_PATH )
            logging.info("Existing the Initiate Data Transformation")
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e,sys) from e


