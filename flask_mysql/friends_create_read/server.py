from flask import Flask,render_template,redirect,request,session
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "asdmdnmnbscbs cn dcn"

SCHEMA = "friendsdb"
@app.route('/')
def index():
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM friends;"
    friend_list = db.query_db(query)
    print(friend_list)
        
    return render_template('index.html',friends= friend_list)
@app.route('/create',methods=['POST'])
def create():
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    new_friend_id = db.query_db(query, data)
    print('*'*10)
    print(new_friend_id)   
    print('*'*10)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)