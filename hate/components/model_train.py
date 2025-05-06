from hate.constant import ARTIFACTS_DIR
from hate.entity.config_entity import ModelTrainConfig
from hate.entity.artifact_entity import DataTransformationArtifacts, ModelTrainArtifacts
from hate.ml.model import Model_Arch
from hate.logger import logging
from hate.exception import CustomException
from sklearn.model_selection import train_test_split
import pandas as pd
import os
import sys
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import pickle

class ModelTrain:
    def __init__(self, data_transformation_artifacts:DataTransformationArtifacts, model_train_config:ModelTrainConfig):
        self.data_transformation_artifacts = data_transformation_artifacts
        self.model_train_config = model_train_config
    def split_file(self):
        logging.info("Start processing of split file")
        raw_data = pd.read_csv(self.data_transformation_artifacts.transformed_file, index_col=False)
        x = raw_data['tweet']
        y = raw_data['class']

        train_x, test_x, train_y, test_y = train_test_split(x,y, test_size = self.model_train_config.TRAIN_TEST_SPLIT_RATIO,random_state = 42)
        os.makedirs(self.model_train_config.MODEL_TRAIN_PATH, exist_ok = True)
        train_x.to_csv(self.model_train_config.X_TRAIN_FILE_PATH)

        logging.info("End processing of split file")
        return train_x, train_y, test_x, test_y
    def tokenize_text(self, train_x, vocab_size, max_len):
        logging.info("Starting tokenizing the text")
        logging.info(train_x.iloc[0])
        try:
            tokenizer = Tokenizer(num_words = vocab_size)
            tokenizer.fit_on_texts(train_x.astype(str))
            sequences = tokenizer.texts_to_sequences(train_x.astype(str))
            logging.info(f"converting text to sequences: {sequences}")
            sequences_matrix = pad_sequences(sequences,maxlen=max_len)
            logging.info(f" The sequence matrix is: {sequences_matrix}")
            return sequences_matrix,tokenizer
        except Exception as e:
            raise CustomException(e, sys) from e
    def start_model_train(self):
        logging.info("Starting Model Training step")
        train_x, train_y, test_x, test_y = self.split_file()
        logging.info("Initialize the model")
        model_arch = Model_Arch()
        model = model_arch.getmodel()
        logging.info("Tokenize and pad sequence the text to max length")
        seq_train, tokenizer = self.tokenize_text(train_x,model_arch.model_config.VOCAB_SIZE, model_arch.model_config.MAX_SEQ_LENGTH)

        logging.info("Start the Model Training")
        model.fit(seq_train, train_y,
                        batch_size=self.model_train_config.BATCH_SIZE, 
                        epochs = self.model_train_config.NUMBER_OF_EPOCHS, 
                        validation_split=self.model_train_config.VALIDATION_SPLIT)
        logging.info("saved the Model")
        with open('tokenizer.pickle', 'wb') as handle:
                pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        model.save(self.model_train_config.MODEL_TRAIN_ARTIFACTS_PATH)
        logging.info("save the test files")
        test_x.to_csv(self.model_train_config.X_TEST_FILE_PATH)
        test_y.to_csv(self.model_train_config.Y_TEST_FILE_PATH)

        logging.info("Create the Model Artifacts object")
        model_train_artifacts = ModelTrainArtifacts(trained_model_path =self.model_train_config.MODEL_TRAIN_ARTIFACTS_PATH,
                                                   x_test_path =self.model_train_config.X_TEST_FILE_PATH,
                                                  y_test_path = self.model_train_config.Y_TEST_FILE_PATH)
        return model_train_artifacts




