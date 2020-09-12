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

        return render_template('calc_view.html', result=result)
    else:
        return render_template('calc_view.html')


if __name__ == '__main__':
    app.run(debug=True)
