from flask import Flask, url_for, redirect, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Connecting a Flask Application to a MySQL Database

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todoapp'

# Configuring the MySQL Connection Cursor
mysql = MySQL(app=app)

# Creating a connection cursor
# mycursor = mysql.connection.cursor()


@app.route(rule="/", methods=['GET', 'POST'])
def home():
    # Creating a connection cursor
    mycursor = mysql.connection.cursor()

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        print(title, desc)
        mycursor.execute(" INSERT INTO mytodo(title, description) VALUES(%s,%s) ", (title, desc))

        mysql.connection.commit()
        # mycursor.close()
    
    mycursor.execute(" SELECT * FROM mytodo ")
    allTodo = list(mycursor.fetchall())
    print(allTodo)
        
    # return render_template(template_name_or_list='index.html', context={'allTodo' : allTodo})
    return render_template(template_name_or_list='index.html', allTodo = allTodo)


@app.route(rule="/about")
def about():
    return render_template(template_name_or_list='about.html')


if __name__ == "__main__":
    app.run(debug=True)
