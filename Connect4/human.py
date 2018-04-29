class Human():
  def __init__(self):
    self.attack = 0
    
  def play(self,node):
    print("Human turn!")
    while 1:
      print("Avaliable move: \n")
      for col,row in enumerate(node.frontier):
        if row!=None:
          print(str(row)+" "+str(col)+'\n')
      action = [int(x) for x in input("Your turn: ").split()]
      if node.frontier[action[1]]!=action[0]:
        print("Move is invalid!")
        continue
      break
    node.update_frontier(action[0],action[1])
    return (action[0],action[1])
    
  def win(self):
    print("Game over: Human win!")