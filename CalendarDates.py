from Functions import download_data, assign_data


class CalendarDates:
    def __init__(self, url_calendar_dates):
        file_name = "dates_list.json"
        download_data(url_calendar_dates, file_name)
        self.list = assign_data(file_name)
