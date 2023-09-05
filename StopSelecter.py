import json
import datetime
from Functions import download_data
from Trips import Trips
from CalendarDates import CalendarDates
from Routes import Routes

URL_TRIPS = "http://api.zdiz.gdynia.pl/pt/trips"
URL_CALENDAR_DATES = "http://api.zdiz.gdynia.pl/pt/calendar_dates"
URL_ROUTES = "http://api.zdiz.gdynia.pl/pt/routes"


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
        trips = Trips(URL_TRIPS)
        for trip_id, trip_data in self.timeTable.items():
            for specific_trip_data in trips.list:
                if trip_id == specific_trip_data["tripId"]:
                    trip_data["routeId"] = specific_trip_data.get("routeId")
                    trip_data["serviceId"] = specific_trip_data.get(
                        "serviceId")
                    trip_data["tripHeadsign"] = specific_trip_data.get(
                        "tripHeadsign")
                    trip_data["tripHeadsign"] = trip_data["tripHeadsign"][:-3]
                    self.timeTable[trip_id] = trip_data
        calendar_date = CalendarDates(URL_CALENDAR_DATES)
        today = str(datetime.date.today()).replace("-", "")
        trip_to_remove = []
        for trip_id, trip_data in self.timeTable.items():
            service_id = trip_data.get("serviceId")
            trip_in_service = False
            for calendar_trips in calendar_date.list:
                id = calendar_trips.get("serviceId")
                if service_id == id:
                    service_day = calendar_trips.get("date")
                    if today == service_day:
                        trip_in_service = True
            if not trip_in_service:
                trip_to_remove.append(trip_id)
        print(f"Kursy do usunięcia: {trip_to_remove}")
        for id_to_remove in trip_to_remove:
            del self.timeTable[id_to_remove]
        routes = Routes(URL_ROUTES)
        for trip_id, trip_data in self.timeTable.items():
            route_id = trip_data.get("routeId")
            for route_data in routes.list:
                route_data_id = route_data.get("routeId")
                if route_id == route_data_id:
                    route_short_name = route_data.get("routeShortName")
                    trip_data["routeShortName"] = route_short_name
