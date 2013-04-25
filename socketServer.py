import socket

s = socket.socket()

host = socket.gethostname()
port = 6819
s.bind((host, port))

s.listen(5)
while True:
    c.addr = s.accept()
    print 'Got connection from', addr
    c.send('hello')
    c.close()
