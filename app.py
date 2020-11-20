from flask import Flask, render_template
from task_list.tasks.TaskList import TaskList
from task_list.users.User import User
from task_list.users.Admin import Admin

app = Flask(__name__)
app.debug = True

tasks = TaskList()
regularUser = User("Regular", "User", 1234)
adminUser = Admin("Admin", "User", 4246)

@app.route("/tasklist")
def register():
    return render_template('task_list.html')

app.run()