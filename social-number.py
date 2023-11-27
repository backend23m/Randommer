import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
            url =  https://randommer.io/api/SocialNumber
        '''
        endpoint = "SocialNumber"
        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key" : api_key
        }

        response = requests.get(url, headers=headers)

        return response.json()
    
s_num = SocialNumber()
print(s_num.get_SocialNumber('9174cdd006f046029c4def5446299088'))
        
