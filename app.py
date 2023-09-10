from StopSelecter import StopSelecter
from flask import Flask, render_template, request

app = Flask(__name__)


URL_STOPS = "http://api.zdiz.gdynia.pl/pt/stops"
URL_STOP_TIMES = "http://api.zdiz.gdynia.pl/pt/stop_times"

stop = StopSelecter(URL_STOPS, URL_STOP_TIMES)

try:
    import json
    with open('stops_list.json', 'r', encoding='utf-8') as f:
        stops_data = json.load(f)
        stops_list = []
        for specific_stop_data in stops_data:
            stop_name = specific_stop_data.get("stopName")
            stops_list.append(stop_name)
            stops_list = sorted(stops_list)
except FileNotFoundError:
    stops_list = []


@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        selected_stop = request.form.get("selected_stop")
        if selected_stop:
            stop.get_stop_data(selected_stop)
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

        return render_template("index.html", stops=stops_list, result=result)

    stops = stops_list
    return render_template("index.html", stops=stops)


if __name__ == "__main__":
    app.run()
