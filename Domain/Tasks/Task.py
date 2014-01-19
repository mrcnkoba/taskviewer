import datetime
from mongoengine import StringField, DateTimeField, ReferenceField
from Domain.Entity import Entity
from Domain.Event import Event
from Domain.Tasks.TaskStatus import TaskStatus, TaskState
from Domain.Users import User


class Task(Entity):
    status = StringField(required=True)
    creation_date = DateTimeField(default=datetime.datetime.now)
    deadline = DateTimeField()
    title = StringField(required=True)
    state = StringField(required=True)
    user = ReferenceField(User)

    def create(self, creation_date, title, user):
        self.apply(Created(creation_date, title, user))
        return self

    def on_created(self, event):
        self.status = TaskStatus.ToDo
        self.creation_date = event.creation_date
        self.title = event.title
        self.state = TaskState.Active
        self.user = event.user

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

    def remove(self):
        self.apply(Removed)

    def on_removed(self):
        self.state = TaskState.Removed

# Events

class Created(Event):
    def __init__(self, creation_date, title, user):
        self.creation_date = creation_date
        self.title = title
        self.user = user


class Reopened(Event):
    pass


class Completed(Event):
    pass


class Removed(Event):
    pass


# Errors

class InvalidStateError():
    def __init__(self):
        pass