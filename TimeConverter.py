from datetime import datetime, timedelta


def convert_time(time_table):
    for trip_id, trip_data in time_table.items():
        departure_time = trip_data.get("departureTime")
        if departure_time >= "24:00:00":
            hour, minute, second = map(int, departure_time.split(':'))
            hour -= 24
            one_hour = timedelta(hours=1)
            time_now = datetime.strptime(
                f"{hour}:{minute}:{second}", "%H:%M:%S")
            if time_now >= datetime(1900, 1, 1, 0, 0, 0) + one_hour:
                time_now -= one_hour
            converted_time = time_now.strftime("%H:%M:%S")
            departure_time = str(converted_time)
            trip_data["departureTime"] = departure_time
            time_table[trip_id] = trip_data
