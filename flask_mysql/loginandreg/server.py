from flask import Flask,render_template,redirect,request,session,flash
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA = "email"

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "vchgsgcjsjdbcjdcdvmsdnvmdsnmvn"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    errors = False
    
    if len(request.form['first_name'])<2:
        flash("First name should be more than 2 characters")
        errors = True
    if str.isalpha(request.form['first_name']) is False:
        flash("Name cannot have numbers", 'first_name')
        errors = True
    if len(request.form['last_name'])<2:
        flash("Last name should be more than 2 characters")
        errors = True
    if str.isalpha(request.form['last_name']) is False:
        flash("Name cannot have numbers", 'last_name')
        errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        errors = True
    if len(request.form['password'])<8:
        flash("Password needs more than 8 characters")
        errors=True
    if len(request.form['password']) != len((request.form['confirmpassword'])):
        flash("Password donot match")
        errors = True
    pw_hash = bcrypt.generate_password_hash(request.form['password']) 
    confirm_hash = bcrypt.generate_password_hash(request.form['confirmpassword'])  
    print(pw_hash)  
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM registers WHERE email=%(email)s;"
    data={
        
        
        "email" : request.form['email'],
        

    }
    email_list = db.query_db(query,data)
    if len(email_list)>0:
        flash("Email already exists")
        errors = True

    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO registers (FirstName,LastName,email,Password ,ConfirmPassword) VALUES (%(FirstName)s,%(LastName)s,%(email)s,%(password_hash)s,%(confirm_hash)s);"
    data={
        
        "FirstName" : request.form['first_name'],
        "LastName" : request.form['last_name'],
        "email" : request.form['email'],
        "password_hash" : pw_hash,
        "confirm_hash" : confirm_hash

    }
    user_list = db.query_db(query,data)
    
    
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM registers;"

    
    login_list = db.query_db(query)

    if errors == True:
        return redirect('/')
    else:
        flash("You are succesfully registered to the site")
        return redirect("/")
        

@app.route('/login',methods=['POST'])
def login():
       
    db = connectToMySQL(SCHEMA)
    query = "SELECT email,password FROM registers WHERE email=%(email)s;"
    data={             
        "email" : request.form['email'],     
    }
    result = db.query_db(query,data)
    if result:        
        if bcrypt.check_password_hash(result[0]['password'],request.form['password']):
            session['email'] = result[0]['email']
            
            return render_template('success.html')
    flash("You could not be logged in")
    return redirect("/")

@app.route('/logout')
def logout():
   session.clear()
   return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
