import requests
import json
import sys


class Routes:
    def __init__(self, url_routes):
        self.url_routes = url_routes
        self.routes = self.routes_list()
        self.route_data = {}

    def routes_list(self):
        try:
            dowlonad_routes = requests.get(self.url_routes)
            if dowlonad_routes.status_code == 200:
                routes_data = dowlonad_routes.json()
                with open("routes_list.json", "w") as routes:
                    json.dump(routes_data, routes)
            else:
                print("Błąd pobierania danych")
                sys.exit(1)
        except Exception as error:
            print("Wystąpił błąd pobierania danych", str(error))
            sys.exit(1)

    def get_route_data(self, route_id):
        with open("routes_list.json", "r") as routes:
            routes_data = json.load(routes)
        for route in routes_data:
            if route["routeId"] == route_id:
                self.route_data[route_id] = {
                    "routeShortName": route["routeShortName"]
                }
                return
