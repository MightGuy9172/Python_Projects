from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests

#-------------------------------------INITIALIZE---------------------------------------
load_dotenv()
API_KEY=os.environ["API_KEY"]
OMDb_API_ENDPOINT= "http://www.omdbapi.com/"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'anysecret'

#-------------------------------------FORM---------------------------------------
class MyForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5",validators=[DataRequired()])
    review = StringField("Your Review",validators=[DataRequired()])
    submit = SubmitField("Done")

#-------------------------------------CREATE DATABASE---------------------------------------
class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-list.db"
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    year:Mapped[str] =mapped_column(nullable=False)
    description:Mapped[str] =mapped_column(nullable=False)
    rating:Mapped[float] =mapped_column(nullable=False)
    ranking:Mapped[float] =mapped_column(nullable=False)
    review:Mapped[str] =mapped_column(nullable=False)
    img_url:Mapped[str] =mapped_column(nullable=False)

with app.app_context():
    db.create_all()


#-------------------------------------HOME---------------------------------------
@app.route("/")
def home():
    data=db.session.execute(db.select(Movie))
    all_movies=data.scalars().all()
    return render_template("index.html",all_movies=all_movies)


#-------------------------------------EDIT/UPDATE---------------------------------------
@app.route("/upadte/<int:movie_id>",methods=["GET","POST"])
def update(movie_id):
    form=MyForm()
    movie_update = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_update.rating = float(form.rating.data)
        movie_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",form=form,movie=movie_update)


#-------------------------------------DELETE---------------------------------------
@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect(url_for('home'))


#-------------------------------------ADD---------------------------------------
@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        movie_name = request.form["title"]
        parameter = {
            "t": movie_name,
            "apikey": API_KEY,
        }
        response = requests.get(url=OMDb_API_ENDPOINT, params=parameter)
        response.raise_for_status(),
        result = response.json()

        with app.app_context():
            movie = Movie(
                title=result["Title"],
                year=result["Year"],
                description=result["Plot"],
                rating=result["imdbRating"],
                ranking=int(float(result["imdbRating"])),
                img_url=result["Poster"],
                review=result["Genre"]
            )
            db.session.add(movie)
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
