from flask import Flask, render_template, request

app = Flask(__name__)

@app.route(rule='/')
def home():
    return render_template(template_name_or_list="form.html")

@app.route(rule='/loginform', methods=['POST'])
def loginform():
    name = ""
    password = ""

    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')

    if name == "alamin" and password == "123":
        return "Login successful"
    else:
        return "Login failed"

# @app.route(rule='/loginform', methods=['GET'])
# def loginform():
#     name = ""
#     password = ""
#
#     if request.method == "GET":
#         name = request.args.get('name')
#         password = request.args.get('password')
#
#     if name == "alamin" and password == "123":
#         return "Login successful"
#     else:
#         return "Login failed"


if __name__ == '__main__':
    app.run(debug=True)