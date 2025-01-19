from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, halo halo halo, hihi huhas !'

@app.route('/about')
def about():
    return 'About'