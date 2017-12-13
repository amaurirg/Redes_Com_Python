#!/usr/bin/env python 3
# Servidor e cliente UDP na interface de loopback (localhost)
# Nesse programa o client não verifica se a resposta veio do servidor
# No final do programa tem um script e uma explicação

import argparse, socket
from datetime import datetime


MAX_BYTES = 65535


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    print('Listening at {}'.format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        print(data)
        print(address)
        text = data.decode('ascii')
        print(text)
        print('The client at {} says {}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        print(data)
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)    #Danger
    text = data.decode('ascii')
    print('The server {} replied {}'.format(address, text))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)


"""
Suponhamos que você seja um invasor que quisesse forjar a resposta do servidor,
poderia enviar esse script de um prompt.
Suspenda o server com CTRL+Z e envie uma requisição de client. Ele aguardará a resposta.
Faça esse script no prompt para enviar a resposta ao client.

>>> import socket
>>> sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>> sock.sendto('FAKE'.encode('ascii'), ('127.0.0.1', 39692))

O client receberá essa resposta achando que é do servidor.

Agora digite fg no terminal onde está suspenso o server para o servidor voltar a aguardar requisições.
Como o client já enviou e recebeu resposta FAKE, ele estará fechado e não receberá resposta do servidor.
"""
