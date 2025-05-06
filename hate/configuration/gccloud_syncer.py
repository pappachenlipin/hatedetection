import os
from hate.exception import CustomException
from hate.logger import logging

class GCCloud:
    def get_data_from_gccloud(self,bucket_name, file_name, file_path):
        command = f"gsutil cp gs://{bucket_name}/{file_name} {file_path}/{file_name}"
        logging.info("Run the command to invoke GC Cloud")
        try:
            os.system(command)
        except Exception as e:
            raise CustomException(e,sys) from e
    def push_data_to_gcloud(bucket_name,file_name,file_path):

        command = f"gsutil cp {file_path}/{file_name} gs://{bucket_name}"
        logging.info("Run the command to push the file to GC Cloud")
        try:
            os.system(command)
        except Exception as e:
            raise CustomException(e,sys) from e


