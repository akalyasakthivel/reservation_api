from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route('/')
def login():
    return render_template('log.html')

@app.route('/bus')
def source():
    return render_template('source.html')

app.run(port=5000)