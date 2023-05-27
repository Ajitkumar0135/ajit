from flask import Flask,render_template, request, redirect , url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'users'
# app.config['SECRET_KEY'] = 'Ajit_kumar_315'

mysql = MySQL(app)

# Route: /hello
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# Route: /users
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

# Route: /new_user
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        mysql.connection.commit()
        cur.close()
        return redirect('/new_user') 
    return render_template('new_user.html')

# Route: /users/<id>
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        id = request.form['id']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cur.fetchall()
        cur.close()
        if user:
            return render_template('user.html', user=user)
        # else:
        #     return "User not found", 404
    return render_template('user.html')


# Error handling
@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404

if __name__ == "__main__":
    app.run(debug=True)
