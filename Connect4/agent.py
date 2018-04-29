from heap_max import Heap_max
from heap_min import Heap_min
import copy
import time

class Agent():
  
  def __init__(self,depth=3):
    self.attack = 1
    self.depth = depth
  # alpha:value of max_node's neigh
  # beta: value of min_node's neigh
  
  def find_min(self,node,depth,alpha,beta):
    if depth==0:
      node.value = node.eval()
      return None, node.value
    min_node,min_value = None,10000000
    for col,row in enumerate(node.frontier):
      if not row==None:
        child_node = node.produce(row,col)
        _, child_node.value = self.find_max(child_node,depth-1,alpha,beta)
        node.children.add(child_node)
    while node.children.size>0:
      child_node = node.children.remove_head()
      child_node.print_stat()
      value = child_node.value
      if value<min_value:
        min_node,min_value = child_node,value
      if min_value<=beta:
        break
      if min_value<alpha:
        alpha = value
    return min_node, min_value
    
  def find_max(self,node,depth,alpha,beta):
    if depth==0:
      node.value = node.eval()
      return node, node.value
    max_node,max_value = None,-10000000
    for col,row in enumerate(node.frontier):
      if not row==None:
        child_node = node.produce(row,col)
        _, child_node.value = self.find_min(child_node,depth-1,alpha,beta)
        node.children.add(child_node)
    while node.children.size>0:
      child_node = node.children.remove_head()
      print('\n'+str(depth))
      child_node.print_stat()
      value = child_node.value
      if value>max_value:
        max_node,max_value = child_node,value
      if max_value>=alpha:
        break
      if max_value>beta:
        beta = value
    return max_node, max_value
    
  def search(self,node,alpha,beta):
    start_time = time.time()
    if self.attack:
      print("find_max")
      next_node,_ = self.find_max(node,self.depth,alpha,beta)
    else:
      print("find_min")
      next_node,_ = self.find_min(node,self.depth,alpha,beta)
    #next_node.print_stat()
    print("Search time: ",time.time()-start_time)
    return next_node.action
    
  def play(self,node):
    action = self.search(copy.deepcopy(node),-10000000,10000000)
    print(str(action[0])+" "+str(action[1])+'\n')
    node.update_frontier(action[0],action[1])
    return (action[0],action[1])
  
  def win(self):
    print('Game over: Agent win!')
