from abc import abstractmethod
from mongoengine import Document, ListField


class Entity(Document):
    def apply(self, event):
        method_name = str(event.__class__).split(".")[-1].lower()
        method = getattr(self, "on_" + method_name)
    #    self.store_event(event)
        method(event)

    meta = {'allow_inheritance': True }

    #def store_event(self, event):
    #    self.events.append(event)

    #events = ListField()



