import requests
import json
import sys
from datetime import datetime


class Delays:
    def __init__(self, url_delays, stop_id):
        self.url_delays = url_delays
        self.stop_id = stop_id
        self.list = self.delays_list()

    def delays_list(self):
        try:
            dowlonad_delays = requests.get(
                self.url_delays.format(stop_id=self.stop_id))
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

    def get_delay_data(self, route_id, departure_time, trip_data, TimeTable, trip_id):
        for delay_data in self.list["delay"]:
            delay_route_id = delay_data.get("routeId")
            delay_departure = delay_data.get("theoreticalTime") + ":00"
            delay_estimated = delay_data.get("estimatedTime") + ":00"

            today = datetime.today()

            hour, minute, second = map(int, delay_estimated.split(':'))
            delay_estimated = today.replace(
                hour=hour, minute=minute, second=second)

            hour, minute, second = map(int, delay_departure.split(':'))
            delay_departure = today.replace(
                hour=hour, minute=minute, second=second)

            delay_vehicle = delay_data.get("vehicleCode")
            if route_id == delay_route_id and departure_time == delay_departure:
                trip_data["estimatedTime"] = delay_estimated
                trip_data["vehicleCode"] = delay_vehicle
                TimeTable[trip_id] = trip_data
