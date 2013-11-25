from Domain.Repository import Repository

__author__ = 'marcin'


class TaskRepository(Repository):
    def __init__(self):
        self.tasks = self.db.tasks

    def insert(self, task):
        self.tasks.insert(task)
