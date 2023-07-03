import pymongo
import os,sys
from src.exception import CustomException
from src.logger import logging
import certifi


def MongoDB_con(url,database_name,collection_name):
    try:
        myclient=pymongo.MongoClient(url,tlsCAFile=certifi.where())
        global collection
        logging.info("mongoDB connection initiated")
        db=myclient[database_name]
        collection=db[collection_name]
        return collection
    except Exception as e:
        raise CustomException(e,sys)

