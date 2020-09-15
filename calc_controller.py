
from flask import Flask, redirect, url_for, request
import math
app = Flask(__name__)


@app.route('/result/<a>/<b>/<value>/<operation>')
def result(a, b, value, operation):

    if operation == 'add':
        return f'{a} + {b} = {value}'
    elif operation == 'subtract':
        return f'{a} - {b} = {value}'
    elif operation == 'multiply':
        return f'{a} * {b} = {value}'
    elif operation == 'divide':
        return f'{a} / {b} = {value}'
    elif operation == 'log':
        return f'log {a}  = {value}'
    elif operation == 'log10':
        return f'log10 {a}  = {value}'

@app.route('/calculator', methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        operation = request.form['operations']
        if operation == 'add':
            return redirect(url_for('result', a=a, b=b, value=a+b, operation=operation))
        elif operation == 'subtract':
            return redirect(url_for('result', a=a, b=b, value=a-b, operation=operation))
        elif operation == 'multiply':
            return redirect(url_for('result', a=a, b=b, value=a*b,  operation=operation))
        elif operation == 'divide':
            return redirect(url_for('result', a=a, b=b, value=a/b,  operation=operation))
        elif operation == 'log':
            return redirect(url_for('result', a=a, b=b, value=math.log(a), operation=operation))
        elif operation == 'log10':
            return redirect(url_for('result', a=a, b=b, value=math.log10(a), operation=operation))

    else:
        a = request.args.get('a')
        return redirect(url_for('result', value=a))


if __name__ == '__main__':
    app.run(debug=True)
