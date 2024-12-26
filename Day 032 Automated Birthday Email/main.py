'''
The purpose of this project was to gain experience using datetime and smtplib. I practiced getting the
current date and viewing attributes such as day, weekday, and year. I learned how to open an SMTP connection
over tls, and how to send an email over that connection.
'''

import random, os
import smtplib
import datetime as dt
import pandas

# Define my email and password
my_email = 'EMAIL'
my_password = 'PASSWORD'

# Get CSV data listing name, email, year, month, day
data = pandas.read_csv("./birthdays.csv")
birthday_list = [row.to_dict() for index, row in data.iterrows()]

# Get today's datetime information
now = dt.datetime.now()

# Check for birthday for each person in list
for person in birthday_list:
    if person["month"] == now.month and person["day"] == now.day:
        
        # If it is their birthday, generate a birthday greeting from a random template
        random_file = random.choice(os.listdir("./birthday_greetings"))
        with open(f'./birthday_greetings/{random_file}') as file:
            message = file.read()
        # Replace "[NAME]" with their name
        message = message.replace("[NAME]", person["name"])
        # Send message in an email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=person["email"],
                                msg=f'Subject:Happy Birthday\n\n{message}')
