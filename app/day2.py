from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash

app = Flask(__name__)

@app.route('/')
def index():
    msg = "Welcome to Flask!"
    return render_template("index.html", msg=msg)

@app.route('/home')
def home():
    msg = "Home Page! SURAJ SHEDGE"
    return jsonify(msg=msg)

if __name__ == "__main__":
    app.run(debug=True)

