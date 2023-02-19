from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route(rule="/")
def home():
    return "Code with Al-Amin"

# Now I will create below url
# 1) localhost/user/student --> localhost/student (covert to it)
# 2) localhost/user/faculty --> localhost/faculty (covert to it)

@app.route(rule="/student")
def student():
    return "This is student page"

@app.route(rule="/faculty")
def faculty():
    return "This is faculty page"

@app.route(rule="/user/<name>")
def user(name):
    if name == "student":
        return redirect(location=url_for(endpoint="student"))
    elif name == "faculty":
        return redirect(location=url_for(endpoint="faculty"))


if __name__ == "__main__":
    app.run(debug=True)

# to run this file open terminal and run python app.py