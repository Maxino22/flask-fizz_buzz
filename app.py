from flask import Flask, render_template, session, redirect, url_for
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysec'

# form


class Form(FlaskForm):

    fizz_buzz = IntegerField('Enter a number', validators=[
                             DataRequired()],)
    submit = SubmitField('Submit')

# fizz_buzz


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizz buzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        session['fizz_buzz'] = form.fizz_buzz.data
        return redirect(url_for('result'))

    return render_template('index.html', form=form)


@app.route('/result')
def result():
    num = session['fizz_buzz']
    rest = fizz_buzz(num)
    return render_template('result.html', rest=rest)


if __name__ == '__main__':
    app.run()
