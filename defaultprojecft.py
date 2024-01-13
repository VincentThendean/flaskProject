from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    body = '<h1>Hello World! :)</h1>'
    return body


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f/<celsius>')
def convert_CtoF(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"


if __name__ == '__main__':
    app.run()
