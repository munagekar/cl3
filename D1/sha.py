
def char2b(char):
  return "{0:08b}".format(ord(char))
  
def chunks(data,num):
  return [data[i:i+num] for i in range(0,len(data),num)]
  
def lr(num,b):
  return ((num << b) | (num >> (32-b))) & 0xffffffff

def sha (data):
  h0 = 0x67452301
  h1 = 0xEFCDAB89
  h2 = 0x98BADCFE
  h3 = 0x10325476
  h4 = 0xC3D2E1F0
     
  bits = "".join([char2b(char) for char in data])+"1"
  pbits = bits
  while(len(pbits)%512 !=448):
    pbits +='0'
  pbits +="{0:064b}".format(len(bits)-1)
  for c in chunks(pbits,512):
    words = chunks(c,32)
    assert (len(words)==16),"Wordlength is Wrong"
    w = [int(x,2) for x in words]
    for i in range(16,80):
      w.append(lr(w[i-3]^w[i-8]^w[i-14]^w[i-16],1))
      

      
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    
    for i in range(0,80):
      if i <=19:
        f = (b&c) | ((~b)&d)
        k = 0x5A827999
      elif i <=39:
        f = (b^c^d)
        k=0x6ED9EBA1
      elif i <=59:
        f = (b&c)|(b&d)|(c&d)
        k = 0x8F1BBCDC
      else:
        f = b^c^d
        k = 0xCA62C1D6
        
      temp = lr(a,5)+f+e+k+w[i] &0xffffffff
      
      e =d
      d =c
      c = lr(b,30)
      b = a
      a =temp
      
      
      
      
    
    h0 = h0 +a &0xffffffff 
    h1 = h1 +b&0xffffffff
    h2 = h2+c&0xffffffff
    h3 = h3 +d&0xffffffff
    h4 = h4 +e&0xffffffff
    
    
  return '%08x%08x%08x%08x%08x' % (h0,h1,h2,h3,h4)
      

    

