import datetime

today = str(datetime.date.today()).replace("-", "")
print(today)

time_1 = "10:50:00"
time_2 = "12:00:00"
check = time_1 > time_2
print(check)

time_now = datetime.datetime.now()
time_plus_hour = time_now + datetime.timedelta(hours=1)
time_now = str(time_now.strftime("%H:%M:%S"))
time_plus_hour = str(time_plus_hour.strftime("%H:%M:%S"))
print(time_now)
print(time_plus_hour)
