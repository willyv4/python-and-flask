# Put your app in here.
from flask import Flask, request

app = Flask(__name__)


@app.route(f'/add', methods=["GET"])
def add():
    """Add a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a + b)


@app.route('/sub', methods=["GET"])
def sub():
    """Substract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a - b)


@app.route('/mult', methods=["GET"])
def mult():
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a * b)


@app.route('/div', methods=["GET"])
def div():
    """Divide a by b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a / b)


@app.route('/math/<operation>', methods=["GET"])
def math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    operations = {
        'add': lambda a, b: a + b,
        'sub': lambda a, b: a - b,
        'mult': lambda a, b: a * b,
        'div': lambda a, b: a / b,
    }

    return str(operations[operation](a, b))
