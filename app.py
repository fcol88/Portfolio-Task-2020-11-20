from flask import Flask, render_template, request, redirect
from task_list.tasks.TaskList import TaskList
from task_list.users.User import User
from task_list.users.Admin import Admin

app = Flask(__name__)
app.debug = True

tasks = TaskList()
regularUser = User("Regular", "User", 1234)
adminUser = Admin("Admin", "User", 4246)

@app.route("/tasklist")
@app.route("/")
def task_list():

    showAll = False

    if not request.args.get("showAll") == None:
        showAll = True

    return render_template('task_list.html', title="Task List", tasks=tasks, showAll = showAll)

@app.route("/addtask", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        req = request.form

        feedback = validate_task(req)

        if len(feedback) != 0:

            return render_template('add_task.html', title="Save task",\
                description=req["description"], feedback=feedback)

        addTaskToList(tasks, req)

        return redirect('/tasklist')

    return render_template('add_task.html', title="Add task")

@app.route("/completetask")
def complete_task():

    id = int(request.args.get('id'))

    if not id > len(tasks.taskList) - 1:
        tasks.completeTask(id)
    
    return redirect('/tasklist')

def validate_task(req):

    feedback = list()

    print(req)

    if req["description"] == "":
        feedback.append("Enter a description")

    if not "user" in req:
        feedback.append("Pick a user")
        return feedback

    if req["user"] == "":
        feedback.append("Choose a user and enter the corresponding PIN")
    elif req["user"] == "std" or req["user"] == "adm":
        if (req["user"] == "std" and req["pin"] != str(regularUser.pin)) or\
           (req["user"] == "adm" and req["pin"] != str(adminUser.pin)):
           feedback.append("PIN is incorrect")
    else:
        feedback.append("Stop mucking about with the DOM")

    return feedback

def addTaskToList(tasks, req):

    if req["user"] == "std":
        regularUser.addTask(tasks, req["description"], req["pin"])
    else:
        adminUser.addTask(tasks, req["description"], req["pin"])


app.run()