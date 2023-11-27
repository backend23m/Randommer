import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
            https://randommer.io/api/Phone/Generate
        '''
        endpoint = 'Phone/Generate'
        url = self.get_url() + endpoint

        params = {
            'CountryCode' : CountryCode,
            'Quantity': Quantity
        }

        head = {
            'X-Api-Key' : api_key
        }

        r = requests.get(url, params=params, headers=head)
        return r.json()
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = "Phone/IMEI"
        url = self.get_url() + endpoint

        p = {
            'Quantity': Quantity
        }

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, params=p, headers=headers)

        return response.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        endpoint = "Phone/IMEI"
        url = self.get_url() + endpoint

        p = {
            'telephone': telephone,
            'ContryCode': CountryCode
        }

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, params=p, headers=headers)

        return response.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        endpoint = "Phone/Countries"
        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, headers=headers)

        return response.json()

phone1 = Phone()
token = '9174cdd006f046029c4def5446299088'
print(phone1.get_countries(token))