from heap_min import Heap_min
from heap_max import Heap_max
import copy

class Node():
  
  def __init__(self,board=None,frontier=None,heap_type=1):
    
    # board: 0 for None, 1 for Agent, -1 for Human
    self.board = board
    
    # available move at the frontier
    self.frontier = frontier
    
    # ordered alpha-beta pruning
    # find_max: 1 and find_min: 0
    self.value = -1
    self.heap_type = heap_type
    self.action = None
    if heap_type==1:
      self.children = Heap_max()
    else:
      self.children = Heap_min()
  
  def draw_board(self):
    board = self.board
    print("\t0\t1\t2\t3\t4\t5\t6")
    print("----------------------------------------------------------")
    for x in range(5,-1,-1):
      s = ""
      s += str(x)+"    |"+'\t'
      for y in range(7):
        s += str(board[x][y])+'\t'
      print(s)
  
  def print_stat(self):
    self.draw_board()
    print("Frontier: ",self.frontier)
    print("Value: ",self.value)
    print("Action: ",self.action)
    print("Heap_type: ",self.heap_type)
    
  def eval(self):
    # evaluate by power of two for potential block.
    # expected to suffer slightly is opponent is about to win
    # check row
    board = self.board
    value = 0
    for row in range(6):
      for col in range(3):
        if sum(board[row][col:col+4])%4==0:
            value += sum(board[row][col:col+4])*10000
        rows = board[row][col:col+4]
        if not 0 in rows and 1 in rows and -1 in rows:
          value += 4*self.heap_type
          continue
        value+=2**sum(rows)
    # check col
    for col in range(7):
      for row in range(2):
        if sum([x[col] for x in board[row:row+4]])%4==0:
            value += sum([x[col] for x in board[row:row+4]])*10000
        cols = [x[col] for x in board[row:row+4]]
        if not 0 in cols and 1 in cols and -1 in cols:
          value += 4*self.heap_type
          continue
        value+=2**sum(cols)
    # check diag
    for diff in range(0,3):
      diag1 = [board[row][diff+row] for row in range(6) if diff+row<7]
      diag2 = [board[row][7-diff-row] for row in range(0,3) if 7-diff-row<7]
      if len(diag1)>3:
        for x in range(0,len(diag1)-3):
          if sum(diag1[x:x+4])%4==0:
            value += sum(diag1[x:x+4])*10000
            return value
          if not 0 in diag1 and 1 in diag1 and -1 in diag1:
            value+=4*self.heap_type
            continue
          value+=2*sum(diag1[x:x+4])
      if len(diag2)>3:
        for x in range(0,len(diag1)-3):
          if sum(diag2[x:x+4])%4==0:
            value += sum(diag2[x:x+4])*10000
            return value
          if not 0 in diag2 and 1 in diag2 and -1 in diag2:
            value += 4*self.heap_type
            continue
          value+=2*sum(diag2[x:x+4])
    self.value = value
    return value
    
  # produce children node to minimax dfs
  def produce(self,row,col):
    board = copy.deepcopy(self.board)
    frontier = self.frontier[:]
    heap_type = self.heap_type
    child = Node(board, frontier, heap_type)
    child.update_frontier(row,col)
    #child.print_stat()
    return child
  
  # Update current node into new state, use moves by either Agent or Human
  def update_frontier(self,row,col):
    if self.frontier[col]<5:
      self.frontier[col]+=1
    elif self.frontier[col]==5:
      self.frontier[col] = None
    self.board[row][col]=self.heap_type
    self.heap_type = -self.heap_type
    if self.heap_type == -1:
      self.children = Heap_min()
    else:
      self.children = Heap_max()
    self.action = (row,col)