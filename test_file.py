import datetime

print("24:40:00" >= "24:00:00")

today = str(datetime.date.today()).replace("-", "")
print(today)

time_1 = "10:50:00"
time_2 = "12:00:00"
check = time_1 > time_2
print(check)

time_now = datetime.datetime(2023, 9, 7, 23, 30, 0)
time_minus_hour = time_now - datetime.timedelta(hours=1)
time_plus_hour = time_now + datetime.timedelta(hours=1)
print(time_now)
print(time_plus_hour)
print(time_minus_hour < time_now < time_plus_hour)

'''
for trip_id, trip_data in self.timeTable:
    route_id = trip_data.get("routeId")
    departure_time = trip_data.get("departureTime")
    for delay_data in delays.list["delay"]:
        delay_route_id = delay_data.get("routeId")
        delay_departure = delay_data.get("theoreticalTime")
        delay_estimated = delay_data.get("estimatedTime")
        delay_vehicle = delay_data.get("vehicleCode")
        if route_id == delay_route_id and departure_time == delay_departure:
            trip_data["estimatedTime"] = delay_estimated
            trip_data["vehicleCode"] = delay_vehicle
'''
