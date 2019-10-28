from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Enter /c/(number to convert) or /f/(number to convert) into the URL bar</h1>'


@app.route('/f')
@app.route('/f/<degrees>')
def f(degrees="0"):
    return convert(degrees, "f")


@app.route('/c')
@app.route('/c/<degrees>')
def c(degrees="0"):
    return convert(degrees, "c")


def convert(degrees, method):
    try:
        degrees = int(degrees)
        converted_degrees = fahrenheit_to_celsius(degrees) if method == "f" else celsius_to_fahrenheit(degrees)
        output = 'The original degrees are {}{}. The converted degrees are: {}'.format(degrees, method,
                                                                                       converted_degrees)
    except ValueError:
        output = 'The degrees to convert must be a number'
    return output


def fahrenheit_to_celsius(degrees):
    return (degrees - 32) * (5 / 9)


def celsius_to_fahrenheit(degrees):
    return (degrees * (9 / 5)) + 32


if __name__ == '__main__':
    app.run()
