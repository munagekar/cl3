# Ridicolously unoptimized code ahead

from random import randint
import hashlib
from math import floor
def is_prime(n):
  if n ==1 or n == 0:
    return False
  return all([n%i for i in range(2,int(floor(n**0.5))+1)])


def gen_p(q):
  assert(is_prime(q)),"Argument must be prime"  
  mul = 2
  while(True):
    p = mul* q + 1
    mul +=1
    if is_prime(p):
      return p
    
def mod_pow(base,exp,mod):
  ans =1
  for i in range(exp):
    ans = (ans*base)%mod
  return ans
  
def mod_inv(num,mod):
  for i in range(1,mod):
    if (num * i ) %mod == 1:
      return i
  raise Exception
      

def gen_g(p,q):
  for h in range(2,p-1):
    g = mod_pow(base = h,exp = (p-1)/q,mod = p)
    if g > 1:
      return g
  raise
  
def gen_keys(p,q,g):
  pr = randint(1,q-1)
  pu = mod_pow(base =g,exp =pr, mod =p)
  return pr,pu
  
def gen_hash(text):
  return int(hashlib.sha1(text).hexdigest(),16)
  
def gen_sign(Hm,p,q,g,pr):
  k = randint(2,q-1)
  kinv = mod_inv(num=k,mod=q)
  
  r = mod_pow(base=g,exp =k,mod =p) % q
  s = (kinv * (Hm + pr *r)) %q
  return r,s
  
def verify(Hm,s,r,p,q,g,pu):
  w = mod_inv(num=s,mod =q)
  u1 = (Hm*w) %q
  u2 = (r*w)%q
  v = mod_pow(base =g,exp =u1,mod=p)*mod_pow(base=pu,exp=u2,mod=p)
  v = (v%p)%q
  if v==r:
    return True
  return False
  
  
q = int(input("Enter the value for prime number q"))
p =gen_p(q)
print "Generated corresponding prime number is ",p
g= gen_g(p,q)
print "G value is:",g
print "Public Parameters Complete"
print "Begin Generation of Keys"
pr,pu = gen_keys(p,q,g)
print "Private Key:",pr
print "Public Key:",pu
print "Begin Generation of Signature"
msg = "test"
Hm = gen_hash(msg)
r,s =gen_sign(Hm,p,q,g,pr)
print "Begin Verification"
print "Verification:",verify(Hm,s,r,p,q,g,pu)
  
  

