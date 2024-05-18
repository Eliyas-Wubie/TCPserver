import socket

IP="127.0.0.1"
PORT=2020
BUF=4000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,PORT))
s.listen(1)

c,a=s.accept()
hello="hello>"
c.send(hello.encode())
print ("IP: ", a)

while True:
    d=c.recv(BUF)
    print (d)
    m=input(">")
    c.send(m.encode())
c.close()
s.close()