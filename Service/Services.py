from Domain.Commands.TaskCommands import CreateTaskCommand
from Domain.Commands.UserCommands import CreateUserCommand
from Domain.Queries.GetAllTasks import GetAllTasks
from Domain.Queries.UserQueries import GetAllUsers


class CommandBus(object):
    def invoke(self, command):
        command_name = command.__class__.__name__
        command_handler_name = command_name + "Handler"
        module = __import__(command.__module__, globals(), locals(), command_handler_name + "()")
        handler = getattr(module, command_handler_name)()
        handler.handle(command)


class QueryDispatcher(object):
    def query(self, query):
        return query.handle()


class TaskService(object):
    def __init__(self):
        self.command_bus = CommandBus()
        self.query_dispatcher = QueryDispatcher()

    def create_task(self, title, username):
        self.command_bus.invoke(CreateTaskCommand(title, username))

    def get_all_tasks(self):
        return self.query_dispatcher.query(GetAllTasks())


class UserService(object):
    def __init__(self):
        self.command_bus = CommandBus()
        self.query_dispatcher = QueryDispatcher()

    def create_user(self, username, password):
        self.command_bus.invoke(CreateUserCommand(username, password))

    def get_all_users(self):
        return self.query_dispatcher.query(GetAllUsers())

if __name__ == '__main__':
    t = TaskService()
    t.create_task('new', 'admin')
    tasks = t.get_all_tasks()
    for t in tasks:
        print t.id, t.title, t.status, t.username