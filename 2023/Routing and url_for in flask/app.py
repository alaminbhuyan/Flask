from flask import Flask


app = Flask(__name__)


@app.route(rule="/")
def home():
    return "This is the home page"


@app.route(rule="/name")
def myname():
    return "Your name is Alamin"

# let's create variable in url pattern
@app.route(rule="/<string:name>")
def myname2(name):
    return f"Your name is {name}"

@app.route(rule="/name/<name>")
def myname3(name):
    return f"Your name is {name}"

@app.route(rule="/birthday/<int:date>")
# @app.route(rule="/birthday/<float:date>")
def birthday(date):
    return f"Your birthday is {date}"

if __name__ == "__main__":
    app.run(debug=True)

# to run this file open terminal and run python app.py