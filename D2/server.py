from sha import sha
from lcg import LCG
import socket

message = "Cant be tampered"
hashval = sha(message,LCG(123))



s = socket.socket()
s.bind(('',12347))
s.listen(5)

while True:
  c,add = s.accept()
  c.send(message+'?'+hashval)
  c.close()
  

