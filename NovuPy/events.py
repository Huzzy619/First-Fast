import requests
from decouple import config
from fastapi import HTTPException, status

class Events:
    base_url = 'https://api.novu.co/v1'

    # simple header with just Api_key
    # declare api_key in .env file
    s_header = {'Authorization': 'ApiKey' + config('NOVU_API_KEY')}

    headers = {
        'Authorization': 'ApiKey'+config('NOVU_API_KEY'),
        'Content_Type': 'application/json'
    }

    def __init__(self) -> None:

        pass

    async def get_messages(self, **kwargs):
        """
        Returns a list of messages, could paginate using the `page` query parameter
        """
        url = self.base_url + self.base_url + f'/messages'
        response = await requests.get(url=url, headers=self.s_header, params=kwargs)

        return response.json()

    async def delete_message(self, message_id):
        """
        Deletes a message entity from the Novu platform
        """
        url = self.base_url + f'/messages/{message_id}'

        response = await requests.delete(url=url, headers=self.s_header)
        return response.json()

    async def trigger(self, event, data):
        """
        Trigger event is the main (and the only) way to send notification to subscribers. 
        The trigger identifier is used to match the particular template associated with it. 
        Additional information can be passed according the the body interface below.
        """
        url = self.base_url + '/events/trigger'

        try:
            data['name'] = event
            response = await requests.post(url=url, headers=self.headers, data=data)

        except:

            HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        return response.json()

    async def broadcast(self, event, body):
        """
        Trigger a broadcast event to all existing subscribers, could be used to send announcements, etc. 
        In the future could be used to trigger events to a subset of subscribers based on defined filters.
        """
        url = self.base_url + '/events/trigger/broadcast'

        try:
            body['name'] = event
            response = await requests.post(url=url, headers=self.headers, data=body)

        except:

            HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        return response.json()

    async def cancel_trigger(self, transaction_id):
        """
        Using a previously generated transactionId during the event trigger, 
        will cancel any active or pending workflows. 
        This is useful to cancel active digests, delays etc...
        """

        url = self.base_url + f'/events/trigger/{transaction_id}'

        response = await requests.delete(url=url, headers=self.s_headers)

        return response.json()