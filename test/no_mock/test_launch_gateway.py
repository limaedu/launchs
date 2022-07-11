import unittest
from launch_gateway import LaunchGateway

class LaunchGatewayTests(unittest.TestCase):

    def setUp(self):
        self.data_launch_gateway = LaunchGateway()
        
    
    def test_get_server_returns_response_200(self):
        response = self.data_launch_gateway.get_data()

        self.assertEqual(200, response.status_code)


    def test_get_returns_empty_when_params_invalid(self):
        response = self.data_launch_gateway.get_data_invalid_params()
        
        self.assertEqual(200, response.status_code)
        
        json_response = response.json()

        self.assertTrue(not json_response)

        
    def test_count_launches_2020(self):
        response = self.data_launch_gateway.get_launchs_from_year(
                   year= "2020")

        self.assertEqual(200, response.status_code)
        
        json_response = response.json()

        self.assertEqual(25,len(json_response))
        

    def test_count_launches_canaveral(self):
        response = self.data_launch_gateway.get_launchs_from_site_id(
                   site_id= "ccafs_slc_40")

        self.assertEqual(200, response.status_code)
        json_response = response.json()

        self.assertEqual(62, len(json_response))



