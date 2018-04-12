from flask import Flask,render_template,request
from math import log,ceil
import random


app = Flask(__name__)


@app.route('/')
def homepage():
  return render_template('index.html')
  
@app.route('/',methods=['POST'])
def process():
  n1 = int(request.form['t1'])
  n2 = int(request.form['t2'])
  ans = Booth(n1,n2).mul()
  return "Anwer is "+str(ans)
  


def bitcal(num):
    return int(ceil(log((num+1),2))+1)
    
def bitstrip(num,l):
    return num & ((2 ** l) -1)

class Booth:
  # a* b
  a = 0
  ca =0
  b = 0
  # Lengths for a & b
  la = 0
  lb = 0
  # Accumulator + Multiplier + q1
  ans = 0
  
  def __init__(self,a,b):
    self.a =a
    self.b =b
    self.la = bitcal(a)
    self.lb = bitcal(b)
    self.ans = b << 1
    self.ca = bitstrip((~a)+1,self.la) 
    
  def mul(self):
    for i in range(self.lb):
      self._bop()
    return self.ans>>1
  
  def _bop(self):
    flag = self.ans & 3
    if flag == 2:
      self._sub()
    elif flag == 1:
      self._add()
    self._rshift()
    
  def _add(self):
     self.ans = self.ans + (self.a<<(self.lb+1))
     self.ans = bitstrip(self.ans,self.la+self.lb+1)
    
  def _sub(self):
    self.ans = self.ans + (self.ca<<(self.lb+1))
    self.ans = bitstrip(self.ans,self.la+self.lb+1)

    
  def _rshift(self):
    if self.ans & 2**(self.la + self.lb) == 0:
      self.ans=self.ans >> 1
    else:
      self.ans = self.ans >> 1
      self.ans += 2**(self.la + self.lb)
      

b = Booth(7,3)
print b.mul()

'''
for i in range(100):
  a = random.randint(0,1024)
  b = random.randint(0,1024)
  if a*b != Booth(a,b).mul():
    print "Error"
'''
    
    
if __name__=='__main__':
  app.run('localhost',port = 1234,debug=True)

  
