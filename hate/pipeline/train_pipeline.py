import os
import sys
from hate.components import model_evaluation
from hate.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts, ModelEvalArtifacts, ModelTrainArtifacts
from hate.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelPushConfig, ModelTrainConfig, ModelEvalConfig
from hate.logger import logging
from hate.exception import CustomException
from hate.constant import *
from hate.components.data_ingestion import DataIngestion
from hate.components.data_transformation import DataTransformation
from hate.components.model_evaluation import ModelEvaluation
from hate.components.model_train import ModelTrain
from hate.components.model_push import ModelPush
class Train_pipeline():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transform_config = DataTransformationConfig()
        self.model_train_config = ModelTrainConfig()
        self.model_eval_config = ModelEvalConfig()
        self.model_push_config = ModelPushConfig()
    
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

    def start_data_transformation(self,data_ingestion_artifacts:DataIngestionArtifacts) -> DataTransformationArtifacts:
        logging.info("Entering Start Data Transformation utility")
        try:
            data_transformation = DataTransformation(self.data_transform_config,data_ingestion_artifacts)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info("Exiting Start Data Transformation utility")
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e, sys) from e
    def start_model_train(self, data_transformation_artifacts:DataTransformationArtifacts)->ModelTrainArtifacts:
        logging.info("Entering Start Model Training")
        try:
            model_train = ModelTrain(data_transformation_artifacts,self.model_train_config)
            model_train_artifact = model_train.start_model_train()
            logging.info("Model Training completed")
            return model_train_artifact
        except Exception as e:
            raise CustomException(e,sys) from e

    def start_model_eval(self,model_train_artifacts:ModelTrainArtifacts)->ModelEvalArtifacts:
        logging.info("Entered the Start Model Eval Activity")
        try:
            model_evaluation = ModelEvaluation(model_train_artifacts,self.model_eval_config)
            model_evaluation_artifacts = model_evaluation.start_model_evaluation()
            return model_evaluation_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e

    def start_model_push(self):
        logging.info("Entered the start model push activity")
        try:
            model_push = ModelPush(self.model_push_config)
            model_push_artifacts = model_push.initiate_model_push()
            return model_push_artifacts
        except Exception as e:
            raise CustomException(e,sys) from e


    def run_pipeline(self):
        logging.info("Starting run pipleine process")
        try:
            ingestion_artifacts = self.start_data_ingestion()
            transformation_artifacts = self.start_data_transformation(ingestion_artifacts)
            model_train_artifacts = self.start_model_train(transformation_artifacts)
            model_eval_artifacts = self.start_model_eval(model_train_artifacts)

            if model_eval_artifacts.is_model_accepted is False:
                raise Exception("Trained Model is not better")

            self.start_model_push()

        except Exception as e:
            raise CustomException(e,sys) from e
