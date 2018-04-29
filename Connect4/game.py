from node import Node
import numpy as np

class Game():
  
  def __init__(self,p0,p1):
    self.node = None
    self.p0 = p0
    self.p1 = p1
    self.p0.attack = 0
    self.p1.attack = 1
    self.p0_score = 0
    self.p1_score = 0
  
  def draw_board(self,board):
    print("\t0\t1\t2\t3\t4\t5\t6")
    print("----------------------------------------------------------")
    for x in range(5,-1,-1):
      s = ""
      s += str(x)+"    |"+'\t'
      for y in range(7):
        s += str(board[x][y])+'\t'
      print(s)
  
  def is_game_over(self,player,move):
    board = self.node.board
    # check row
    for col in range(3):
      if not None in board[move[0]][col:(col+4)]:
        if sum(board[move[0]][col:(col+4)])==4*player:
          return True
    # check col
    if move[0]-3>=0:
      if sum([x[move[1]] for x in board[move[0]-3:move[0]+1]])==4*player:
        return True
    # check diag
    diff1 = move[0]+move[1]
    diff2 = move[0]-move[1]
    diag1 = 0
    diag2 = 0
    for row in range(6):
      if diff1>=row and diff1-row<7 and board[row][diff1-row]==player:
        diag1+=1
      else:
        diag1 = 0
      if row>=diff2 and row-diff2<7 and board[row][row-diff2]==player:
        diag2+=1
      else:
        diag2 = 0
      if diag1==4 or diag2==4:
        return True
    return False
    
  def game(self,show = False):
    p0 = self.p0
    p1 = self.p1
    # initialize board
    board = []
    for x in range(6):
      board.append([])
      for y in range(7):
        board[x].append(0)
    # initialize frontier
    frontier = []
    for i in range(7):
      frontier.append(0)
    # initialize node for player
    node = Node(board,frontier)
    self.node = node
    # initialize attack
    p0.attack = 1
    p1.attack = -1
      
    # choose first player
    p = np.random.random()
    if p<0.5:
      player = 1 
    else:
      player = -1
      
    # Play game until there is a winner
    step = 0
    while step!=42:
      print(node.frontier)
      if player==1:
        move = p0.play(node)
        self.draw_board(board)
      else:
        move = p1.play(node)
        self.draw_board(board)
      if self.is_game_over(player,move):
        if player==1:
          p0.win()
          self.p0_score+=1
        else:
          p1.win()
          self.p1_score+=1
        break
      player = 0-player
      step += 1
      if show:
        node.print_stat()
    if step==42:
      print("Game over: Draw!")
  
