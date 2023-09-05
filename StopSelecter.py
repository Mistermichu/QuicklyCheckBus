import json
from Functions import download_data


class StopSelecter():
    def __init__(self, url_stops, url_stop_times):
        download_data(url_stops, "stops_list.json")
        download_data(url_stop_times, "stop_times_list.json")
        self.stop_data = {}
        self.timeTable = {}

    def get_stop_data(self):
        key_error = True
        while key_error:
            user_stop_name = str(input("Podaj nazwę przystanku: "))
            with open("stops_list.json", "r") as stops:
                stops_data = json.load(stops)
            for stop_name in stops_data:
                if stop_name["stopName"] == user_stop_name:
                    key_error = False
                    self.stop_data = {
                        "stopName": stop_name['stopName'],
                        "stopId": stop_name['stopId'],
                        "zoneId": stop_name['zoneId']
                    }
                    return
            print("Nie znalezniono przystanku. Spróbuj ponownie")

    def stop_time_table(self):
        with open("stop_times_list.json", "r") as stop_time_table:
            time_table = json.load(stop_time_table)
        for departure in time_table:
            if departure["stopId"] == self.stop_data["stopId"]:
                tripId = departure.get("tripId")
                departureTtime = departure.get("departureTime")
                self.timeTable[tripId] = {
                    "departureTime": departureTtime
                }
