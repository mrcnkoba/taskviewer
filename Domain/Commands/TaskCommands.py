import datetime
from Domain.Repos.TaskRepository import TaskRepository
from Domain.Tasks.Task import Task
from Infrastructure.BaseCommandHandler import BaseCommandHandler

__author__ = 'marcin'


class CreateTaskCommand(object):
    def __init__(self):
        pass


class CreateTaskCommandHandler(BaseCommandHandler):
    def __init__(self):
        self.repo = TaskRepository()

    def handle(self, command):
        task = Task().create(creation_date=datetime.datetime.now())
        self.repo.insert(task)

    repo = None


