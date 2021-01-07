"""
Python's built-in datetime module
https://docs.python.org/3/library/datetime.html
"""
import datetime

# ------ DATE ------
print("DATE")

# Create a date object
date = datetime.date(2000, 1, 23)
print(date)

# Format a date
print(date.strftime("%B %d, %Y"))  # https://strftime.org/

# Get date fields
print(date.day)
print(date.month)
print(date.year)
print(date.weekday())


# ------ TIME ------
print("\nTIME")

# Create a time object
time = datetime.time(1, 23, 45, 678)
print(time)

# Format a time
print(time.strftime("%-I:%M %p"))  # https://strftime.org/

# Get time fields
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)


# ------ DATETIME ------
print("\nDATETIME")

# Create a datetime object
dt = datetime.datetime(2000, 1, 23, 4, 5, 6)
print(dt)

# Format a datetime
print(dt.strftime("%B %d, %Y %-I:%M %p"))  # https://strftime.org/

# Create a datetime from a parsed string
dt2 = datetime.datetime.strptime("March 14, 2001 1:59 AM", "%B %d, %Y %I:%M %p")
print(f"{dt2.month}.{dt2.day}{dt2.hour}{dt2.minute}")  # PI day!

# Doing math on datetimes using timedeltas
time_diff = dt2 - dt
print(time_diff.days)
print(f'Diff in years: {round(time_diff.days/365.25, 2)}')
print(time_diff.seconds)

# Or you can compare year/month/day
print(dt2.year - dt.year)

# ------ CURRENT MOMENT ------
print('\nNOW')
now = datetime.datetime.now()
print(now)
print(now.date())
print(now.time())
