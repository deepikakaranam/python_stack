from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'asdffghjjkkl'

@app.route('/')
def index():
    return render_template("index.html",message="message")

@app.route('/process_money',methods=["POST"])
def process_money():
    location=request.form["building"]
    building_map = {
        'farm':random.randint(10,21),
        'cave':random.randint(5,11),
        'house':random.randint(2,6),
        'casino':random.randint(-50,51)
    }
    print (location)
    print(building_map[location])
    cur_gold=building_map[location]

    if 'gold' in session:
        session['gold']+= cur_gold
    else:
        session['gold']=cur_gold
    

    if cur_gold>0:
        message={
            'class':'green',
            'content':"You won {} golds at the {}.".format(cur_gold,location)
        }
    else:
        message={
            'class':'red',
            'content': "You lost{} golds at the {}.".format(cur_gold,location)
        }

    if not 'activities' in session:
        session['activities']=[message]
    else:
        session['activities'].append(message)
        session.modified = True
    return redirect('/')

@app.route('/reset')
def reset():
    
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True) 