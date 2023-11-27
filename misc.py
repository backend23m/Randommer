import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        endpoint = "Misc/Cultures"
        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, headers=headers)

        return response.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
            url : https://randommer.io/api/Misc/Random-Address
        '''
        endpoint = "Misc/Random-Address"
        url = self.get_url() + endpoint

        payload = {
            'number' : number,
            'culture': culture
        }

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, params=payload, headers=headers)

        return response.json()

m = Misc()
token = '9174cdd006f046029c4def5446299088'
print(m.get_random_address(token, 998))