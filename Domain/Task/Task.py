from Domain.Entity import Entity
from Domain.Event import Event
from Domain.Task.TaskStatus import TaskStatus

__author__ = 'marcin'


class Task(Entity):
    status = None
    creation_date = None
    start_date = None
    end_date = None
    deadline = None


    def __init__(self, creation_date):
        self.apply(Created(creation_date))

    def on_created(self, event):
        self.status = TaskStatus.Draft
        self.creation_date = event.creation_date

    def complete(self):
        if self.status != TaskStatus.ToDo:
            raise InvalidStateError

        self.apply(Completed())

    def on_completed(self, event):
        self.status = TaskStatus.Completed

    def reopen(self):
        self.apply(Reopened())

    def on_reopened(self, event):
        self.status = TaskStatus.ToDo

    def assign_to_dates(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError
        self.apply(Assigned(start_date, end_date))

    def on_assigned(self, event):
        self.start_date = event.start_date
        self.end_date = event.end_date
        self.status = TaskStatus.ToDo

# Events

class Created(Event):
    def __init__(self, creation_date):
        self.creation_date = creation_date


class Reopened(Event):
    pass


class Completed(Event):
    pass


class Assigned(Event):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

# Errors

class InvalidStateError():
    def __init__(self):
        pass