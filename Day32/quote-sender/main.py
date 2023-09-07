import smtplib
import datetime as dt
import random
EMAIL = 'test.rbhat@gmail.com'
PASSWORD = 'enregiarlbtffjmh'


current_date = dt.datetime.now().weekday()

if current_date == 6:
    with open('quotes.txt') as file:
        quotes = file.readlines()

    quotes = [quote.strip() for quote in quotes]
    quote_of_the_day = random.choice(quotes)
    quote, quotee = quote_of_the_day.split('-')

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Monday Motivation!\n\n{quote}\n-{quotee}")
