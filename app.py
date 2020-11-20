from flask import Flask, render_template, request, redirect
from task_list.tasks.TaskList import TaskList
from task_list.users.User import User
from task_list.users.Admin import Admin
import babel

app = Flask(__name__)
app.debug = True

tasks = TaskList()
regularUser = User("Regular", "User", 1234)
adminUser = Admin("Admin", "User", 4246)

@app.template_filter('datetime')
def format_datetime(value, format='short'):
    if format == 'long':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel.dates.format_datetime(value, format)

@app.route("/tasklist")
def tasklist():

    return render_template('task_list.html', title="Task List", tasks=tasks)

@app.route("/addtask", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        #do something

        return redirect('/tasklist')

    return render_template('add_task.html')

app.run()