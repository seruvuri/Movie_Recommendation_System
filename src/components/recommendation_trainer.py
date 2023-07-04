import os,sys
from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils import *

@dataclass
class RecommendationTrainerconfig:
    similarity_obj_file_path=os.path.join('artifacts','similarity.pkl')

class RecommendationTrainer:
    def __init__(self):
        self.Recommendation_config=RecommendationTrainerconfig()

    def initiate_recommendation_trainer(self,movies_df):
        try:
            logging.info('Recommendation training initiated')

            logging.info('using to CounterVectorizer to analyzing text in "tags" column and converting into vector matrix')
            ## using counter vectorizer for analyzing the text in tags column and converting into vector matrix
            cv=CountVectorizer(max_features=10000,stop_words='english')
            vector=cv.fit_transform(movies_df['tags'].values.astype('U')).toarray()
            
            #getting similar values form tags using cosine_similarity
            logging.info('using Cosine similarity from sklearn for finding similarity between indexs')
            similarity=cosine_similarity(vector)
            
            logging.info('saving similarity object to pickle file and available in path {file_path_name}'.format(' ',file_path_name=self.Recommendation_config.similarity_obj_file_path))
            save_obj(file_path=self.Recommendation_config.similarity_obj_file_path,
                     obj=similarity)
            
            return similarity
        except Exception as e:
            raise CustomException(e,sys)

