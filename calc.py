#simple calculator website by @noxzyous

from flask import Flask, render_template, request

calc = Flask(__name__)

@calc.route('/')
def home_page():
    return render_template('form.html')

@calc.route('/result', methods=['GET','POST'])
def math_is():
    if request.method=='POST':
        num1 = request.form.get("num1", type=int)
        num2 = request.form.get("num2", type=int)
        yor_job = request.form.get("yor_job")

        if(yor_job == 'Addition'):
            result = num1+num2
        elif(yor_job == 'Subtraction'):
            result = num1-num2
        elif(yor_job == 'Multiplication'):
            result = num1*num2
        elif(yor_job == 'Division'):
            if(num1==0 and num2==0):
                result = 0
            else:
                result = num1/num2
        else:
            result = 0
        output = result
        return render_template('result.html', output=output)


if __name__ == '__main__':
    calc.run(debug=True)