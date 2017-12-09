#!/usr/bin/env python3
# Convertendo um nome de host em um endereço IP com socket

import socket


if __name__ == '__main__':
    hostname = 'www.python.org'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))
