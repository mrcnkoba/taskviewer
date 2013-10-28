__author__ = 'marcin'


class Task(object):
    def __init__(self, status, creationDate, validTo):
        self.Status = status
        self.CreationDate = creationDate
        self.ValidTo = validTo

    Status = None
    CreationDate = None
    ValidTo = None