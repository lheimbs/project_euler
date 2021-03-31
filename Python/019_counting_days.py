from datetime import timedelta, datetime

d = datetime(1901, 1, 1)
d += timedelta(days=6-d.weekday())

sundays = 0
while d < datetime(2001, 1, 1):
    if d.day == 1 and d.weekday() == 6:
        sundays += 1
    d += timedelta(days=7)

print(sundays)

