import asyncio
import time
from dataclass import DataClass
from forbes import ForbesVip
from celeb import CelebrityApi
search_info = {
    "name": "fola",
    "age": 86,
    "occupation": "influencer",
    "email": "fkh@gmail.com",
    "gender": "male"
}



def TwitterSrvfn(search_info):
    return search_info


def FacebookSrvfn(search_info):
    return search_info


def LinkedinSrvfn(search_info):
    return search_info


class Process():

    def __init__(self, search_info):
        self.search_info = search_info

    def main(self):
        services_response = asyncio.run(self.get_service_response())
        response = DataClass(services_response, **self.search_info)
        data_response = response.initiate()
        return data_response

    async def runService(self, Service):

        return Service().process(self.search_info)

    async def get_service_response(self):
        linked_s = await asyncio.gather(self.runService(CelebrityApi)) #self.runService(ForbesVip)
        # return [linked_s, facebook_s] 
        return linked_s

        #[twitter_s, facebook_s, linked_s]
        # twitter_s, facebook_s,


res = Process(search_info)
print(res.main())
x = time.perf_counter()
y = time.perf_counter() - x
print(y)

# self.runService(TwitterSrvfn),
                                        # self.runService(FacebookSrvfn), 
                                        # self.runService(LinkedinSrvfn)