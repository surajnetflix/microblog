from flask import Flask, render_template, request, redirect, url_for, session, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Hello World"
    usrs = ["Suraj", "Qualcomm", "Hyderabad", "India"]
    return jsonify(msg=msg, usrs=usrs)

if __name__ == '__main__':
    app.run(debug=True)
