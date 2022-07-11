import requests


class LaunchGateway():
    url = "https://api.spacexdata.com/v3/launches"
    headers = {'Content-Type': 'application/json'}

    def get_data(self):
        response = requests.request("GET", self.url, 
                                   headers=self.headers)
        
        return response

    def get_data_invalid_params(self):
        params = {"launch_year": "invalid"}
        response = requests.request("GET", self.url, 
                                   headers=self.headers, params = params)

        return response

    def get_launchs_from_year(self, year):
        params = {"launch_year": year}
        response = requests.request("GET", self.url, 
                                   headers=self.headers, params = params)
        
        return response

    def get_launchs_from_site_id(self, site_id):
        params = {"site_id": site_id}
        response = requests.request("GET", self.url, 
                                   headers=self.headers, params = params)
        
        return response

        