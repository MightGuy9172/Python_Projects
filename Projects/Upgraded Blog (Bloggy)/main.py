from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


MY_EMAIL=os.environ['MYUSER']
MY_PAASWORD=os.environ['PASS']

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_PKG_TYPE'] = 'standard'


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    result=db.session.execute(db.select(BlogPost))
    all_posts=result.scalars().all()
    return render_template("index.html", all_posts=all_posts)

@app.route("/add-post",methods=["GET","POST"])
def make_post():
    form=CreatePostForm()
    if form.validate_on_submit():
        new_post=BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=datetime.now().strftime("%B %d, %Y")
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html",form=form, is_edit=False)



@app.route("/edit-post/<int:index>",methods=["GET","POST"])
def edit_post(index):
    post = db.get_or_404(BlogPost, index)
    edit_form = CreatePostForm(
        title= post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title=edit_form.title.data
        post.subtitle=edit_form.subtitle.data
        post.author=edit_form.author.data
        post.img_url=edit_form.img_url.data
        post.body=edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", index=post.id))
    return render_template("make-post.html",form=edit_form, is_edit=True,  post=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == "POST":
        #Extracting Data
        name=request.form["name"]
        email=request.form["email"]
        phone=request.form["phone"]
        msg=request.form["message"]

        #Writing MSg
        content=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}"
        person=os.environ["PERSON"]

        #Sending Message
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PAASWORD)
            msg = MIMEText(content, _charset="utf-8")
            msg['Subject'] = "Success !"
            msg['From'] = MY_EMAIL
            msg['To'] = person
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person, msg=msg.as_string())

        return render_template("contact.html",success=True)
    else:
        return render_template("contact.html",success=False)


@app.route("/delete/<int:index>")
def delete_post(index):
    post_to_delete = db.get_or_404(BlogPost, index)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))



@app.route("/post/<int:index>")
def show_post(index):
    post=db.get_or_404(BlogPost,index)
    return render_template("post.html", post=post)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
