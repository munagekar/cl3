from pymongo import MongoClient
from multiprocessing import Process,Lock
import time

client = MongoClient()
db = client.dbname


def readfood(phil):
  client = MongoClient()
  db = client.dbname
  doc = db.colname.find_one({'phil':phil})
  food = doc["food"]
  return food

class Phil(Process):
  name = ""
  food = ""
  lock1 = None
  lock2 = None
  
  
  def __init__(self,name,lock1,lock2):
    super(Phil,self).__init__()
    self.name = name
    self.food = readfood(name)
    self.lock1= lock1
    self.lock2 =lock2
    
  def run(self):
    while True:
      print self.name+" is thinking"
      time.sleep(2)
      print self.name+ " wants to eat"
      lock1.acquire()
      lock2.acquire()
      print self.name +" is eating"
      time.sleep(2)
      print self.name +" ate "+self.food
      lock2.release()
      lock1.release()
    
    
locks = [Lock() for i in range(5)]

for i in range(5):
  lockpair=[i,(i+1)%5]
  lock1 = locks[min(lockpair)]
  lock2 = locks[max(lockpair)]
  p=Phil(str(i),lock1,lock2)
  p.start()
  
while True:
  pass






