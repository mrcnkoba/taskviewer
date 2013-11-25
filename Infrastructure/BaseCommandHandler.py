from abc import abstractmethod

__author__ = 'marcin'

class BaseCommandHandler(object):
    @abstractmethod
    def handle(self, command):
        pass



