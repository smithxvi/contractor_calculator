import math
import datetime
from datetime import timedelta


def calculate_pay():

    while True:

        try:
            user_hours = float(input("Hours: "))
            user_minutes = float(input("Minutes: "))
            user_seconds = float(input("Seconds: "))
            user_hourly_rate = float(input("Enter hourly rate: "))
            hours_minutes_seconds = timedelta(hours= user_hours, minutes = user_minutes, seconds = user_seconds)
        
            # convert user time to decimal format

            time_in_decimal_format = round(user_hours * (1/1) + user_minutes * (1/60) + user_seconds * (1/3600),2)

            # calculate pay

            pay = time_in_decimal_format * user_hourly_rate
            return f"Number of Hours in decimal form: {time_in_decimal_format}. Total pay: {pay}"
            

        except:
            print("Please enter a valid numerical value")









    






