# test heaps
from heap_max import Heap_max
from heap_min import Heap_min
from node import Node
from agent import Agent

def test_heap_max():
  print("test heap_max")
  h = Heap_max()
  a = Node()
  a.value = 12
  b = Node()
  b.value = 100
  c = Node()
  c.value = 34
  d = Node()
  d.value = 2
  h.add(a)
  h.add(b)
  h.add(c)
  h.add(d)
  print(h.remove_head().value)
  print(h.remove_head().value)
  print(h.remove_head().value)
  print(h.remove_head().value)
  
def test_heap_min():
  print("test heap_min")
  h = Heap_min()
  a = Node()
  a.value = 12
  b = Node()
  b.value = 100
  c = Node()
  c.value = 34
  d = Node()
  d.value = 2
  h.add(a)
  h.add(b)
  h.add(c)
  h.add(d)
  print(h.remove_head().value)
  print(h.remove_head().value)
  print(h.remove_head().value)
  print(h.remove_head().value)
  
# test Node
def test_eval():
  board =[[0,0,1,-1,-1,1,0],
          [0,0,0,-1,1,0,0],
          [0,0,0,-1,0,0,0],
          [0,0,0,-1,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]
  a = Node(board)
  print("Eval: ",a.eval())
  
def test_produce():
  board =[[0,0,0,1,1,1,1],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]
  frontier = [0,0,0,1,1,1,1]
  a = Node(board,frontier,1)
  b = a.produce(0,2)
  a.print_stat()
  b.print_stat()

# test agent
def test_minimax():
  agent = Agent(1)
  board =[[0,0,0,0,1,1,1],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]
  frontier = [0,0,0,1,1,1,1]
  a = Node(board,frontier,1)
  agent.play(a)
"""
# test human
def test_human_vs_human():
# test game
def test_agent_vs_agent():
def test_alternate_attack():
def test_game_over():
def test_replay():
"""