# /usr/bin/python

from select import select
import socket
a, b, c = select([], [], [])

'''
import select
a, b, c = select.select([], [], []) 
a : ne pas rester bloque
b : send dans lequel on peut ecrire
c : event exceptionnel
'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind socket to local port
sock.bind(('127.0.0.1',1234))
sock.listen(10) #10 co en attente
conn, addr = sock.accept() #return conn, addr
print("CONNECT %r" % (addr,))
while True:
    '''
    print(repr(conn.recv(4096))) #je reçois 4K sur la socket conn
    
    data = conn.recv(4096)
    len = struct.unpack('>I', data)[0]
    data += conn.recv(len)
    '''
    data = conn.recv(4096)
    conn.send(data)
    if not data:
        break
    print(repr(data))
#repr(obj) returns a printable representational string of the given object.
#conn connexion attache au client
#addr adresse du client
#sock cote serv


