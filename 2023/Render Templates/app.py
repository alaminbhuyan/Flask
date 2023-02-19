from flask import Flask, render_template


app = Flask(__name__)


@app.route(rule="/")
def home():
    return render_template(template_name_or_list="index.html")



if __name__ == "__main__":
    app.run(debug=True)

# to run this file open terminal and run python app.py