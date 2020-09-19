import calc_model

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main():
    add = '+'
    subtract = '-'
    multiply = '×'
    divide = '÷'
    exponent = '**'
    result = 0
    if request.method == 'POST':
        display_text = request.form['display']
        if add in display_text:
            num1, num2, num3= display_text.split(add)
            result = calc_model.add(num1, num2, num3)
        elif subtract in display_text:
            num1, num2, num3 = display_text.split(subtract)
            result = calc_model.subtract(num1, num2, num3)
        elif multiply in display_text:
            num1, num2, num3 = display_text.split(multiply)
            result = calc_model.multiply(num1, num2, num3)
        elif divide in display_text:
            num1, num2, num3 = display_text.split(divide)
            result = calc_model.divide(num1, num2, num3)
        elif exponent in display_text:
            num1, num2, num3 = display_text.split(exponent)
            result = calc_model.exponent(num1, num2, num3)

        return render_template('Calc_View.html', result=result)
    else:
        return render_template('Calc_View.html')


if __name__ == '__main__':
    app.run(debug=True)
