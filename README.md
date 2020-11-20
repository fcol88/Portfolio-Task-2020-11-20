# Portfolio Task 2020-11-20 (Week 7)

Learning exercise for CETM65

## Task List V1.3

### Description

Learning exercise for CETM65

### Usage

Install requirements using:

` pip install -r requirements.txt `

Run the flask application using:

` python app.py `

Visit http://127.0.0.1:5000/ (or your similarly configured localhost address)

This works very much like the previous task list, but now with a front end!

From the home screen, you can:

- Add a task: click Add task
- Flip between views: click Show All to show all tasks, and Show Active to show active tasks
- Complete a task: click Mark as done

When you're on the add task page:

Enter:

- A description
- Which user is making the task (sorry, just a choice of two this time)
- Enter the pin (1234 for regular, 4246 for admin)
- Click Save task

Or click Cancel to go back to the home screen.

If there's an issue, the app will tell you what to do to fix it.