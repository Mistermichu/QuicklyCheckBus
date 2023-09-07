import json
from Functions import download_data, exclude_trips
from TimeConverter import convert_time
from Trips import Trips
from CalendarDates import CalendarDates
from Routes import Routes
from Delays import Delays
import datetime


URL_TRIPS = "http://api.zdiz.gdynia.pl/pt/trips"
URL_CALENDAR_DATES = "http://api.zdiz.gdynia.pl/pt/calendar_dates"
URL_ROUTES = "http://api.zdiz.gdynia.pl/pt/routes"
URL_DELAYS = "http://api.zdiz.gdynia.pl/pt/delays?stopId={stop_id}"


class StopSelecter():
    def __init__(self, url_stops, url_stop_times):
        download_data(url_stops, "stops_list.json")
        download_data(url_stop_times, "stop_times_list.json")
        self.stop_data = {}
        self.timeTable = {}
        self.updateTime = None

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
        # Downlad full Time Table for selected stop
        self.timeTable = {}
        with open("stop_times_list.json", "r") as stop_time_table:
            time_table = json.load(stop_time_table)
        for departure in time_table:
            if departure["stopId"] == self.stop_data["stopId"]:
                tripId = departure.get("tripId")
                departureTtime = departure.get("departureTime")
                self.timeTable[tripId] = {
                    "departureTime": departureTtime
                }
        # Exclude all passed departures and departures later than 1h
        exclude_trips(self.timeTable)
        # Assign routeID, serviceId, tripHeadsign
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
        # Exclude all trips not in service on specific day
        calendar_date = CalendarDates(URL_CALENDAR_DATES)
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        today = str(today).replace("-", "")
        yesterday = str(yesterday).replace("-", "")
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
                    elif yesterday == service_day:
                        departure_time = trip_data.get("departureTime")
                        if departure_time >= "24:00:00":
                            trip_in_service = True
            if not trip_in_service:
                trip_to_remove.append(trip_id)
        for id_to_remove in trip_to_remove:
            del self.timeTable[id_to_remove]
        # Convert Time
        convert_time(self.timeTable)
        # Exclude all passed departures and departures later than 1h after time convert
        exclude_trips(self.timeTable)
        # Get routeShortName
        routes = Routes(URL_ROUTES)
        for trip_id, trip_data in self.timeTable.items():
            route_id = trip_data.get("routeId")
            for route_data in routes.list:
                route_data_id = route_data.get("routeId")
                if route_id == route_data_id:
                    route_short_name = route_data.get("routeShortName")
                    trip_data["routeShortName"] = route_short_name
        # Assign current delays data
        delays = Delays(URL_DELAYS, self.stop_data["stopId"])
        self.updateTime = delays.list["lastUpdate"]
        for trip_id, trip_data in self.timeTable.items():
            route_id = trip_data.get("routeId")
            departure_time = trip_data.get("departureTime")
            delays.get_delay_data(route_id, departure_time,
                                  trip_data, self.timeTable, trip_id)
