from Domain.Repository import Repository
from Domain.Tasks.Task import Task


class TaskRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def insert(self, task):
        task.save()

    def get_all(self):
        return Task.objects