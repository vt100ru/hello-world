from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Web App with Python Flask! commit 1'

app.run(host='0.0.0.0', port=8081)
