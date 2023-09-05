from Functions import download_data


class Trips:
    def __init__(self, url_trips):
        download_data(url_trips, "trips_list.json")
