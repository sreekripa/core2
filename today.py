from datetime import date
today= date.today()
print("day",today)

from datetime import datetime
now = datetime.now()
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)