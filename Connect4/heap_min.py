import copy

class Heap_min():
  def __init__(self):
    self.h = []
    self.size = 0
    
  def leftChild(self,index):
    return index*2+1
  def rightChild(self,index):
    return index*2+2
    
  def hasLeftChild(self,index):
    return self.leftChild(index)<len(self.h) and self.leftChild(index)>-1
  def hasRightChild(self,index):
    return self.rightChild(index)<len(self.h) and self.rightChild(index)>-1
    
  def isLeaf(self,index):
    return not self.hasRightChild(index) and not self.hasLeftChild(index)
  def parent(self,index):
    return (index-1)//2
    
  def remove_head(self):
    head = copy.copy(self.h[0])
    self.h[0] = self.h[-1]
    self.h = self.h[:-1]
    self.down_heapify(0)
    self.size -= 1
    return head
    
  def down_heapify(self,index):
    if self.isLeaf(index):
      return
    if self.hasLeftChild(index) and self.h[self.leftChild(index)].value<self.h[index].value:
      if (self.hasRightChild(index) and self.h[self.leftChild(index)].value<self.h[self.rightChild(index)].value) or not self.hasRightChild(index):
          self.h[index], self.h[self.leftChild(index)] = self.h[self.leftChild(index)], self.h[index]
          self.down_heapify(self.leftChild(index))
    if self.hasRightChild(index) and self.h[self.rightChild(index)].value<self.h[index].value:
      if (self.hasLeftChild(index) and self.h[self.rightChild(index)].value<self.h[self.leftChild(index)].value) or not self.hasLeftChild(index):
        self.h[index], self.h[self.rightChild(index)] = self.h[self.rightChild(index)], self.h[index]
        self.down_heapify(self.rightChild(index))
    return
  
  def add(self,node):
    self.h.append(node)
    self.size += 1
    self.up_heapify(len(self.h)-1)
    
  def up_heapify(self,index):
    if index==0:
      return
    if self.h[index].value<self.h[self.parent(index)].value:
      self.h[index], self.h[self.parent(index)] = self.h[self.parent(index)], self.h[index]
      self.up_heapify(self.parent(index))
    return
