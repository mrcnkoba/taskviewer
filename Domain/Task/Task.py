from Domain.Entity import Entity
from Domain.Event import Event
from Domain.Task.TaskStatus import TaskStatus

__author__ = 'marcin'


class Task(Entity):
    status = None
    creation_date = None
    valid_to = None
    deadline = None
    valid_from = None

    def __init__(self, creation_date, valid_from, valid_to, deadline=None):
        if valid_from > valid_to:
            raise ValueError()
        self.apply(Created(TaskStatus.ToDo, creation_date, valid_from, valid_to, deadline))

    def on_created(self, event):
        self.status = event.status
        self.creation_date = event.creation_date
        self.valid_from = event.valid_from
        self.valid_to = event.valid_to
        self.deadline = event.deadline

    def complete(self):
        self.apply(Completed())

    def on_completed(self, event):
        self.status = TaskStatus.Completed

    def reopen(self):
        self.apply(Reopened())

    def on_reopened(self, event):
        self.status = TaskStatus.ToDo

# Events

class Completed(Event):
    pass


class Created(Event):
    def __init__(self, status, creation_date, valid_from, valid_to, deadline=None):
        self.status = status
        self.creation_date = creation_date
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.deadline = deadline


class Reopened(Event):
    pass


