import os,sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

from src.utils import *

@dataclass
class DataingestionConfig:
    raw_data_file_path=os.path.join('artifacts','raw.csv')
    
class Dataingestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()
    
    def initiate_dataingestion(self):
        try:
            logging.info('Dataingestion initiated')
            collection=MongoDB_con(url="mongodb+srv://sairam:sairam8662@cluster0.lyahcgb.mongodb.net/?retryWrites=true&w=majority",
                               database_name='Recommendation_system',collection_name='TMDB_Movies')
            #checking if the list is empty or not
            if collection.find()== 0:
                            logging.info("No data available")
                            exit()
            else:
                logging.info('Coverting MongoDB list to Pandas Dataframe')
                dataset_df=pd.DataFrame(list(collection.find()))
                dataset_df.to_csv(self.ingestion_config.raw_data_file_path,index=False,header=True)
                logging.info('Converted list to dataframe and available in path{file_path}'.format(' ',file_path=self.ingestion_config.raw_data_file_path))

            return dataset_df   
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    ingestion_obj=Dataingestion()
    raw_dataset=ingestion_obj.initiate_dataingestion()