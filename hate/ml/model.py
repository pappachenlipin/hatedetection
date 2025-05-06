from hate.constant import *
from keras.layers import LSTM, Activation,Dense, Dropout,Input, Embedding, SpatialDropout1D
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
from hate.entity.config_entity import ModelConfig

class Model_Arch:
    def __init__(self):
        self.model_config = ModelConfig()
    def getmodel(self):
        model = Sequential()
        model.add(Embedding(self.model_config.VOCAB_SIZE, self.model_config.EMBEDDING_SIZE, input_length = self.model_config.MAX_SEQ_LENGTH))
        model.add(SpatialDropout1D(self.model_config.DROP_OUT))
        model.add(LSTM(self.model_config.EMBEDDING_SIZE, dropout = self.model_config.DROP_OUT, recurrent_dropout = self.model_config.DROP_OUT))
        model.add(Dense(self.model_config.OUTPUT_SIZE,activation = self.model_config.ACTIVATION))
        model.summary()
        model.compile(loss = self.model_config.LOSS, optimizer = RMSprop(), metrics = self.model_config.METRICS)
        return model


