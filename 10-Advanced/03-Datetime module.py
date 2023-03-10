print("Python has the datetime module to help deal with timestamps in your code.")

import datetime

print("A time instance only holds values of time, and not a date associated with the time.")

t = datetime.time(4, 20, 1)
# Let's show the different components
print(t)
print('Hour  :', t.hour)
print('Minute:', t.minute)
print('Second:', t.second)
print('Microsecond:', t.microsecond)
print('Tzinfo:', t.tzinfo)
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)


print("\nDatetime instances have attributes for year, month, and day.")
today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)

print("\nDatetime differences")
d1 = datetime.date(2030, 4, 12)
print("Datetime 1", d1)
d2 = datetime.date(2015, 3, 11)
print("Datetime 2", d2)
print("Datetime difference", d1-d2)
