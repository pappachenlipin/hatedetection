import os
from hate.pipeline.train_pipeline import Train_pipeline


#Create a train pipeline instance

train_line = Train_pipeline()

train_line.run_pipeline()
print("Completed")