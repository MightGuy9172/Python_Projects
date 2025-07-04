from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=to_dict(random_cafe))

@app.route("/all")
def all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    all_result=[to_dict(cafe) for cafe in all_cafes]
    return jsonify(cafe=all_result)

@app.route("/search")
def locate():
    loc = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location==loc))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add",methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(resonse={"success": "Successfully Added a new Cafe. "})


# HTTP PUT/PATCH - Update Record
@app.route("/update/<int:cafe_id>",methods=["PATCH"])
def update(cafe_id):
    new_price = request.args.get("new_price")
    cafe=db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
    if cafe:
        cafe.coffee_price=new_price
        db.session.commit()
        return jsonify(resonse={"success": "Successfully Updated the price. "})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe of this id."}), 404


# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>",methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api_key")
    if api_key=="MyKey":
        cafe=db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(resonse={"success": "Successfully Deleted the cafe. "})
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe of this id."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
