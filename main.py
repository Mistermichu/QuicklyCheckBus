from StopSelecter import StopSelecter
from Routes import Routes
from Delays import Delays
from Trips import Trips


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_DELAYS = "http://api.zdiz.gdynia.pl/pt/delays?stopId={stop_id}"
URL_ROUTES = "http://api.zdiz.gdynia.pl/pt/routes"
URL_STOP_TIMES = "http://api.zdiz.gdynia.pl/pt/stop_times"
URL_TRIPS = "http://api.zdiz.gdynia.pl/pt/trips"

timeTable = {}

stop = StopSelecter(URL_STOPS, URL_STOP_TIMES)


#####
# 1 Pobieramy dane na temat dostępnych przystanków
# 2 Pytamu użytkownika o wybrany przystanek
# 3 Pobieramy tripId i deparureTime
# 4 Ze zbioru trips pobieramu za pomocą tripId pobieramy kierunek i routeId
# 5 Ze zbioru Rote pobieramy Route short name (numer linii)


run_app = True
while run_app:
    stop.get_stop_data()
    stop.stop_time_table()
    timeTable = stop.timeTable
    trips = Trips(URL_TRIPS)
