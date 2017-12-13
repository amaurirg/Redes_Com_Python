#!/usr/bin/env python3
# Cliente e servidor TCP simples
# Enviam e recebem 16 octetos

import argparse, socket



def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data


class TCPserver:
    def server(self, interface, port):
        self.sock_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock_srv.bind((interface, port))
        self.sock_srv.listen(1)
        print('Listening at', self.sock_srv.getsockname())
        # while True:
        #     self.sc, self.sockname = self.sock_srv.accept()
        #     print('sc =', self.sc)
        #     print('We have accepted a connection from', self.sockname)
        #     print('  Socket name:', self.sc.getsockname())
        #     print('  Socket peer:', self.sc.getpeername())
        #     self.message = recvall(self.sc, 16)
        #     print('  Incoming sixteen-octet message:', repr(self.message))
        #     self.sc.sendall(b'Farewell, client')
        #     self.sc.close()
        #     print('  Reply sent, socket closed')


class TCPclient:
    def client(self, host, port):
        self.sock_cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_cl.connect((host, port))
        print('Client has been assigned socket name', self.sock_cl.getsockname())
        self.sock_cl.sendall(b'Hi there, server')
        reply = recvall(self.sock_cl, 16)
        print('The server said', repr(reply))
        self.sock_cl.close()


# if __name__ == '__main__':
#     choices = {'client': client, 'server': server}
#     parser = argparse.ArgumentParser(description='Send and receive over TCP')
#     parser.add_argument('role', choices=choices, help='which role to play')
#     parser.add_argument('host', help='interface the server listen at;'
#                                      'host the client sends to')
#     parser.add_argument('-p', metavar='PORT', type=int, default=1060,
#                         help='UDP port (default 1060')
#
#     args = parser.parse_args()
#     function = choices[args.role]
#     function(args.host, args.p)
