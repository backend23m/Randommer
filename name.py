import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        endpoint = "Name"
        url = self.get_url() + endpoint

        params = {
            'nameType': nameType,
            'quantity': quantity
        }

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, params=params, headers=headers)

        return response.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        endpoint = "Name/Suggestions"
        url = self.get_url() + endpoint

        params = {
            'startingWords': startingWords
        }

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, params=params, headers=headers)

        return response.json()
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        endpoint = "Name/Cultures"
        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, headers=headers)

        return response.json()

token = '9174cdd006f046029c4def5446299088'
n = Name()
print(n.get_name_cultures(token))