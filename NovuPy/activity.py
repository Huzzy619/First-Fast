import requests
from decouple import config

class Activity:
    base_url = 'https://api.novu.co/v1'

    # simple header with just Api_key
    # declare api_key in .env file
    s_header = {'Authorization': 'ApiKey' + config('NOVU_API_KEY', '')}

    headers = {
        'Authorization': 'ApiKey'+config('NOVU_API_KEY'),
        'Content_Type': 'application/json'
    }

    def __init__(self) -> None:

        pass

    async def get_activity(self, **kwargs):
        """
        Get activity feed
        """
        url = self.base_url+'/activity'
        response = await requests.get(url=url, headers=self.s_header, params=kwargs )

        return response.json()

    async def get_activity_stats(self):
        """
        Get activity statistics
        """
        url = self.base_url+'/activity/stats'
        response = await requests.get(url=url, headers=self.s_header)

        return response.json()

    
    