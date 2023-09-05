from Functions import download_data, assign_data


class Routes:
    def __init__(self, url_routes):
        file_name = "routes_list.json"
        download_data(url_routes, file_name)
        self.list = assign_data(file_name)
