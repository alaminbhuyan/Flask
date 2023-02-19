from flask import Flask, render_template, request

app = Flask(__name__)

# {{ }} --> variables, expressions
# {% %} --> statements like for, if
# {# #} --> to comments a variable

@app.route(rule='/')
def home():
    info = {
        "name": "Alamin",
        "age": 23,
        "gender": "male",
        "location": "Uttara, Dhaka-1230"
    }
    return render_template(template_name_or_list="message.html", information=info)

@app.route(rule='/<name>')
def yourname(name):
    return render_template(template_name_or_list="index.html", name=name)



if __name__ == '__main__':
    app.run(debug=True)