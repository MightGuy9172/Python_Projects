from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
app.secret_key="anysecretkey"

#---------------------Initialize CLASS------------------------
class MyForm(FlaskForm):
    title=StringField("Name of the Book",validators=[DataRequired()])
    author = StringField("Author of Book", validators=[DataRequired()])
    rating = IntegerField(
        "Your Rating (1–10)",
        validators=[
            DataRequired(message="Rating is required."),
            NumberRange(min=1, max=10, message="Rating must be between 1 and 10.")
        ]
    )
    submit=SubmitField("Submit")


#---------------------Initialize DATABASE------------------------
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

#---------------------CREATE TABLE------------------------
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


#---------------------HOME PAGE------------------------
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars().all()
    return render_template("index.html",all_books=all_books)



#---------------------ADD PAGE------------------------
@app.route("/add",methods=["GET","POST"])
def add():
    form=MyForm()
    if form.validate_on_submit():
        with app.app_context():
            new_book = Book(title=form.title.data, author=form.author.data, rating=float(form.rating.data))
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html",form=form)



#---------------------EDIT PAGE------------------------
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)



#---------------------DELETE RECORD------------------------
@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

