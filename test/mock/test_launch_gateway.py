import unittest
from unittest.mock import patch, Mock
from launch_gateway import LaunchGateway
import json

class LaunchGatewayTests(unittest.TestCase):

    def setUp(self):
        self.data_launch_gateway = LaunchGateway()
        
    
    def test_mock(self):
        
        #Criando o patch do mock
        mock_patch = patch('launch_gateway.requests.get')

        #Usando um json mock
        with open("sample_json.json") as f:
            launchs = json.load(f)

        #Iniciando o patch do mock
        mock_get = mock_patch.start()

        #Configurando o mock para retornar status 200 e guardando o 1o lançamento
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = launchs
        
        #Mandando a requisição 
        response = self.data_launch_gateway.get_data_from_flight_number(1)

        mock_patch.stop()

        #Assertando a resposta da requisição e o json
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.json(),launchs)


    



