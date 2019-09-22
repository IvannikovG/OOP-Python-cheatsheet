import datetime
import pytz

# naive date and times
# aware date and times

d = datetime.date(2016, 7, 24)
#(year-month a without zero-day)
print('date 0 -', d)
tday = datetime.date.today()
# today`s local date, possible to grab just a day etc.
print('date 1 -', tday.isoweekday())  # recommended, sunday is 7

tdelta = datetime.timedelta(days=7)
#duration in days

print('date 2 -', tday + tdelta)
# day -> from today, 1 week from today

# how many days until my birthday this year?

bday = datetime.date(2019, 11, 16)
till_bday = bday - tday
print('date 3 -', till_bday.total_seconds())

# datetime for time

t = datetime.time(9, 30, 45, 100000)
print('time 1 -', t.second)
# t.hour, t.minute, t.second
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# includes date and time
print('the entire date and the time -', dt)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

# pytz recommends to work with utc.

dt1 = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt1)

dt1_now = datetime.datetime.now(tz=pytz.UTC)
print(dt1_now)
