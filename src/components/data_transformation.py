import pandas as pd
import os,sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import *

@dataclass
class DataTransformationConfig:
    movies_list_file_path=os.path.join('artifacts','movies_list.pkl')

class DataTranformation:
    def __init__(self):
        self.transformation_config=DataTransformationConfig()

    def initiate_data_transformation(self,dataset):
        try:
            logging.info('Data transformation initiated')

            logging.info('Removing Unnecessary columns from dataset')
            dataset=dataset.drop(['_id','original_language','release_date','vote_average','vote_count','popularity'],axis=1)
            
            logging.info('adding "Tags" column for further analysis')
            dataset['tags']=dataset['genre']+dataset['overview']

            logging.info('Dropping "genere","overview" columns form dataset')
            movies=dataset.drop(['genre','overview'], axis=1)
            
            logging.info('Saving movies list to pickle file and available in path {file_path_name}'.format(' ',file_path_name=self.transformation_config.movies_list_file_path))
            save_obj(file_path=self.transformation_config.movies_list_file_path,
                     obj=movies)
            
            return movies
        except Exception as e:
            raise CustomException(e,sys)
