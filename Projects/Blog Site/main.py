from flask import Flask, render_template,request
import requests
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


MY_EMAIL=os.environ['MYUSER']
MY_PAASWORD=os.environ['PASS']
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()



app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


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




@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
