from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
from mysqlconnection import connectToMySQL
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
SCHEMA = "email"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
        
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM email_table WHERE email=%(email)s;"
    data={
        'email': request.form['email']
    }
    
    new_query = db.query_db(query,data)
    print('*' * 50)
    print(new_query)
    print('*' * 50)
    if len(new_query)>0:
        flash("Email exists")
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO email_table(email,created_at) VALUES (%(email)s,now());"
    data = { 
        'email': request.form['email']
    }
    new_email = db.query_db(query,data)
    print(new_email)
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM email_table;"
    
    new_table = db.query_db(query)
       
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template("success.html",newemail = new_table)

    @app.route('/delete',methods=['DELETE'])
    def delete():
        db = connectToMySQL(SCHEMA)
        query = "DELETE * FROM email_table WHERE email=%(email)s;"
        data={
            'email':x['email'],
            'created_at':x['created_at']
        }

    
        new_data = db.query_db(query,data)
        
        return render_template("success.html",newemail = new_data)

if __name__=="__main__":
    app.run(debug=True)