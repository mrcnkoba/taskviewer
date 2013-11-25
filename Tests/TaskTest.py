import unittest
import datetime
from Domain.Task.Task import Task, InvalidStateError
from Domain.Task.TaskStatus import TaskStatus


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.InitialStatus = TaskStatus.Draft
        self.CreationDate = datetime.date(2000, 01, 01)
        self.ValidFrom = datetime.date(2001, 01, 01)
        self.ValidTo = datetime.date(2001, 06, 06)
        self.Deadline = datetime.date(2010, 01, 01)

    def testTaskShouldHaveInitialValues(self):
        #given

        #when
        task = self.getTask()

        #then
        self.assertTrue(task.status == self.InitialStatus, "Status")
        self.assertTrue(task.creation_date == self.CreationDate, "Creation Date")
        self.assertTrue(task.start_date is None, "Valid From")
        self.assertTrue(task.end_date is None, "Valid To")
        self.assertTrue(task.deadline is None, "Deadline")

    def testTaskShouldHaveNoDeadline(self):
        #when
        task = self.getTask()

        #then
        self.assertTrue(task.status == self.InitialStatus, "Status")
        self.assertTrue(task.creation_date == self.CreationDate, "Creation Date")
        self.assertTrue(task.deadline is None, "Deadline")

    def testTaskShouldBeAssignedToDates(self):
        #given
        task = self.getTask()

        #when
        task.assign_to_dates(self.ValidFrom, self.ValidTo)

        #then
        self.assertTrue(task.start_date == self.ValidFrom, "start date")
        self.assertTrue(task.end_date == self.ValidTo, "end date")

    def testTaskStartDateShouldNotBeAfterEndDate(self):
        #given
        task = self.getTask()

        #when
        #then
        self.assertRaises(ValueError, task.assign_to_dates, datetime.date(2000, 01, 01), datetime.date(1999, 01, 01))

    def testTaskShouldBeClosed(self):
        # given
        task = Task(self.CreationDate)
        task.assign_to_dates(self.ValidFrom, self.ValidTo)

        # when
        task.complete()

        #then
        self.assertTrue(task.status == TaskStatus.Completed, "Status")

    def testTaskShouldBeReopened(self):
        # given
        task = self.getTask()
        task.assign_to_dates(self.ValidFrom, self.ValidTo)
        task.complete()

        # when
        task.reopen()

        # then
        self.assertTrue(task.status == TaskStatus.ToDo, "Status")

    def testTaskCannotBeCompletedBeforeAssignment(self):
        # given
        task = self.getTask()

        # when
        # then
        self.assertRaises(InvalidStateError, task.complete)

    def getTask(self):
        return Task(self.CreationDate)

    CreationDate = None
    ValidTo = None


if __name__ == '__main__':
    unittest.main()
