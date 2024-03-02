# 1. Write a Python program to subtract five days from current date.
# Sample Date : 
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17
# Solution is 

import datetime
from datetime import timedelta


def subtract_five_days():
    today = datetime.date.today()
    five_days_before = today - timedelta(days=5)
    return five_days_before


print(subtract_five_days())



# 2. Write a Python program to print yesterday, today, tomorrow.
print(f"Yesterday was: {datetime.date.today() - timedelta(days=1)}")
print(f"Today is: {datetime.date.today()}")
print(f"Tommorrow is: {datetime.date.today() + timedelta(days=1)}")


# 3. Write a Python program to drop microseconds from datetime.
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  

# 4. Write a Python program to calculate two date difference in seconds

def date_diff_in_seconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds


print(date_diff_in_seconds(datetime.datetime.now(), datetime.datetime(2022, 1, 1)))