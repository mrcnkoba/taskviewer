from pymongo import MongoClient

__author__ = 'marcin'

#TODO: Insert parameters to config file!
class Repository(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.taskviewer_database
