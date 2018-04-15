from sha import sha
import socket

message = "Cant be tampered"
hashval = sha(message)



s = socket.socket()
s.bind(('',12346))
s.listen(5)

while True:
  c,add = s.accept()
  c.send(message+'?'+hashval)
  c.close()
  

