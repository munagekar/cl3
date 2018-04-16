from sha import sha
from lcg import LCG
import socket

c = socket.socket()
c.connect(('localhost',12347))
message,hashval = c.recv(1000).split('?')

if sha(message,LCG(123))==hashval:
  print "Integrity maintained"
  
else:
  print "Message Tampered"

