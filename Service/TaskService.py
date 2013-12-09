from Domain.Commands.TaskCommands import CreateTaskCommand
from Domain.Queries.GetAllTasks import GetAllTasks

__author__ = 'marcin'

class CommandBus(object):
    def invoke(self, command ):
        command_name = command.__class__.__name__
        command_handler_name = command_name + "Handler"
        module = __import__(command.__module__, globals(), locals(), command_handler_name+"()")
        handler = getattr(module, command_handler_name)()
        handler.handle(command)

class QueryDispatcher(object):
    def query(self, query):
        return query.handle()

class TaskService(object):
    def __init__(self):
        self.command_bus = CommandBus()
        self.query_dispatcher = QueryDispatcher()
        
    def create_task(self):
        self.command_bus.invoke(CreateTaskCommand())

    def get_all_tasks(self):
        return self.query_dispatcher.query(GetAllTasks())

if __name__ == '__main__':
    t = TaskService()
    t.create_task()
    tasks = t.get_all_tasks()
    for t in tasks:
        print t