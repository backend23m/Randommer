import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        endpoint = "Finance/CryptoAddress/Types"
        url =  self.get_url() + endpoint
        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, headers = headers)

        return response.json()


    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        endpoint = "Finance/CryptoAddress"
        url = self.get_url() + endpoint

        params = {
            'cryptoType' : crypto_type
        }

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, params=params, headers=headers)

        return response.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        endpoint = "Finance/Countries"
        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
            url = https://randommer.io/api/Finance/Iban/{countryCode}
        '''
        endpoint = f"Finance/Iban/{country_code}"
        url = self.get_url() + endpoint

        params = {
            'countryCode' : country_code
        }

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, params=params, headers=headers)

        return response.json()

f = Finance()
print(f.get_iban_by_country_code('AL', '9174cdd006f046029c4def5446299088'))