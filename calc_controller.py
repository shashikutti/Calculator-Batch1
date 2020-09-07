from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/result/<a>/<b>/<value>')
def result(a, b, value):
    return f'{a} + {b} = {value}'


@app.route('/calculator', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        return redirect(url_for('result', a=a, b=b, value=a+b))
    else:
        a = request.args.get('a')
        return redirect(url_for('result', value=a))


if __name__ == '__main__':
    app.run(debug=True)
