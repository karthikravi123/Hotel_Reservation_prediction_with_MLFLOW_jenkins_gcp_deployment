import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml


logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.filename = self.config["bucket_file_name"]
        self.train_test_ratio =self.config["train_ratio"]

        os.makedirs(RAW_DIR,exist_ok=True)
        logger.info(f"Data INgestion started with {self.bucket_name} and file is {self.filename}")

    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            print("\n------------------------")
            print("DEBUG → Listing files in bucket:", self.bucket_name)
            print("------------------------")

            all_files = list(bucket.list_blobs())
            if not all_files:
                print("❌ No files found in bucket!")
            else:
                for b in all_files:
                    print("📂", b.name)

            print("------------------------")
            print("DEBUG → Trying to download:", self.filename)
            print("------------------------\n")

            blob = bucket.blob(self.filename)

            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"CSV file successfully downloaded to {RAW_FILE_PATH}") 
        except Exception as e:
            logger.error("Error while downloading the CSV file")
            raise CustomException("Error while downloading the CSV file", e)

    def split_data(self):
        try:
                logger.info("started splitting data")
                data = pd.read_csv(RAW_FILE_PATH)

                train_data,test_data = train_test_split(data,test_size=1-self.train_test_ratio,random_state=42)
                train_data.to_csv(TRAIN_FILE_PATH,index=False)
                test_data.to_csv(TEST_FILE_PATH,index=False)
                logger.info(f"train data saved to  {TRAIN_FILE_PATH}")
                logger.info(f"test data saved to  {TEST_FILE_PATH}")

        except Exception as e:
                logger.error("Error while splitting data")
                raise CustomException("Failed while splitting data",e)
            
    def run(self):
        try:
              logger.info("starting data ingestion")
              self.download_csv_from_gcp()
              self.split_data()

              logger.info("Data Ingestion completed succesfully")
        except Exception as e:
              logger.error(f"Cusotm exception: {str(e)}")

        finally:
              logger.info("Data ingestion completed")

if __name__ == "__main__":
      dataingestion = DataIngestion(read_yaml(CONFIG_PATH))
      dataingestion.run()
                
    