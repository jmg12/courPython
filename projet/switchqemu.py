# /usr/bin/python

from select import select
import socket

'''
import select
a, b, c = select.select([], [], []) 
a (rlist wait until ready for reading): ne pas rester bloque, client + socket serv
b (wlist wait until ready for writing): send dans lequel on peut ecrire
c (xlist): event exceptionnel
'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to local port
'''
sock est la socket de server
'''
sock.bind(('127.0.0.1',1234))
sock.listen(10) #accept 1 client
conn, addr = sock.accept() # donne une adresse
print("CONNECT %r" % (addr,)) #lis data
while True:
    #print(repr(conn.recv(4096)))
    data = conn.recv(4)
    len = struct.unpack('>I', data)[0]
    data += conn.recv(len)
    #a, b, c = select([data], [], [] )
    conn.send(data)
    if not data:
        break
    print(repr(data))
