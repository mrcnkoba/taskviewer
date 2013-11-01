import datetime

__author__ = 'marcin'


class Event:
    def __init__(self, event_id=None, entity_id=None):
        self.event_id = event_id
        self.entity_id = entity_id
        self.fired_date = datetime.datetime.now()

