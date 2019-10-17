# /usr/bin/python

from select import select
import socket

#a, b, c = select([], [], [])

'''
import select
a, b, c = select.select([], [], []) 
a : ne pas rester bloque, client + socket serv
b : send dans lequel on peut ecrire
c : event exceptionnel
'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to local port
sock.bind(('127.0.0.1',1234))
sock.listen(10)
conn, addr = sock.accept()
print("CONNECT %r" % (addr,))
while True:
    #print(repr(conn.recv(4096)))
    data = conn.recv(4096)
    # len =
    #data += conn.recv(len)
    conn.send(data)
    if not data:
        break
    print(repr(data))
