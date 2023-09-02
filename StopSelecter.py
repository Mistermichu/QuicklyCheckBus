import requests
import json
import sys

class StopSelecter():
    def __init__(self, url_stops) :
        self.url_stops = url_stops
        self.stops = self.stops_list()  
        self.stop_data = {}      

    def stops_list(self):
        try:
            dowlonad_stops = requests.get(self.url_stops)
            if dowlonad_stops.status_code == 200:
                stops_data = dowlonad_stops.json()
                with open("stops_list.json", "w") as stops:
                    json.dump(stops_data, stops)
            else:
                print("Błąd pobierania danych")
                sys.exit(1)
        except Exception as error:
            print("Wystąpił błąd pobierania danych", str(error))
            sys.exit(1)

    def get_stop_data(self):
        key_error = True
        while key_error:
            user_stop_name = str(input("Podaj nazwę przystanku: "))        
            with open("stops_list.json", "r") as stops:
                stops_data = json.load(stops)
            for stop_name in stops_data:
                if stop_name["stopName"] == user_stop_name:
                    key_error = False                                        
                    self.stop_data =  {
                        "stopName": stop_name['stopName'],
                        "stopId": stop_name['stopId'],
                        "zoneId": stop_name['zoneId']
                    }
                    return
            print("Nie znalezniono przystanku. Spróbuj ponownie")
                






    

