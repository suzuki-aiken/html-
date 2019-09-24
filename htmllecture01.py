from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return '<h1>hello world</h1>'


@app.route('/goodbye')
def goodbye():
    return 'Good bye later'


@app.route('/add/<a>/<b>')
def add(a, b):
    print(type(a))
    return str(int(a) + int(b))


if __name__ == '__main__':
    app.run(debug=True)
