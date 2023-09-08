import requests
import json
import sys
import datetime


def download_data(url, file_name):
    try:
        dowlonad_data = requests.get(url)
        if dowlonad_data.status_code == 200:
            file_data = dowlonad_data.json()
            with open(file_name, "w") as data:
                json.dump(file_data, data)
        else:
            print("Błąd pobierania danych")
            sys.exit(1)
    except Exception as error:
        print("Wystąpił błąd pobierania danych", str(error))
        sys.exit(1)


def assign_data(file_name):
    with open(file_name, "r") as data_list:
        file_data = json.load(data_list)
    return file_data


def exclude_trips(time_table):
    '''
    time_now = datetime.datetime.now()
    '''
    ###
    time_now = datetime.datetime(2023, 9, 7, 00, 1, 0)
    ###
    time_plus_hour = time_now + datetime.timedelta(hours=1)
    time_now = str(time_now.strftime("%H:%M:%S"))
    time_plus_hour = str(time_plus_hour.strftime("%H:%M:%S"))
    trip_to_remove = []
    for trip_id, trip_data in time_table.items():
        departure_time = trip_data.get("departureTime")
        if departure_time >= "24:00:00":
            continue
        if time_now > departure_time or departure_time > time_plus_hour:
            trip_to_remove.append(trip_id)
    for id_to_remove in trip_to_remove:
        del time_table[id_to_remove]


def exclude_trips_2(time_table):
    time_now = datetime.datetime.now()
    '''
    Inser specific time for testing:
    time_now = datetime.datetime(2023, 9, 8, 00, 1, 0)
    '''
    time_plus_hour = time_now + datetime.timedelta(hours=1)
    trip_to_remove = []
    for trip_id, trip_data in time_table.items():
        if "estimatedTime" in trip_data:
            departure_time = trip_data.get("estimatedTime")
        else:
            departure_time = trip_data.get("departureTime")
        if time_now > departure_time or departure_time > time_plus_hour:
            trip_to_remove.append(trip_id)
    for id_to_remove in trip_to_remove:
        del time_table[id_to_remove]


def time_to_string(time_table, time):
    for trip_id, trip_data in time_table.items():
        departure_time = trip_data.get(time)
        if departure_time:
            departure_time = str(departure_time.strftime("%H:%M:%S"))
            trip_data[time] = departure_time
            time_table[trip_id] = trip_data
