from Domain.Repos.TaskRepository import TaskRepository

__author__ = 'marcin'


class GetAllTasks(object):
    def __init__(self):
        self.task_repo = TaskRepository()

    def handle(self):
        return self.task_repo.get_all()
