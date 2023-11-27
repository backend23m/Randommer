import requests
from randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''

        url = f"{self.get_url()}Text/LoremIpsum"

        headers = {
            "X-Api-Key": api_key
        }

        parametrs = {
            "loremType": loremType,
            "type": type,
            'number': number
        }

        response = requests.get(url, params=parametrs, headers=headers)
        return response.json()
    
    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        url = f"{self.get_url()}Text/Password"

        headers = {
            "X-Api-Key": api_key
        }
        parametrs = {
            'length': length,
            'hasDigits': hasDigits,
            'hasUppercase': hasUppercase,
            'hasSpecial': hasSpecial
        }

        response = requests.get(url, params=parametrs, headers=headers)
        return response.json()
    
api_key = '9174cdd006f046029c4def5446299088'
t = Text()
print(t.generate_LoremIpsum(api_key, 'normal', 'words', 22))
