import requests
import json
import sys


class CalendarDates:
    def __init__(self, url_calendar_dates):
        self.url_calendar_dates = url_calendar_dates
        self.dates = self.dates_list()

    def dates_list(self):
        try:
            dowlonad_dates = requests.get(self.url_calendar_dates)
            if dowlonad_dates.status_code == 200:
                dates_data = dowlonad_dates.json()
                with open("dates_list.json", "w") as dates:
                    json.dump(dates_data, dates)
                    return dates_data
            else:
                print("Błąd pobierania danych")
                sys.exit(1)
        except Exception as error:
            print("Wystąpił błąd pobierania danych", str(error))
            sys.exit(1)
