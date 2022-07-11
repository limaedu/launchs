import requests


class LaunchGateway():
    url = "https://api.spacexdata.com/v3/launches"
    headers = {'Content-Type': 'application/json'}

    def get_data_from_flight_number(self, flight_number):
        params = {"flight_number": flight_number}
        response = requests.request("GET", self.url, 
                                   headers = self.headers, params = params)
        
        return response



        