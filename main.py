from StopSelecter import StopSelecter


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_STOP_TIMES = "http://api.zdiz.gdynia.pl/pt/stop_times"

stop = StopSelecter(URL_STOPS, URL_STOP_TIMES)

run_app = True
while run_app:
    stop.get_stop_data()
    stop.stop_time_table()
    for trip_id, trip_data in stop.timeTable.items():
        if len(trip_data) == 5:
            print("*" * 20)
            print("*KURS NIEZALOGOWANY*")
            print(f"Linia: {trip_data['routeShortName']}")
            print(f"Kierunek: {trip_data['tripHeadsign']}")
            print(f"Planowany odjazd: {trip_data['departureTime']}")
        else:
            print("*" * 20)
            print(f"Linia: {trip_data['routeShortName']}")
            print(f"Kierunek: {trip_data['tripHeadsign']}")
            print(f"Planowany odjazd: {trip_data['departureTime']}")
            print(f"Rzeczywisty czas odjazdu: {trip_data['estimatedTime']}")
            print(f"Numer boczny pojazdu: {trip_data['vehicleCode']}")
    print("*" * 50)
