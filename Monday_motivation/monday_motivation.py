import smtplib
import datetime as dt
import random

email = "------@gmail.com"
password = "-------"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="--------@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n {quote}")
