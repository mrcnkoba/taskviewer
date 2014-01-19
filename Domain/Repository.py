from abc import abstractmethod
from mongoengine import connect


#TODO: Insert parameters to config file!
class Repository(object):
    def __init__(self):
        connect('taskviewer')

    @abstractmethod
    def get_all(self):
        pass