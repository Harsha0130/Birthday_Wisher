# import smtplib
#
# email = "-----@gmail.com"
# password = "--------------"
#
# with (smtplib.SMTP("smtp.gmail.com")) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email,
#                         to_addrs="------.com",
#                         msg="Subject: Hello!\n\n This is Harsha from Amazon")

import datetime as dt

# now = dt.datetime.now()
#
# minute = now.minute
# second = now.second
# week = now.weekday()
#
# print(minute)
# print(second)
# print(week)

dob = dt.datetime(year=2024, month=6, day=17)
print(dob)

aa = dob.weekday()
print(aa)


