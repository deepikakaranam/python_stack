from flask import Flask,render_template,redirect,request,session,flash
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA = "wall"

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
           
           
            
            return redirect('/wall')
    flash("You could not be logged in")
    
    
    return redirect("/")

@app.route('/create_message',methods=['POST'])

def create_message():
    
    if not 'user_id' in session:
        return redirect ('/')
    print(request.form)
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO messages (message,created_at,sender_id,receiver_id) Values (%(message)s,now(),%(sender_id)s,%(receiver)s);"
    data={
        'sender_id': session['user_id'],
        'message': request.form['comment'],
        'receiver':request.form['receiver_id']

    }
    
    message_list = db.query_db(query,data)
    print(message_list)
    return redirect('/wall')

@app.route('/<name>/delete')
def destroy(name):
    db = connectToMySQL(SCHEMA)
        
    query = "DELETE  from users WHERE name= %(name)s;"  
    data={
        'name':name
    }  
    delete_user=db.query_db(query,data)
    return redirect('/wall')

    
      
   

@app.route('/wall',methods=['GET'])
def get_messages():
    if not 'user_id' in session:
        return redirect ('/')
    db = connectToMySQL(SCHEMA)
    query = "SELECT id,first_name,email,password FROM users WHERE id!=%(user_id)s;"
    data={             
        "user_id" : session['user_id'],     
    }
    user_list=db.query_db(query,data)
    
    print("is it working--->",user_list)
    
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM messages;"
    messages= db.query_db(query)
    
    print("is messages working--->",messages)
    db = connectToMySQL(SCHEMA)
    query = "SELECT* FROM messages WHERE receiver_id= %(id)s;"
    data={
        "id":session['user_id']
    }
    received_list= db.query_db(query,data)
    db = connectToMySQL(SCHEMA)
    query = "SELECT messages.id as id,users.first_name as name,messages.created_at as time,messages.message as message,count(messages.message)as count from users join messages on users.id=messages.sender_id where receiver_id= %(id)s;"
    data={
        "id":session['user_id']
    }
    messages_list= db.query_db(query,data)
    print(messages_list)
    
    
    
    

    return render_template('wall.html',users=user_list,messages=messages,mails= received_list,senders=messages_list)





@app.route('/logout')
def logout():
   session.clear()
   return redirect('/')


    
    
if __name__ == "__main__":
    app.run(debug=True)
