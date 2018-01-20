#!/usr/bin/env python3
# Cliente e servidor TCP simples
# Enviam e recebem 16 octetos

import argparse, socket
from time import sleep


def server_esp(data = b'acende'):
    sock_esp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_esp.connect(('192.168.0.40', 1060))
    sock_esp.sendall(data)
    sock_esp.close()


def recvall(sock, length):
    data = b''
    while len(data) < length:
        server_esp()
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    server_esp(b'apaga')
    return data


def server(interface, port):
    sock_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_srv.bind((interface, port))
    sock_srv.listen(2)
    print('Listening at', sock_srv.getsockname())

    while True:
        # server_esp()
        sc, sockname = sock_srv.accept()
        print('sc =', sc)
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())
        message = recvall(sc, 16)
        print('  Incoming sixteen-octet message:', repr(message))
        sc.sendall(b'Farewell, client')
        sc.close()
        print('  Reply sent, socket closed')


def client(host, port):
    # for i in range(90):
    sock_cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_cl.connect((host, port))
    print('Client has been assigned socket name', sock_cl.getsockname())
    sock_cl.sendall(b'Hi there, server')
    reply = recvall(sock_cl, 16)
    print('The server said', repr(reply))
    sock_cl.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listen at;'
                                     'host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1080,
                        help='UDP port (default 1060')

    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
