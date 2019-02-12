from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'asdffghjjkkl'
@app.route('/')
def index():
    if "result" not in session:
        result="no guess"
    else:
        result=session["result"]
    print(result)
    return render_template("result.html",result=result)

@app.route('/guessnum', methods=['POST'])
def guess_num():
    print("Got Post Info")
    random_num=random.randrange(0, 101)
    print(random_num)
    session['random_num']=random_num
    print(session['random_num'])
    correct=session['random_num']
    
    session['guess'] = int(request.form['guess'])
    print(session['guess'])
    
   
    numguess=int(session['guess'])   
    if correct==numguess:
        session["result"]="correct"
    if correct>numguess :
        session["result"]="Too Low"
    else:
       session["result"]="Too high"
    return redirect('/') 
if __name__=="__main__":
    app.run(debug=True) 