#!/usr/bin/env python3
# Informa Latitude e Longitude usando API do Google com socket e urllib

from socket import socket
from urllib.parse import quote_plus


request_text = """
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.0\r\n
Host: maps.google.com:80\r\n
User-Agent: search4.py (Foundations of Python Network Programming)\r\n
Connection: close\r\n
\r\n
"""


def geocode(address):
    sock = socket()
    sock.connect(('maps.google.com', 80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))


if __name__ == '__main__':
    # geocode('Avenida Brasil, 1000, SP')
    geocode('207 N. Defiance St, Archbold, OH')