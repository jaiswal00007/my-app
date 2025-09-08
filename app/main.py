# app/main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from me  + Kubernetes!"

@app.route('/login')
def home():
    return "login + Kubernetes!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
