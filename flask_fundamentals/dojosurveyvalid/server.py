# import Flask
from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("survey.html")


@app.route("/result", methods=['POST'])
def submit():
    Name = request.form['name']
    Location = request.form['location']
    Languages = request.form['languages']
    Comment = request.form['comment']
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['name']) <= 3:
        flash("Name must be 3+ characters", 'name')
    
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!", 'comment')
    elif len(request.form['comment']) > 120:
        flash("Comment must be less than 100 characters", 'comment')
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template('result.html')
if __name__=="__main__":
    app.run(debug=True)