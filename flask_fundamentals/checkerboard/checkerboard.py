from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checker():
    return render_template("checkerboard.html")


@app.route('/<num>')
def square(num):
    num = int(num)
    result = []
    for i in range(num):
        result.append([])
        for j in range(num):
            if i % 2 == 0:
                if j % 2 == 0:
                    result[i].append("red")
                else:
                    result[i].append("black")
            else:
                if j % 2 == 0:
                    result[i].append("black")
                else:
                    result[i].append("red")
    print(result)

    return render_template("checkerboard.html", blocknum=num, checkerboard=result)


if __name__ == "__main__":
    app.run(debug=True)
