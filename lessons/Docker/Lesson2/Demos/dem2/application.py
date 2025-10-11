from flask import Flask


app = Flask('__name__')


@app.get('/hello')
def hello():
    return '<h1 style="color:red;"> hello from flask </h1>'


app.run(port=5000,host='0.0.0.0')