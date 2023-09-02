from StopSelecter import StopSelecter


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_DELAYS = "http://api.zdiz.gdynia.pl/pt/delays?stopId={stop_id}"
URL_ROUTES = "http://api.zdiz.gdynia.pl/pt/routes"

stop = StopSelecter(URL_STOPS)
stop.get_stop_data()
print(stop.stop_data["stopId"])
