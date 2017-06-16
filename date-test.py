import time
from datetime import datetime, date, time

date.today()

t=date.today()
t.year
t.month
t.day
str(t)

print(date.today())

s='today is ' + str(date.today())

'today is {}'.format(date.today())


today = date.today()
today == date.fromtimestamp(time.time())

birthday = date(today.year, 6, 24)
if birthday < today:
    birthday = birthday.replace(year=today.year + 1)

time_to_birthday = abs(birthday - today)
time_to_birthday.days

# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
datetime.combine(d, t)

# Using datetime.now() or datetime.utcnow()
datetime.now()
datetime.utcnow()

# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")

now = datetime.now()
now.strftime('%Y-%m-%d %H:%M:%S')
