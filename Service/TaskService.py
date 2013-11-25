from Domain.Commands.TaskCommands import CreateTaskCommand

__author__ = 'marcin'

class CommandBus(object):
    def invoke(self, command):
        command_name = command.__class__.__name__
        command_handler_name = command_name + "Handler"
        module = __import__(command.__module__, globals(), locals(), command_handler_name+"()")
        handler = getattr(module, command_handler_name)
        method = getattr(handler(), "handle")
        method(command)


class TaskService(object):
    def __init__(self):
        self.command_bus = CommandBus()
        
    def create_task(self):
        self.command_bus.invoke(CreateTaskCommand())


if __name__ == '__main__':
    c = CommandBus()
    c.invoke(CreateTaskCommand("mess"))
