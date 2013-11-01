import unittest
import datetime
from Domain.Task.Task import Task
from Domain.Task.TaskStatus import TaskStatus


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.InitialStatus = TaskStatus.ToDo
        self.CreationDate = datetime.date(2000, 01, 01)
        self.ValidFrom = datetime.date(2001, 01, 01)
        self.ValidTo = datetime.date(2001, 06, 06)
        self.Deadline = datetime.date(2010, 01, 01)

    def testTaskShouldHaveInitialValues(self):
        #given

        #when
        task = Task(self.CreationDate, self.ValidFrom, self.ValidTo, self.Deadline)

        #then
        self.assertTrue(task.status == self.InitialStatus, "Status")
        self.assertTrue(task.creation_date == self.CreationDate, "Creation Date")
        self.assertTrue(task.valid_from == self.ValidFrom, "Valid From")
        self.assertTrue(task.valid_to == self.ValidTo, "Valid To")
        self.assertTrue(task.deadline == self.Deadline, "Deadline")

    def testTaskShouldHaveNoDeadline(self):

        #when
        task = self.getTask()

        #then
        self.assertTrue(task.status == self.InitialStatus, "Status")
        self.assertTrue(task.creation_date == self.CreationDate, "Creation Date")
        self.assertTrue(task.valid_from == self.ValidFrom, "Valid From")
        self.assertTrue(task.valid_to == self.ValidTo, "Valid To")
        self.assertTrue(task.deadline == None, "Deadline")

    def testTaskShouldBeClosed(self):
        # given
        task = Task(self.CreationDate, self.ValidFrom, self.ValidTo)

        # when
        task.complete()

        #then
        self.assertTrue(task.status == TaskStatus.Completed, "Status")

    def testTaskShouldBeReopened(self):
        # given
        task = self.getTask()
        task.complete()

        # when
        task.reopen()

        # then
        self.assertTrue(task.status == TaskStatus.ToDo, "Status")

    def testTaskShouldThrowExceptionWhenStartDateIsAfterEndDate(self):
        # given
        start_date = datetime.date(2010, 01, 01)
        end_date = datetime.date(2000, 01, 01)

        # when
        # then
        self.failUnlessRaises(ValueError, Task, self.CreationDate, start_date, end_date)


    def getTask(self):
        return Task(self.CreationDate, self.ValidFrom, self.ValidTo)

    CreationDate = None
    ValidTo = None


if __name__ == '__main__':
    unittest.main()
