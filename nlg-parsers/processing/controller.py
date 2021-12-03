import socket
import docker
import json
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from requests_tor import RequestsTor
from processing.models import Organization
from random import randint as ri
from multiprocessing import Pool

pool = Pool()
client = docker.from_env()
with open('rerion_list.txt', mode='r') as f:
    region_list = f.read().split(',')


class Broker:
    def __init__(self, region_list, pages_step):
        self.region_list = region_list
        self.current_region = region_list[0]
        self.pages_step = pages_step
        self.containers_count = pages_step * 2
        self.region_parsed = False
        self.cont_list = []
        self.region_has_more = True
        self.ports = []
        self.cports = []
        self.ports_in_use = []
        self.cports_in_use = []

    def get_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    def containers_create(self):
        for i in range(0, self.containers_count, 2):
            port = 9050 + i
            self.ports.append(port)
            cport = 9051 + i
            self.cports.append(cport)
            client.containers.run(image='1dabd7c7c596',
                                  ports={'9050/tcp': port, '9051/tcp': cport},
                                  detach=True,
                                  remove=True)

    def get_headers(self):
        headers_list = [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36']

        headers = {"User-Agent": headers_list[ri(0, 7)]}
        return headers

    def get_company_details(self, method, token, rt, id=None):
        url = 'https://pb.nalog.ru/company-proc.json'
        data = {'method': method,
                'token': token,
                'id': id}
        try:
            r = rt.post(url=url, data=data, headers=self.get_headers)
        except Exception as e:
            print('THERE IS ERROR WHILE GETTING DETAILS ======== ', e)
            rt.new_id()
            r = rt.post(url=url, data=data, headers=self.get_headers)
        j_company_details = json.loads(r.text)
        return j_company_details

    def get_tor_request(self):
        port = self.ports.pop()
        self.ports_in_use.append(port)
        cport = self.ports.pop()
        self.cports_in_use.append(cport)
        return RequestsTor(tor_ports=(port, ), tor_cport=cport, password='password')

    def create_organization(self, page):
        rt = self.get_tor_request()
        url = 'https://pb.nalog.ru/search-proc.json'
        page = page
        print(f'PAGE ======== {page}')
        headers = self.get_headers()
        data = {'mode': 'search-ul',
                'regionUl': '77', #self.current_region,
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
            print('CNT NUMBER IS  ====== ', str(cnt))
            print('ITEM ', item, type(item))
            headers = self.get_headers()
            get_request = self.get_company_details('get-request', item['token'], rt=rt)
            company_details = self.get_company_details('get-response', get_request['token'],
                                                  id=get_request['id'], rt=rt)

            if get_request or (get_request.get('ERROR') or company_details.get('ERROR')):
                print("THERE IS AN A CAPTCHA!!! so we have change identity/")
                rt.new_id()
                get_request = self.get_company_details('get-request', item['token'])
                company_details = self.get_company_details('get-response', get_request['token'],
                                                      id=get_request['id'])

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
            if jr['ul']['hasMore'] == 'false':
                break


    def start_parse(self):
        # self.containers_create()
        for region in self.region_list:
            print('CURRENT_REGION ====== ', region)
            pool.map(self.create_organization, [x for x in range(1, 6)])


region_list = ['77']
b = Broker(region_list=region_list, pages_step=5)
# pool.map(b.create_organization, [x for x in range(1, 6)])
b.containers_create()
b.create_organization(page=1)




