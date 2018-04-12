# Binary Search & Quick Sort

import unittest
from random import randint
import threading
import xml.etree.ElementTree as et


class XMLreader(unittest.TestCase):
  @staticmethod
  def readfile(filename):
    tree = et.parse(filename)
    root = tree.getroot()
    return [int(x) for x in root.text.split()]
    
  def test_positive(self):
    self.assertEqual(self.readfile('test.xml'),[10,20,30,40,50])
    
  def test_negative(self):
    self.assertRaises(IOError,lambda : self.readfile('dummy.txt'))
    

    
  

class List(unittest.TestCase):
  _mylist = []

  def set_list(self,l):
    self._mylist = l

  def qs(self):
    self._qs(0,len(self._mylist)-1)
  
  def _qs(self,low,high):
    if high <= low :
      return
    split = self._partition(low,high)
    threading.Thread(self._qs(low,split-1)).start()
    threading.Thread(self._qs(split+1,high)).start()
    #threading.Thread.getname()
    
  def bs(self,key):
    return self._bs(0,len(self._mylist)-1,key)
    
  def _bs(self,low,high,key):
    if low > high:
      return -1
    mid = (low + high)/2
    if self._mylist[mid] > key:
      return self._bs(low,mid-1,key)
    elif self._mylist[mid] < key:
      return self._bs(mid+1,high,key)
    else:
      return mid
   
  def __str__(self):
    return " ".join(str(x) for x in self._mylist)
    
  def _swap(self,i1,i2):
    assert(i1<len(self._mylist) and i2<len(self._mylist)),"Index Out of Bounds"
    temp = self._mylist[i1]
    self._mylist[i1] = self._mylist[i2]
    self._mylist[i2] = temp

  def _partition(self,low,high):
    pivot = self._mylist[low]
    left = low+1
    # Note: In python For loop Last Value Not included
    for i in range(low+1,high+1):
      if self._mylist[i] < pivot:
        self._swap(left,i)
        left +=1
    left-=1
    self._swap(low,left)
    return left
    
  def check_sorted(self): 
    for i,j in zip(self._mylist[:-1],self._mylist[1:]):
      if i > j :
        return False
    return True
    
  def test_swap(self):
    self._mylist = [1,2,3]
    self._swap(1,2)
    self.assertEqual(self._mylist,[1,3,2])
    self._swap(1,1)
    self.assertEqual(self._mylist,[1,3,2])
    
  def test_asending(self):
    self._mylist = [1,2,3]
    self.qs()
    self.assertTrue(self.check_sorted())
    
  def test_descending(self):
    self._mylist = [1,2,3]
    self._mylist = self._mylist[::-1]
    self.qs()
    self.assertTrue(self.check_sorted())
    
  def test_sorting(self):
    for i in range(100):
      self._mylist = [randint(0,1023) for i in range(randint(1,100))]
      self.qs()
      self.assertTrue(self.check_sorted())
      
  def test_bs(self):
    self._mylist = [1,2,3,4,5]
    self.assertEqual(2,self.bs(3))
    self.assertEqual(-1,self.bs(7))
    for i in range(100):
      self._mylist = [randint(0,1023) for i in range(randint(1,100))]
      self._mylist = list(set(self._mylist))
      self.qs()
      self.assertTrue(self.check_sorted())  
      index = randint(0,randint(0,len(self._mylist)-1))
      self.assertEqual(index,self.bs(self._mylist[index]))
      
  def runTest(self):
    pass

ml = List()
ml.set_list(XMLreader.readfile('test.xml'))
ml.qs()
print ml
print "Bin Srch 10", ml.bs(10)



if __name__ == "__main__":
  unittest.main()

  


     
      
      
    
    
    

	
