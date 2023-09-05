import datetime

today = str(datetime.date.today()).replace("-", "")
print(today)

time_1 = "10:50:00"
time_2 = "12:00:00"
check = time_1 > time_2
print(check)
