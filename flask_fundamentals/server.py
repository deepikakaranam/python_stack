from flask import Flask
app = Flask(__name__)

print(__name__)


@app.route('/')
def hello_world():
    return "Hello Web!!"


@app.route('/Dojo')
def Dojo():
    return "Dojo"


@app.route('/say/<flask>')
def say(flask):
    print(flask)
    return "Hi "+flask


@app.route('/repeat/<num>/<name>')
def repeat(num, name):
    num = int(num)
    print(name*num)
    return name*num


if __name__ == "__main__":
    app.run(debug=True)
