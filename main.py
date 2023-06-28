import pandas as pd
import datetime as dt
import random
import smtplib

birthday_file = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "mateusz.pujer@pomel.com.pl"
password = "epymlypuchuvtbhg"

for index, row in birthday_file.iterrows():
    if row["month"] == month and row["day"] == day:
        random_number_of_letter = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number_of_letter}.txt", 'r') as letter:
            text = letter.read().replace('[NAME]', f'{row["name"]}')
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday\n\n{text}"
                )





