from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Enter /c</h1>'


@app.route('/f')
@app.route('/f/<degrees>')
def f(degrees="0"):
    return fahrenheit_to_celsius(degrees)


@app.route('/c')
@app.route('/c/<degrees>')
def c(degrees="0"):
    return celsius_to_fahrenheit(degrees)


def fahrenheit_to_celsius(degrees):
    try:
        degrees = int(degrees)
        celsius = (degrees - 32) * (5 / 9)
        output = 'The converted degrees are: {}'.format(celsius)
    except ValueError:
        output = 'The degrees to convert must be a number'
    return output


def celsius_to_fahrenheit(degrees):
    try:
        degrees = int(degrees)
        fahrenheit = (degrees * (9 / 5)) + 32
        output = 'The converted degrees are: {}'.format(fahrenheit)
    except ValueError:
        output = 'The degrees to convert must be a number'
    return output


if __name__ == '__main__':
    app.run()
