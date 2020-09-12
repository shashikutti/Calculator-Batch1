from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/result/<a>/<b>/<value>/<operation>')
def result(a, b, value, operation):
    if operation == 'Add':
        return f'{a} + {b} = {value}'
    elif operation == 'Subtract':
        return f'{a} - {b} = {value}'
    elif operation == 'Multiply':
        return f'{a} * {b} = {value}'
    elif operation == 'Divide':
        return f'{a} / {b} = {value}'


@app.route('/calculator', methods=['POST', 'GET'])
def Calculate():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        operation = request.form['operation']
        if operation == 'Add':
            return redirect(url_for('result', a=a, b=b, value=a + b, operation=operation))
        elif operation == 'Subtract':
            return redirect(url_for('result', a=a, b=b, value=a - b, operation=operation))
        elif operation == 'Multiply':
            return redirect(url_for('result', a=a, b=b, value=a * b, operation=operation))
        elif operation == 'Divide':
            return redirect(url_for('result', a=a, b=b, value=a / b, operation=operation))
    else:
        a = request.args.get('a')
        return redirect(url_for('result', value=a))


if __name__ == '__main__':
    app.run(debug=True)