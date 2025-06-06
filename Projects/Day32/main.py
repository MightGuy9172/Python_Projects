import datetime as dt
import pandas
import random
import smtplib
from email.mime.text import MIMEText


MY_EMAIL=" "
MY_PAASWORD=" "
today=dt.datetime.now()
today_tuple=(today.month,today.day)

data=pandas.read_csv("birthdays.csv")

birth_dict={(data_row["month"],data_row["day"]-1):data_row for (index,data_row) in data.iterrows()}
print(today_tuple)
if today_tuple in birth_dict:
    person=birth_dict[today_tuple]
    print(person)
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path,encoding="utf-8") as letter:
        content=letter.read()
        content=content.replace("[NAME]",person["name"])

    with smtplib.SMTP("smtp.gmail.com") as  connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PAASWORD)
        msg = MIMEText(content, _charset="utf-8")
        msg['Subject'] = "Happy Birthday!"
        msg['From'] = MY_EMAIL
        msg['To'] = person["email"]
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=person["email"],msg=msg.as_string())
