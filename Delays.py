import requests
import json
import sys

class Delays:
    def __init__(self, url_delays, stop_id):
        self.url_delays = url_delays
        self.stop_id = stop_id
        self.delays = self.delays_list()

    def delays_list(self):
        try:
            dowlonad_delays = requests.get(self.url_delays.format(stop_id=self.stop_id))
            if dowlonad_delays.status_code == 200:
                delays_data = dowlonad_delays.json()
                with open("delays_list.json", "w") as delays:
                    json.dump(delays_data, delays)
                return delays_data
            else:
                print("Błąd pobierania danych")
                sys.exit(1)
        except Exception as error:
            print("Wystąpił błąd pobierania danych", str(error))
            sys.exit(1)