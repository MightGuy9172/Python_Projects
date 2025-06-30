from ensurepip import bootstrap

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
        email = EmailField('Email',validators=[DataRequired(), Email("Invaild email")])
        password=PasswordField('Password',validators=[DataRequired(),Length(min=8)])
        submit=SubmitField('Submit')



app = Flask(__name__)
app.secret_key="manish@9896"
bootstrap=Bootstrap5(app)


@app.route("/login",methods=["GET","POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)



@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
