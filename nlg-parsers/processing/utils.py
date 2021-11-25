import requests
import json
from time import sleep
from random import randint
# from torrequest import TorRequest
# from multiprocessing.pool import ThreadPool
# from torpy.http.requests import tor_requests_session
from requests_tor import RequestsTor

def simple_get_data():
    for i in range(1, 100):
        r = requests.post('https://pb.nalog.ru/search-proc.json', data={'mode': 'search-ul',
                                                                        'regionUl': '03',
                                                                        'page': i,
                                                                        'pageSize': '100'})
        print(r.text)
        jr = json.loads(r.text)
        print(jr)
        sleep(randint(6, 15))


# def get_data_with_tor(region_number):
#     for i in range(1, 100):
#         with TorRequest() as tr:
#             response = tr.get('https://pb.nalog.ru/search-proc.json',
#                               password='1234',
#                               data={'mode': 'search-ul',
#                                     'regionUl': region_number,
#                                     'page': i,
#                                     'pageSize': '100'})
#             print(response.text)
#             tr.reset_identity()

# get_data_with_tor('03')
# with tor_requests_session() as s:  # returns requests.Session() object
#     links = ['https://pb.nalog.ru/search-proc.json']
#
#     with ThreadPool(3) as pool:
#         pool.map(s.get, links)
#         print(s.text)
# #
# rt = RequestsTor()
# rt.check_ip()

# r = rt.post('https://pb.nalog.ru/search-proc.json', data={'mode': 'search-ul',
#                                                                         'regionUl': '03',
#                                                                         'page': '250',
#                                                                         'pageSize': '100'})
# print(r.text)

rt = RequestsTor(tor_ports=(9050,), tor_cport=9051, autochange_id=1)
url = 'https://httpbin.org/anything'
r = rt.get(url)
rt.test()
print(r.text)