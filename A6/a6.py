import string
class InvalidKeyException(Exception):
  pass
class InvalidMode(Exception):
  pass
  
class Cipher:
  
  @staticmethod
  def numeric_key(st):
    st =st.strip().lower()
    return [ord(x)-ord('a') for x in list(st)]
    
  @staticmethod
  def caesar(st,key,mode='encrypt'):
    st= st.lower()
    if mode not in ['encrypt','decrypt']:
      raise InvalidMode("Mode must be encrypt or decrypt")
    if key <0 or key > 25:
      raise InvalidKeyException("Key must be between 0 and 25")
    return st.translate(Cipher.table(key,mode))
  
  @staticmethod
  def table(key,mode):
    assert (mode in ['encrypt','decrypt']),"Invalid Mode"
    alpha = string.ascii_lowercase
    salpha = alpha[key:]+alpha[:key]
    if mode == 'encrypt':
      return string.maketrans(alpha,salpha)
    return string.maketrans(salpha,alpha)
    
  @staticmethod
  def vignere(st,keystr,mode='encrypt'):
    st = st.strip().lower()
    l = len(st)
    keys = Cipher.numeric_key(keystr)
    tables = [Cipher.table(key,mode) for key in keys]
    return "".join([c.translate(tables[i%l]) for i,c in enumerate(st)])
    
       
cipher =  Cipher.caesar('azb',1,mode='encrypt')
print Cipher.caesar(cipher,1,mode='decrypt')

cipher =  Cipher.vignere('azb','abc',mode='encrypt')
print cipher
print Cipher.vignere(cipher,'abc',mode='decrypt')
