import xml.etree.ElementTree as et
import unittest
import itertools
from functools import reduce
from copy import deepcopy
from random import randint

def xmlreader(_file):
  tree = et.parse(_file)
  root = tree.getroot()
  x,y = str(root.text).strip().split(' ')
  return int(x),int(y)
  
class Queen(unittest.TestCase):
  _board = []
  _size = 0
  
  def set_size(self,s):
   self._size = s 
  
  def placequeen(self,pos):
    assert(self._checksafe(pos)),"Unsafe Position"
    self._board.append((pos))
 
  def _checksafe(self,pos1):
    for pos2 in self._board:
      if Queen.danger(pos1,pos2):
        return False
    return True
    
  @staticmethod
  def danger(pos1,pos2):
    y1,x1=pos1
    y2,x2=pos2
    if x1 == x2 or y1 ==y2:
      return True
    if ((x1 + y1) == (x2 + y2)) or ((x1-y1) ==(x2-y2)):
      return True
    return False
    
  @staticmethod
  def check_solved(board,size):
    if len(board) != size:
      return False
    for pos1,pos2 in itertools.combinations(board,2):
      if Queen.danger(pos1,pos2):
        return False
    return True
    
  def __repr__(self):
    return Queen.pprint(self._board)
    
  @staticmethod
  def pprint(board):
    strboard = [['.' for i in range(len(board))] for j in range(len(board))]
    for y,x in board:
      strboard[y][x] = 'Q'
    strboard = [str(''.join(row)) for row in strboard]
    strboard = reduce(lambda x,y : x + '\n' + y,strboard)
    return strboard
    
  def _solve(self):
    solved = []    
    self.solve(0,solved)
    return solved
    
  def solve(self,row,solved_boards):
    if row == self._size:
      solved_boards.append(deepcopy(self._board))
    prows = [x[0]for x in self._board]
    if row in prows:
      self.solve(row +1,solved_boards)
    else:
      for c in range(self._size):
        if self._checksafe((row,c)):
          self.placequeen((row,c))
          self.solve(row+1,solved_boards)
          self._board.remove((row,c))


  
  
  def test_correct(self):
    self._size = 8
    for i in range( 1):
      x=randint(0,7)
      y=randint(0,7)
      self._board=[(0,7)]
      boards = self._solve()
      for b in boards:
        self.assertTrue(Queen.check_solved(b,self._size))

  def runTest(self):
    pass
    
q = Queen()
q.set_size(8)
q.placequeen((5,0))
boards=q._solve()
for b in boards:
  print b
  print Queen.pprint(b)



if __name__ == "__main__":
  unittest.main()
 
    
      
