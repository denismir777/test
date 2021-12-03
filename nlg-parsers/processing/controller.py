import socket
import docker

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



    def parse_page(self, page_number):
        for i in range(1, 101):
            pass


    def start_parse(self):
        self.containers_create()
        for page in self.pages_step:
            pass




