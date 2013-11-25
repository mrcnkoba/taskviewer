from abc import abstractmethod

__author__ = 'marcin'

def wrapper(func):
    def use_decorator(_self, command):
        print 'hehe'
        func(_self, command)

    return use_decorator


class BaseCommandHandler(object):
    @abstractmethod
    @wrapper
    def handle(self, command):
        pass



