from mongoengine import StringField
from Domain.Entity import Entity


class User(Entity):
    username = StringField(required=True)
    password = StringField(required=True)


    def create(self, username, password):
        self.username = username
        self.password = password
        return self

