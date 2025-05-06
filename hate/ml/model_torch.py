import torch.nn as nn
from hate.constant import *

class LSTMModel(nn.Module):
    def __init__(self,input_size,embedding_size,hidden_size,num_of_layers):
        super(LSTMModel, self).__init__()
        embedding = nn.Embedding(input_size, embedding_size)
        lstm = nn.LSTM(embedding_size,hidden_size,num_of_layers)
