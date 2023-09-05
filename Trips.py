from Functions import download_data
import json


class Trips:
    def __init__(self, url_trips):
        download_data(url_trips, "trips_list.json")
        self.list = self.get_trips_list()

    def get_trips_list(self):
        with open("trips_list.json", "r") as trips_list:
            trips_data = json.load(trips_list)
        return trips_data
