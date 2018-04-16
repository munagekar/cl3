import time

class LCG:
  a = 0
  c = 0
  m = 0
  seed = 0
  def __init__(self,seed=None,a=12345,c=11,m=2**32):
    self.a =a
    self.c =c
    if seed is None:
      seed = time.time() % m
    else:
      self.seed = seed % m
    self.m = m
    
  def gen(self):
    self.seed = (self.a*self.seed + self.c) % self.m
    return self.seed

