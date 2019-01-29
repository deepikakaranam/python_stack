from flask import Flask,render_template,session,redirect
app=Flask(__name__)
app.secret_key="asdfg"
@app.route('/')
def counter():
    if "count" in session:
        session['count']+=1
    else:
        session['count']=1
    return render_template("index.html")

@app.route('/countby2')
def countby2():
    if "count" in session:
        session['count']+=2
    else:
        session['count']=1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
