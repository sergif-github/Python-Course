# Module 11: Additional Python Modules and Libraries

## Part 1: Dates and Times Manipulation (datetime module)

Working with dates and times is a common task in many Python applications. The `datetime` module provides classes and functions
for manipulating dates, times, and timestamps in Python.

### 1.1 Datetime module

To work with dates and times, you need to import the `datetime` module. Here's an example:

```python
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current datetime:", current_datetime)

# Create a specific date
specific_date = datetime.datetime(2023, 6, 15)
print("Specific date:", specific_date)

# Extract components from a datetime object
year = specific_date.year
month = specific_date.month
day = specific_date.day
hour = specific_date.hour
minute = specific_date.minute
second = specific_date.second

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)

# Perform arithmetic operations with datetime objects
tomorrow = current_datetime + datetime.timedelta(days=1)
print("Tomorrow:", tomorrow)

# Format datetime as a string
formatted_date = specific_date.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)
```

In this example, we import the datetime module and use it to perform various operations. Here's what each step does:
- We use the datetime.now() function to get the current date and time.
- We create a specific date by calling datetime.datetime() with the year, month, and day as arguments.
- We extract the individual components of a datetime object using attributes like year, month, day, hour, minute, and second.
- We perform arithmetic operations with datetime objects using the timedelta function, which allows us to add or subtract time intervals.
- We format a datetime object as a string using the strftime() method and a formatting string.

### 1.2 Summary

The datetime module provides many more functionalities for working with dates and times, including comparing dates, parsing 
strings into datetime objects, and working with time zones. You can refer to the official Python documentation for more information
on the datetime module.