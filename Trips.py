from Functions import download_data, assign_data
import json


class Trips:
    def __init__(self, url_trips):
        file_name = "trips_list.json"
        download_data(url_trips, file_name)
        self.list = assign_data(file_name)

    def get_trips_list(self):
        with open("trips_list.json", "r") as trips_list:
            trips_data = json.load(trips_list)
        return trips_data
