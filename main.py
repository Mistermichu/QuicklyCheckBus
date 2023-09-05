from StopSelecter import StopSelecter
from Routes import Routes
from Delays import Delays


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_DELAYS = "http://api.zdiz.gdynia.pl/pt/delays?stopId={stop_id}"
URL_STOP_TIMES = "http://api.zdiz.gdynia.pl/pt/stop_times"

stop = StopSelecter(URL_STOPS, URL_STOP_TIMES)

run_app = True
while run_app:
    stop.get_stop_data()
    stop.stop_time_table()
    print(stop.timeTable)
