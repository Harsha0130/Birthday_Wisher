# Birthday Reminder and Email Automation

This Python script checks a CSV file (`birthdays.csv`) for birthdays matching the current date and sends birthday wishes via email using Gmail SMTP.
- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course by Dr. Angela Yu.

## Prerequisites

- Python 3.x
- Libraries: `datetime`, `smtplib`, `pytz`, `pandas`, `random`

## Gmail account setup

- Enable less secure apps: [Google Account settings](https://myaccount.google.com/lesssecureapps)
- Generate an App Password: [Google App Passwords](https://myaccount.google.com/apppasswords)

## CSV file setup (`birthdays.csv`)

- Create a CSV file with columns: `name`, `month`, `day` (Already created)
- Add birthday entries in the format: `John Doe, 6, 21` (for June 21st)

## Usage

- Update `email` and `password` variables in the script with your Gmail credentials.
- Customize email templates in the `Letter_templates` directory (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`).
