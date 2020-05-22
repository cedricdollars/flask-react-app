from flask import Flask

app = Flask(__name__)

@app.route('/')
def app():
    return{
        'userId': 1,
        'title': 'React Flask App',
        'completed': False
    }