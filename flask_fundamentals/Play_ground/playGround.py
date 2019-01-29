from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play/<num>/<color>')
def play(num, color):
    num = int(num)
    return render_template("playGround.html", blockNum=num, changecolor=color)


if __name__ == "__main__":
    app.run(debug=True)
