#simple calculator website by @noxzyous

from flask import Flask, render_template, request

calc = Flask(__name__)

@calc.route('/')
def home_page():
    return render_template('form.html')

if __name__ == '__main__':
    calc.run()

