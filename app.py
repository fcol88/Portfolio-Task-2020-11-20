from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/register")
def register():
    return render_template('register.html')

app.run()