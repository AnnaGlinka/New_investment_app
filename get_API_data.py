from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class APIError(Exception):

    def __init__(self, _response):
        self._status_code = _response.status_code
        self._error_text = json.loads(_response.text)
        self._error_message = self._error_text['status']['error_message']
          
        
    def __str__(self):
        return f"APIError: status={self._status_code}\n{self._error_message}" 


class APIdataGetter:
    
    def get_API_data(self, url:str, parameters:dict={}, headers:dict={}) -> dict:

        #print(parameters)
        
        self.url = self
        self.parameters = parameters
        self.headers = headers

        session = Session()
        session.headers.update(headers)
        try:
            _response = session.get(url, params=parameters)
            #print(_response.status_code)
            if _response.status_code != 200:
                raise APIError(_response)
                
            data = json.loads(_response.text)
            return data
    
        except (APIError, ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)