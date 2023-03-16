from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class GetAPIdata:
    
    def get_API_data(self, url:str, parameters:dict={}, headers:dict={}) -> dict:
        
        self.url = self
        self.parameters = parameters
        self.headers = headers

        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data
    
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)