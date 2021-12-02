import socket
import docker

client = docker.from_env()
with open('rerion_list.txt', mode='r') as f:
    region_list = f.read().split(',')


class Broker:
    def __init__(self, region_list, pages_step):
        self.current_region = region_list[0]
        self.pages_step = pages_step
        self.region_parsed = False
        self.cont_list = []

    def get_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    def containers_create(self, count, container):
        for i in self.pages_step:
            client.containers.run()


    def start_parse(self):
        pass


class Container:
    def __init__(self, port, cport):
        self.port = port
        self.cport = cport

    def run(self):
        pass

