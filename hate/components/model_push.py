import sys
from hate.components.data_ingestion import GCCloud
from hate.constant import *
from hate.logger import logging
from hate.exception import CustomException
from hate.entity.config_entity import ModelPushConfig
from hate.entity.artifact_entity import ModelEvalArtifacts, ModelPushArtifacts
from hate.configuration.gccloud_syncer import GCCloud

class ModelPush:
    def __init__(model_push_config:ModelPushConfig):
        self.model_push_config = model_push_config
        self.gccloud = GCCloud()
    def initiate_model_push(self)->ModelPushArtifacts:
        logging.info("Entering the Model Push activity")
        try:
            self.gccloud.push_data_to_gcloud(self.model_push_config.BUCKET_NAME,self.model_push_config.MODEL_NAME,self.model_push_config.MODEL_TRAIN_ARTIFACTS_PATH)
            model_push_artifacts = ModelPushArtifacts(bucket_name=self.model_push_config.BUCKET_NAME)
            logging.info("Exiting the Model push activity")
            return model_push_artifacts
        except Exception as e:
            raise CustomException(e,sys) from e


