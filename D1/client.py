from sha import sha
import socket

c = socket.socket()
c.connect(('localhost',12346))
message,hashval = c.recv(1000).split('?')

if sha(message)==hashval:
  print "Integrity maintained"
  
else:
  print "Message Tampered"

