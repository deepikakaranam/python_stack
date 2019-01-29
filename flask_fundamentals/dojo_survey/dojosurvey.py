from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("survey.html")


@app.route('/result', methods=['POST'])
def create_dojo():
    print("Done")
    Name = request.form['name']
    Location = request.form['location']
    Languages = request.form['Languages']
    Comment = request.form['description']

    return render_template('result.html')


@app.route('/danger')
def danger():
    print("a user tried to visit / danger.  we have redirected the user to / ")

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
