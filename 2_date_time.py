from datetime import datetime, timedelta

date_today = datetime.now()
delta_days = timedelta(days=1)
delta_months = timedelta(days=30)
date_yesterday = date_today-delta_days
date_month_before = date_today-delta_months

print(date_today.strftime('%d.%m.%y'))
print(date_yesterday.strftime('%d.%m.%y'))
print(date_month_before.strftime('%d.%m.%y'))


#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

d = "01/01/17 12:10:03.234567"
d_datetime_object = datetime.strptime(d,'%d/%m/%y %H:%M:%S.%f')
print(d_datetime_object)