import requests
import json
from time import sleep
from random import randint
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from requests_tor import RequestsTor
from processing.models import Organization
import uuid

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


with open('rerion_list.txt', mode='r') as f:
    region_list = f.read().split(',')


rt = RequestsTor(tor_ports=(9050,), tor_cport=9051, password='password')
regionUl = '20'
url = 'https://pb.nalog.ru/search-proc.json'
flag = True

def get_company_details(method, token, id=None):
    url = 'https://pb.nalog.ru/company-proc.json'
    data = {'method': method,
            'token': token,
            'id': id}
    print(data)
    r = rt.post(url=url, data=data)
    print(r.text)
    print('THE R: ', r)
    j_company_details = json.loads(r.text)
    print('=====')
    print('j_company_details ', j_company_details)
    return j_company_details

region_list = ['77']

for zone in region_list:
    page = 1
    while flag:
        data = {'mode': 'search-ul',
                'regionUl': zone,
                'page': page,
                'pageSize': '100'}
        r = rt.post(url=url, data=data)
        print(r.text)
        jr = json.loads(r.text)
        print('JR DATA: ', jr)

        for item in jr['ul']['data']:
            print('ITEM ', item, type(item))
            get_request = get_company_details('get-request', item['token'])
            company_details = get_company_details('get-response', get_request['token'], id=get_request['id'])
            # try:
            Organization.objects.create(yearcode=item.get('yearcode'),
                                        periodcode=item.get('yearcode'),
                                        inn=item.get('inn'),
                                        ogrn=company_details['vyp']['ОГРН'],
                                        regionname=item.get('regionname'),
                                        namep=item.get('namep'),
                                        namec=item.get('namec'),
                                        invalid=item.get('invalid'),
                                        okved2=item.get('okved2'),
                                        okved2name=item.get('okved2name'),
                                        token=item.get('token'),
                                        other_data=company_details,
            )
            # except Exception as e:
            #     with open('error.log', mode='a') as f:
            #         f.write(str(e) + '\n')
        page += 1
        flag = jr['ul']['hasMore']
