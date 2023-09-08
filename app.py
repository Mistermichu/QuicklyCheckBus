from StopSelecter import StopSelecter
from flask import Flask, render_template

app = (Flask(__name__))


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_STOP_TIMES = "http://api.zdiz.gdynia.pl/pt/stop_times"

stop = StopSelecter(URL_STOPS, URL_STOP_TIMES)


@app.route("/")
def index():
    run_app = True
    result = []
    while run_app:
        stop.get_stop_data()
        stop.stop_time_table()
        for trip_id, trip_data in stop.timeTable.items():
            if len(trip_data) == 5:
                entry = {
                    "status": "KURS NIEZALOGOWANY",
                    "linia": trip_data['routeShortName'],
                    "kierunek": trip_data['tripHeadsign'],
                    "planowany_odjazd": trip_data['departureTime']
                }
                result.append(entry)
            else:
                entry = {
                    "linia": trip_data['routeShortName'],
                    "kierunek": trip_data['tripHeadsign'],
                    "planowany_odjazd": trip_data['departureTime'],
                    "rzeczywisty_czas_odjazdu": trip_data['estimatedTime'],
                    "numer_boczny_pojazdu": trip_data['vehicleCode']
                }
                result.append(entry)
            run_app = False
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()
