from Domain.Repos.TaskRepository import TaskRepository
from Service.dtos import TaskDto

__author__ = 'marcin'


class GetAllTasks(object):
    def __init__(self):
        self.task_repo = TaskRepository()

    def handle(self):
        tasks = self.task_repo.get_all()
        repacked = []
        for task in tasks:
            repacked.append(TaskDto(id=task.id, title=task.title, status=task.status, username=task.user.username))
        return repacked