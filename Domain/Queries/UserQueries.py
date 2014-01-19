from Domain.Repos.UserRepository import UserRepository
from Service.dtos import UserDto


def repack(user):
    return UserDto(username=user.username)


class GetAllUsers(object):
    def __init__(self):
        self.repo = UserRepository()

    def handle(self):
        users = self.repo.get_all()
        dtos = [repack(user) for user in users]
        return dtos