import pickle
import sys
from hate.entity.config_entity import ModelEvalConfig
from hate.constant import *
from hate.entity.artifact_entity import ModelTrainArtifacts, ModelEvalArtifacts, DataTransformationArtifacts
from hate.exception import CustomException
from hate.logger import logging
import pandas as pd
import numpy as np
from hate.configuration.gccloud_syncer import GCCloud
from keras.utils import pad_sequences
import pickle
import keras

class ModelEvaluation:
    def __init__(self,model_train_artifacts:ModelTrainArtifacts,model_eval_config:ModelEvalConfig):
        self.model_train_artifacts = model_train_artifacts
        self.model_eval_config = model_eval_config
        #self.data_transformation_artifacts = data_transformation_artifacts
        self.gccloud = GCCloud()
    def get_model_from_gcloud(self):
        logging.info("Entering Get Model from gcloud utility")

        try:
            os.makedirs(self.model_eval_config.MODEL_EVAL_ARTIFACTS_PATH,exist_ok=True)
            best_model = self.gccloud.get_data_from_gccloud(self.model_eval_config.BUCKET_NAME,self.model_eval_config.MODEL_NAME,self.model_eval_config.BEST_MODEL_DIR)
            best_model_path = os.path.join(self.model_eval_config.BEST_MODEL_DIR,self.model_eval_config.MODEL_NAME)
            return best_model_path
        except Exception as e:
            raise CustomException(e, sys) from e


    def evaluate(self, model):
        logging.info("Start execution of evaluate method")
        logging.info("Read the test input file")
        test_x = pd.read_csv(self.model_train_artifacts.x_test_path,index_col=0)
        logging.info("read the test target file")
        test_y = pd.read_csv(self.model_train_artifacts.y_test_path,index_col =0)

        #load the model
        model = keras.models.load_model(model)
        #load the tokenizer
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

       
        x_test = test_x['tweet'].astype(str)
        x_test = x_test.squeeze()
        print(f"-----------------{test_y.shape}--------------")
        test_y = test_y.squeeze()
        
        sequences = tokenizer.texts_to_sequences(x_test)
        test_sequences = pad_sequences(sequences,maxlen=MAX_SEQ_LENGTH)

        #calculate the accuracy
        logging.info("Evalue the accuracy")
        print(f"----------{test_sequences}------------------")

        print(f"-----------------{x_test.shape}--------------")
        print(f"-----------------{test_y.shape}--------------")
        accuracy = model.evaluate(test_sequences,test_y)
        return accuracy
    def start_model_evaluation(self)->ModelEvalArtifacts:
        logging.info("Start Model Evaluation")
         #load the model
        logging.info("Load the Current Model from train path")
       
        logging.info("Evaluate the accuracy for the specified model")
        model_accuracy = self.evaluate(self.model_train_artifacts.trained_model_path)
        logging.info(f"Accuracy is {model_accuracy}")
        # check if a model exists in gc clod

        is_best_model = False

        current_best_gcp_model = self.get_model_from_gcloud()
        if os.path.isfile(current_best_gcp_model):
            best_gc_model_accuracy = self.evaluate(current_best_gcp_model)
            if best_gc_model_accuracy < current_best_gcp_model:
                is_best_model = True
        else:
            is_best_model = True
        model_eval_artifacts = ModelEvalArtifacts(is_model_accepted = is_best_model)
        return model_eval_artifacts
        
















