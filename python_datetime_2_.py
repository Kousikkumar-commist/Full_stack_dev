import datetime
a=datetime.datetime.now()
print("time =",a.strftime("%H:%M:%S"))
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

from datetime import time
print(time())
print(time(4,32,45))
print(time(hour=13, minute=32,second=45))
a=time(12,12,12,121212)
print(a.hour)
print(a.second)
print(a.minute)
print(a.microsecond)

from datetime import date,time
print(date(year=2024,month=5,day=22))
print(datetime.datetime(year=2024,month=5,day=22,hour=5,minute=19,second=15))
a=datetime.datetime(year=2024,month=5,day=22,hour=5,minute=19,second=15)
print(type(a))

# This is known as the timedelta
a=datetime.datetime(year=2024,month=5,day=22,hour=5,minute=19,second=15)
b=datetime.datetime(year=2014,month=5,day=22,hour=5,minute=19,second=15)
print(type(a-b)) 