__author__ = 'marcin'

class DTO(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class TaskDto(DTO):
    pass

class UserDto(DTO):
    pass