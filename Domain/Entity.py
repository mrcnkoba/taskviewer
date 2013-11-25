from abc import abstractmethod

__author__ = 'marcin'


class Entity():
    @abstractmethod
    def apply(self, event):
        method_name = str(event.__class__).split(".")[-1].lower()
        method = getattr(self, "on_" + method_name)
        self.store_event(event)
        method(event)

    def store_event(self, event):
        self.events.append(event)

    events = []



