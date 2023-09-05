import requests
import json
import sys


def download_data(url, file_name):
    try:
        dowlonad_data = requests.get(url)
        if dowlonad_data.status_code == 200:
            file_data = dowlonad_data.json()
            with open(file_name, "w") as data:
                json.dump(file_data, data)
        else:
            print("Błąd pobierania danych")
            sys.exit(1)
    except Exception as error:
        print("Wystąpił błąd pobierania danych", str(error))
        sys.exit(1)


def assign_data(file_name):
    with open(file_name, "r") as data_list:
        file_data = json.load(data_list)
    return file_data
