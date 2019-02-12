from flask import Flask,render_template,redirect,request,session,flash
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA = "simplewall"

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
    
    pw_hash = bcrypt.generate_password_hash(request.form['password']) 
    print('*' * 100, "started",'*' * 100 )
    print(pw_hash)  
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users WHERE email=%(email)s;"
    data={
        
        
        "email" : request.form['email'],
        

    }
    email_list = db.query_db(query,data)
    if len(email_list)>0:
        flash("Email already exists")
        errors = True

    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO users (first_name,last_name,email,Password,created_at) VALUES (%(FirstName)s,%(LastName)s,%(email)s,%(password_hash)s,now());"
    data={
        
        "FirstName" : request.form['first_name'],
        "LastName" : request.form['last_name'],
        "email" : request.form['email'],
        "password_hash" : pw_hash,
        
    }
    user_list = db.query_db(query,data)
    
    
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users;"

    
    login_list = db.query_db(query)

    if errors == True:
        return redirect('/')
    else:
        flash("You are succesfully registered to the site")
        
        return redirect("/")
        

@app.route('/login',methods=['POST'])
def login():
       
    db = connectToMySQL(SCHEMA)
    query = "SELECT id,first_name,email,password FROM users WHERE email=%(email)s;"
    data={             
        "email" : request.form['email'],     
    }
    result = db.query_db(query,data)

    if result:        
        if bcrypt.check_password_hash(result[0]['password'],request.form['password']):
            session['email'] = result[0]['email']
            session['user_id'] = result[0]['id']
            session['user_name'] = result[0]['first_name']
            
            print(session['email'],session['user_id'])
            db = connectToMySQL(SCHEMA)
            query = "SELECT id,first_name,email,password FROM users WHERE id=%(user_id)s;"
            data={             
                "user_id" : session['user_id'],     
            }
            result = db.query_db(query,data)
            print(result)
            db = connectToMySQL(SCHEMA)
            query = "SELECT * FROM messages;"
            
            result_1 = db.query_db(query)
            print(result_1)
           
            
            return render_template('wall.html',result=result,messages=result_1)
    flash("You could not be logged in")
    
    
    return redirect("/")

@app.route('/message',methods=['POST'])

def message():
    if not 'user_id' in session:
        return redirect ('/')
    print(request.form)
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO messages (user_id,message,created_at) Values (%(user_id)s,%(message)s,now());"
    data={
        'user_id': session['user_id'],
        'message': request.form['description']

    }
    
    message_list = db.query_db(query,data)
       
    print(message_list)
    
      
    return redirect('/wall')
@app.route('/comment/<message_id>',methods=['POST'])
def comment(message_id):
    print("am here")
    print("from comments -->" , request.form)
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO comments (user_id,message_id,comment,created_at) Values (%(user_id)s,%(message_id)s,%(comment)s,now());"
    data={
         
        
        'user_id': session['user_id'],
        'message_id':message_id,
        'comment': request.form['comment']

    }
    
    comment_list = db.query_db(query,data)
       
    
    
      
    return redirect('/wall')


@app.route('/wall',methods=['GET'])

def wall():
    if not 'user_id' in session:
        return redirect ('/')
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users;"
    users= db.query_db(query)
    db = connectToMySQL(SCHEMA)
    query = "SELECT messages.id as message_id,users.first_name as firstname, users.last_name as lastname,users.email as email, messages.message as message,messages.created_at as date,messages.id as message_id from users join messages on users.id = messages.user_id order by date desc; "
    messages= db.query_db(query)
   
    print("messages from line 174" ,messages)
    
    db = connectToMySQL(SCHEMA)
    query = "SELECT comments.comment as comment,comments.message_id as message_id,users.first_name as firstname,users.last_name as lastname,comments.created_at as created_at FROM comments join users on comments.user_id = users.id ; "
    comments= db.query_db(query)
    print('comments FROM LINE 179 -->', comments)
   
    return render_template('wall.html',messages=messages,comments=comments)
 

@app.route('/logout')
def logout():
   session.clear()
   return redirect('/')


    
    
if __name__ == "__main__":
    app.run(debug=True)
