from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def checker():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print("Done")
    print(request.form)
    return render_template("checkout.html")



if __name__ == "__main__":
    app.run(debug=True)
