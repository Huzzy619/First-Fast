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

    async def get_feeds(self):
        """
        Get feed
        """
        url = self.base_url+'/feeds'
        response = await requests.get(url=url, headers=self.s_header)

        return response.json()

    async def create_feed(self, data):
        """
        Create Feed
        """
        url = self.base_url+'/feeds'
        response = await requests.post(url=url, headers=self.header, data=data)

        return response.json()

    async def delete_feed(self, feed_id):
        """
        Create Feed
        """
        url = self.base_url+f'/feeds/{feed_id}'
        response = await requests.delete(url=url, headers=self.header)

        return response.json()
