import requests
import json
import sys


class Trips:
    def __init__(self, url_trips):
        self.url_trips = url_trips
        self.trips = self.trips_list()

    def trips_list(self):
        try:
            dowlonad_trips = requests.get(self.url_trips)
            if dowlonad_trips.status_code == 200:
                trips_data = dowlonad_trips.json()
                with open("trips_list.json", "w") as trips:
                    json.dump(trips_data, trips)
                    return trips_data
            else:
                print("Błąd pobierania danych")
                sys.exit(1)
        except Exception as error:
            print("Wystąpił błąd pobierania danych", str(error))
            sys.exit(1)
