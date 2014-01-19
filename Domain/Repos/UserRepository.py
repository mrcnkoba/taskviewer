from Domain.Repository import Repository
from Domain.Users import User


class UserRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def insert(self, user):
        user.save()

    def get_all(self):
        return User.objects

    def get_by_name(self, name):
        return User.objects(username=name).first()