from flask import Flask, request, render_template


app = Flask(__name__)


@app.route(rule="/")
def home():
    return render_template("index.html")

# we can use one of them following way

# @app.route(rule="/registrationForm", methods=["POST"])
# def registrationForm():
#     if request.method == "POST":
#         info = request.form

#     return render_template("registration.html", info=info)

@app.route(rule="/registrationForm", methods=["POST"])
def registrationForm():
    if request.method == "POST":
        userName = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        phone = request.form.get("phone")
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
    
    info = {
        "username": userName,
        "password": password,
        "email": email,
        "phone": phone,
        "birthday": birthday,
        "gender": gender
    }

    return render_template("registration.html", info=info)



if __name__ == "__main__":
    app.run(debug=True)
