import smtplib
import pandas
import random
import datetime as dt
EMAIL = 'test.rbhat@gmail.com'
PASSWORD = 'enregiarlbtffjmh'


# Accessing birthdays from csv file anc creating a list of birthdays
data = pandas.read_csv('birthdays.csv')
birthday_data = data.to_dict(orient='records')

# Getting current date from datetime module
now = dt.datetime.now()
month = now.month
day = now.day

templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

for bd in birthday_data:
    if month == bd['month'] and day == bd['day']:
        with open(f"letter_templates/{random.choice(templates)}") as file:
            msg = file.read()
        msg = msg.replace('[NAME]', bd['name'])
        msg = msg.replace('Angela', 'Meow')

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(EMAIL, bd['email'], f"Subject: Happy Birthday!\n\n{msg}")
