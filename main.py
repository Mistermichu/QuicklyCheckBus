from StopSelecter import StopSelecter


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_DELAYS = "http://api.zdiz.gdynia.pl/pt/delays?stopId={stop_id}"
URL_STOP_TIMES = "http://api.zdiz.gdynia.pl/pt/stop_times"

stop = StopSelecter(URL_STOPS, URL_STOP_TIMES)

run_app = True
while run_app:
    stop.get_stop_data()
    stop.stop_time_table()
    time_table = dict(sorted(stop.timeTable.items(),
                      key=lambda item: item[1]["departureTime"]))
    for trip_id, trip_data in time_table.items():
        print("*" * 20)
        print(f"Linia: {trip_data['routeShortName']}")
        print(f"Kierunek: {trip_data['tripHeadsign']}")
        print(f"Odjazd: {trip_data['departureTime']}")
