from flask import Flask

app = Flask("moshe")


@app.route('/')
def hello_world():
    # return 'Hello! I am a Flask application'
    a = 10
    b = 5
    return str(a + b)


app.run(host='0.0.0.0')
