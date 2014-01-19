from Domain.Repos.UserRepository import UserRepository
from Domain.Users import User


class CreateUserCommand(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class CreateUserCommandHandler(object):
    def __init__(self):
        self.user_repo = UserRepository()

    def handle(self, command):
        user = User().create(command.username, command.password)
        users = self.user_repo.get_all()
        self.user_repo.insert(user)