FROM ubuntu:latest

ENV TORNAME tor-0.4.6.8
RUN apt-get update
RUN apt-get install -y libwww-perl build-essential libevent-dev libssl-dev zlib1g zlib1g-dev
RUN GET https://www.torproject.org/dist/${TORNAME}.tar.gz | tar xz -C /tmp

RUN cd /tmp/${TORNAME} && ./configure
RUN cd /tmp/${TORNAME} && make
RUN cd /tmp/${TORNAME} && make install
RUN rm -rf /tmp/${TORNAME}

EXPOSE 9050
EXPOSE 9051
RUN echo "Log notice stdout" >> /etc/torrc
RUN echo "SocksPort 0.0.0.0:9050" >> /etc/torrc
RUN echo "ControlPort 0.0.0.0:9051" >> /etc/torrc
RUN echo "HashedControlPassword 16:5768EC564A78C998604707DCA086D97D67BE6F7A9A93101F6CFB566F58" >> /etc/torrc

CMD /usr/local/bin/tor -f /etc/torrc