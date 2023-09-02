from StopSelecter import StopSelecter
from Routes import Routes
from Delays import Delays


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_DELAYS = "http://api.zdiz.gdynia.pl/pt/delays?stopId={stop_id}"
URL_ROUTES = "http://api.zdiz.gdynia.pl/pt/routes"

stop = StopSelecter(URL_STOPS)
routes = Routes(URL_ROUTES)


run_app = True
while run_app:
    stop.get_stop_data()
    delays = Delays(URL_DELAYS, stop.stop_data["stopId"])
    print("*" * 50)
    print(f"Ostatnia aktualizacja: {delays.delays['lastUpdate']}")
    if len(delays.delays["delay"]) == 0:
        print("Brak odjazdów")
    else:
        for line_data in delays.delays["delay"]:
            routes.get_route_data(line_data["routeId"])
            line_name = routes.route_data["routeShortName"]
            destination = line_data["headsign"]
            theoretical_time = line_data["theoreticalTime"]
            estimated_time = line_data["estimatedTime"]
            print(f"{line_name} {destination} Czas rozkładowy: {theoretical_time} Rzeczywisty czas przyjazdu: {estimated_time}")