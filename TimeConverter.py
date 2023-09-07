from datetime import datetime, timedelta


def convert_time(time_table, key):
    for trip_id, trip_data in time_table.items():
        departure_time = trip_data.get(key)
        hour, minute, second = map(int, departure_time.split(':'))
        if hour >= 24:
            hour -= 24
            today = datetime.today()
            day_delta = timedelta(days=1)
            today += day_delta
            departure_time = today.replace(
                hour=hour, minute=minute, second=second, microsecond=0)
        else:
            today = datetime.today()
            departure_time = today.replace(
                hour=hour, minute=minute, second=second, microsecond=0)
        trip_data[key] = departure_time
        time_table[trip_id] = trip_data
