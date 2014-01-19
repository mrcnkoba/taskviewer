import datetime
from Domain.Repos.TaskRepository import TaskRepository
from Domain.Repos.UserRepository import UserRepository
from Domain.Tasks.Task import Task
from Infrastructure.BaseCommandHandler import BaseCommandHandler


class CreateTaskCommand(object):
    def __init__(self, title, username):
        self.title = title
        self.username = username


class CreateTaskCommandHandler(BaseCommandHandler):
    def __init__(self):
        self.taskRepo = TaskRepository()
        self.userRepo = UserRepository()

    def handle(self, command):
        user = self.userRepo.get_by_name(command.username)
        task = Task().create(datetime.datetime.now(), command.title, user)
        self.taskRepo.insert(task)

    taskRepo = None


