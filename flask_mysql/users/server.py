from flask import Flask,render_template,redirect,request,session,flash
import re
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA = "usersassignment"
app = Flask(__name__)
app.secret_key = "vchgsgcjsjdbcjdcdvmsdnvmdsnmvn"
@app.route('/')
def index():
    db = connectToMySQL(SCHEMA)
        
    query = "select * from users;"    
     

    users = db.query_db(query)
    print(users)
    return render_template("index.html",users=users)
@app.route('/users/create')
def users():
    print(request.form)
    return render_template("users.html")

@app.route('/users/new',methods = ["POST"])
def users_new():
    print('*' * 100 ,request.form)
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
    if errors == True:
        return redirect('/users/create')
    else:
        db = connectToMySQL(SCHEMA)
            
        query = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (%(firstname)s,%(lastname)s,%(email)s,now(),now());"  
        data={
            'firstname': request.form['first_name'],
            'lastname': request.form['last_name'],
            'email': request.form['email']   
            }  
        

        users_new= db.query_db(query,data)
        print(users_new)
        
        return redirect('/')
@app.route('/<id>/edit')
def edit(id):
    db = connectToMySQL(SCHEMA)
        
    query = "select * from users WHERE id=%(id)s;"  
    data={
        'id':id
    }  
    update_user=db.query_db(query,data)
    user=update_user[0]
    print(update_user)
           
    return render_template("edituser.html",users=user)

@app.route('/<id>/update',methods = ["POST"])
def update(id):
    print("Came here")
    errors = False
    
    if len(request.form['first_name'])<2:
        flash("First name should be more than 2 characters")
        errors = True
    
    if len(request.form['last_name'])<2:
        flash("Last name should be more than 2 characters")
        errors = True
    
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        errors = True
    if errors == True:
        return redirect('/<id>/edit')
    else:
        db= connectToMySQL(SCHEMA)
        query = "UPDATE users SET first_name=%(firstname)s,last_name=%(lastname)s,email=%(email)s WHERE id=%(id)s;"
        data = {
        'firstname': request.form['first_name'],
        'lastname' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : id
            
        }
        edit_user = db.query_db(query,data)
        print(edit_user)
        
        
        return redirect('/')
@app.route('/<id>')
def show(id):
    print(id)
    db = connectToMySQL(SCHEMA)
        
    query = "select * from users WHERE id= %(id)s;"  
    data={
        'id':id
    }  
    show_user=db.query_db(query,data)
    
           
    return render_template("show.html",show=show_user)
@app.route('/<id>/delete')
def destroy(id):
    db = connectToMySQL(SCHEMA)
        
    query = "DELETE  from users WHERE id= %(id)s;"  
    data={
        'id':id
    }  
    delete_user=db.query_db(query,data)
    return redirect('/')


   

if __name__ == "__main__":
    app.run(debug=True)