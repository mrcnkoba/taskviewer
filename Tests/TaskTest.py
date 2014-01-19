import unittest
import datetime
from Domain.Tasks.Task import Task, InvalidStateError
from Domain.Tasks.TaskStatus import TaskStatus
from Domain.Users import User


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
        task = self.getTask('new')

        #then
        self.assertTrue(task.status == self.InitialStatus, "Status")
        self.assertTrue(task.creation_date == self.CreationDate, "Creation Date")
        self.assertTrue(task.title, 'new')

    def testTaskShouldHaveNoDeadline(self):
        #when
        task = self.getTask('new')

        #then
        self.assertTrue(task.status == self.InitialStatus, "Status")
        self.assertTrue(task.creation_date == self.CreationDate, "Creation Date")
        self.assertTrue(task.deadline is None, "Deadline")


    def testTaskShouldBeClosed(self):
        # given
        task = self.getTask('new')

        # when
        task.complete()

        #then
        self.assertTrue(task.status == TaskStatus.Completed, "Status")

    def testTaskShouldBeReopened(self):
        # given
        task = self.getTask('new')
        task.complete()

        # when
        task.reopen()

        # then
        self.assertTrue(task.status == TaskStatus.ToDo, "Status")

    def taskCannotBeCompletedTwice(self):
        # given
        task = self.getTask('new')

        # when
        task.complete()
        # then
        self.assertRaises(InvalidStateError, task.complete)

    def getTask(self, title):
        user = self.getUser('admin')
        return Task().create(self.CreationDate, title, user)

    def getUser(self, name):
        return User().create(name, '')

    CreationDate = None
    ValidTo = None


if __name__ == '__main__':
    unittest.main()
