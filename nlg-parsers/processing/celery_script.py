import json
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from requests_tor import RequestsTor
from processing.models import Organization
from random import randint as ri
from multiprocessing import Pool

with open('rerion_list.txt', mode='r') as f:
    region_list = f.read().split(',')


rt = RequestsTor(tor_ports=(9050,), tor_cport=9051, password='password')


regionUl = '20'
url = 'https://pb.nalog.ru/search-proc.json'
flag = True

headers_list = ['Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36']


def get_heders(headers_list):
    headers = {"User-Agent": headers_list[ri(0, 7)]}
    return headers

def get_company_details(method, token, headers, id=None):
    url = 'https://pb.nalog.ru/company-proc.json'
    data = {'method': method,
            'token': token,
            'id': id}
    r = rt.post(url=url, data=data, headers=headers)
    j_company_details = json.loads(r.text)
    return j_company_details

region_list = ['77']
zone = '77'


def create_organization(page):
    page = page
    print(f'PAGE ======== {page}')
    flag = True
    while flag:
        headers = get_heders(headers_list)
        data = {'mode': 'search-ul',
                'regionUl': zone,
                'page': page,
                'pageSize': '100'}
        try:
            r = rt.post(url=url, data=data, headers=headers)
            jr = json.loads(r.text)
        except Exception as e:
            print("IP BANNED IN MAIN REQEST, CHANGING ID ", str(e))
            rt.new_id()
            r = rt.post(url=url, data=data, headers=headers)
            jr = json.loads(r.text)
        cnt = 0
        for item in jr['ul']['data']:
            print('CNT NUMBER IS  ====== ',  str(cnt))
            print('ITEM ', item, type(item))
            try:
                get_request = get_company_details('get-request', item['token'], headers=headers)
                company_details = get_company_details('get-response', get_request['token'], id=get_request['id'], headers=headers)
            except Exception as e:
                print(str(e) + "IP IS BANNED")
                rt.new_id()
                get_request = get_company_details('get-request', item['token'], headers=headers)
                company_details = get_company_details('get-response', get_request['token'], id=get_request['id'],
                                                      headers=headers)
            if get_request or (get_request.get('ERROR') or company_details.get('ERROR')):
                print("THERE IS AN A CAPTCHA!!! so we have change identity/")
                rt.new_id()
                get_request = get_company_details('get-request', item['token'], headers=headers)
                company_details = get_company_details('get-response', get_request['token'], id=get_request['id'],
                                                      headers=headers)

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
            cnt += 1
        page += 1
        if jr['ul']['hasMore'] == 'false':
            flag = False
            return 'Parsing completed!'


pool = Pool()
pool.map(create_organization, [x for x in range(1, 4)])
