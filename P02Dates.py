# https://www.w3schools.com/python/python_datetime.asp

import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print("========")
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%M"))  # Minute
print(x.strftime("%m"))  # Month Num
print(x.strftime("%d"))  # Hour

# Date Object

x = datetime.datetime(1962, 0o3, 0o2)

print(x)

x = datetime.datetime.now()
y = "<<<Today is {0} in {1} the month of {0}."

day = x.strftime("%a")
mon = x.strftime("%b")

print(y.format(day, mon))

print(f'>>>Today is {day} in the month of {mon}.')
