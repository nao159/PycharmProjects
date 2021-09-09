##################### Extra Hard Starting Project ######################
import smtplib

import pandas as pd
import datetime as dt
import random
# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv", na_values=["."])
today = dt.datetime.now()
current_day = (today.month, today.day)
# 2. Check if today matches a birthday in the birthdays.csv
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
MY_MAIL = "vainikkaxd@gmail.com"
MY_PASSWORD = "031099ma"

if current_day in birthdays_dict:
    num = random.randint(1, 2)
    person = birthdays_dict[current_day]["name"]
    email = birthdays_dict[current_day]["email"]
    file_path = f"letter{num}.txt"
    with open(file_path, "r") as letter:
        letter_context = letter.read()
        new_letter = letter_context.replace("xnamex", person)
        print(person)
        print(new_letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{new_letter}")

# 4. Send the letter generated in step 3 to that person's email address.




