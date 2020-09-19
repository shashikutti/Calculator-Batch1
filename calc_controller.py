from flask import Flask, redirect, url_for, request, render_template
import calc_model

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def load_homepage():
    if request.method == 'POST':
        display_text = request.form['display']
        result = None
        plus = '+'
        minus = '-'
        multiply = 'x'
        divide = '/'
        power = '^'
        fac = '!'
        sqroot = '√'

        if plus in display_text:
            num1, num2 = display_text.split(plus)
            result = calc_model.add(num1, num2)
        elif minus in display_text:
            num1, num2 = display_text.split(minus)
            result = calc_model.subtract(num1, num2)
        elif multiply in display_text:
            num1, num2 = display_text.split(multiply)
            result = calc_model.multiply(num1, num2)
        elif divide in display_text:
            num1, num2 = display_text.split(divide)
            result = calc_model.divide(num1, num2)
        elif power in display_text:
            num1, num2 = display_text.split(power)
            result = calc_model.power(num1, num2)
        elif fac in display_text:
            strlen = len(display_text)
            substr = display_text[0:strlen-1]
            result = calc_model.fac(substr)
        elif sqroot in display_text:
            strlen = len(display_text)
            substr = display_text[1:strlen]
            result = calc_model.sqroot(substr)

        return render_template('calc_view.html', result=result)
    else:
        return render_template('calc_view.html')


if __name__ == '__main__':
    app.run(debug=True)
