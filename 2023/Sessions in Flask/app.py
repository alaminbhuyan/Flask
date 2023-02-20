from flask import Flask,render_template,request,flash,session,redirect,url_for


app = Flask(__name__)

app.secret_key = "abc"


@app.route(rule="/")
def home():
    return render_template(template_name_or_list="forms.html")


@app.route(rule="/loginform", methods=["POST"])
def logIn():
    if request.method == 'POST':
        error = None
        uname = request.form.get("name")
        password = request.form.get("password")

        if uname == "alamin" and password == "123":
            session['name'] = uname
            flash("Successfully logged in")
            return render_template(template_name_or_list="profile.html", uname=uname)
        
        else:
            error = "Please enter a valid username and password"
            return render_template(template_name_or_list="forms.html", error=error)


@app.route(rule="/logout")
def userlogOut():
    session.pop('name', None)
    return redirect(location=url_for(endpoint="home"))



if __name__ == "__main__":
    app.run(debug=True)
