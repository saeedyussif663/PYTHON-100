import datetime as dt
import pandas, random, smtplib
EMAIL = "placeholder"
PASSWORD = "aune sckl aeww xdsg"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthday_dic = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dic:
    birthday_person = birthday_dic[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file=file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=birthday_person['email'],
            msg=f"Subject:Birthday\n\n {contents}")