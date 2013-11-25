from Domain.Repos.TaskRepository import TaskRepository
from Infrastructure.BaseCommandHandler import BaseCommandHandler

__author__ = 'marcin'



class CreateTaskCommand(object):
    def __init__(self, message):
        self.repo = TaskRepository()

class CreateTaskCommandHandler(BaseCommandHandler):
    def handle(self, command):
        
        self.repo.insert()

    def __init__(self):
        pass




