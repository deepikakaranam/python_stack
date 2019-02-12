from flask import Flask,render_template,redirect,request,session,flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key="ancyeunksnkdwuydwijslmc,snjwfheik"
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/process", methods=['POST'])
def submit():
    FirstName = request.form['first_name']
    LastName = request.form['last_name']
    Email = request.form['email']
    Password = request.form['password']
        
    if len(request.form['first_name']) < 1:
        flash("Name cannot be blank!", 'first_name')
    elif len(request.form['first_name']) <= 3:
        flash("Name must be 3+ characters", 'first_name')
    if str.isalpha(request.form['first_name']) is False:
         flash("Name cannot have numbers", 'first_name')

    if len(request.form['last_name']) < 1:
        flash("Name cannot be blank!", 'first_name')
    elif len(request.form['last_name']) <= 3:
        flash("Name must be 3+ characters", 'last_name')

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    
    if len(request.form['password']) <8:
        flash("Password should be more than 8 characters")
    elif len(request.form['password']) != len((request.form['confirm_password'])):
        flash("Password donot match")
    if  '_flashes' in session.keys():
        flash("****Error****")
    else:
        flash("Thank You for submitting the form")
        
    
    if '_flashes' in session.keys():
        return redirect("/")
    else:      
        return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)