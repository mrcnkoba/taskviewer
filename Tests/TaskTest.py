import unittest
import datetime
from Domain.Task import Task


class TaskStatus(object):
    ToDo = 1


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.InitialStatus = TaskStatus.ToDo
        self.CreationDate = datetime.date(2000,01,01)
        self.ValidTo = datetime.date(2001,06,06)

    def testTaskShouldHaveInitialValues(self):
        task = Task(self.InitialStatus, self.CreationDate, self.ValidTo)
        self.assertTrue(task.Status == self.InitialStatus, "Status")
        self.assertTrue(task.CreationDate == self.CreationDate, "Creation Date")
        self.assertTrue(task.ValidTo == self.ValidTo, "Valid To")

    InitialStatus = None
    CreationDate = None
    ValidTo = None



if __name__ == '__main__':
    unittest.main()
