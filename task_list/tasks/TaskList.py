from task_list.tasks.Task import Task
from task_list.Audit import Audit
from task_list.users.Admin import Admin


# define task list class
class TaskList:

    # define a private taskList that cannot be easily
    # manipulated at command-line level (not truly private)
    def __init__(self):
        self.taskList = []
        self.created = Audit()

    # add task to task list
    def addTask(self, task):
        # if task is not a Task, advise the user that they're
        # using the method wrong and return early
        if type(task) != Task:
            print("Incorrect usage of add task. Add from a User or Admin!")
            return
        # otherwise, add the task to the list
        self.taskList.append(task)

    # clear the task list - not really the intended means of
    # calling the method, but can be done this way
    def clearList(self, user, pin):
        # if the user isn't an admin, prevent them from clearing the list
        if type(user) != Admin or user.pin != pin:
            print("You can't clear the list!")
        else:
            # run clear method on taskList
            self.taskList.clear()

    # delete a specific task from the list - not
    # really the intended means of calling the method,
    # but can be done this way
    def deleteItem(self, user, pin, id):
        # prevent unauthorised users from deleting
        if type(user) != Admin or user.pin != pin:
            print("You can't delete items!")
        else:
            # if the list is empty, notify the user
            if len(self.taskList) == 0:
                print("No tasks to delete!")
            # otherwise if it's an invalid ID, tell them that too
            elif id < 1 or id > len(self.taskList):
                print("Enter a valid task ID")
            # otherwise delete the item they've
            # specified, adjusting for off-by-one
            else:
                del(self.taskList[id - 1])
                print("Task deleted")

    # mark task as completed
    def completeTask(self, id):

        self.taskList[id].completeTask()

    # returns task list as a string
    def __str__(self):
        taskListString = "Created: {0:%d/%m/%y %H:%M} Tasks: "\
            .format(self.created.timestamp)
        # if the list is empty, add a string explaining it's empty
        if (len(self.taskList)) == 0:
            return taskListString + "None"
        # otherwise, loop through and call the __str__ method on the tasks
        for task in self.taskList:
            taskListString = taskListString+"{"+str(task)+"},"
        return taskListString[:-1]

    # returns code used to instantiate object
    def __repr__(self):
        return "TaskList()"
