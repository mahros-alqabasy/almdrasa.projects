# FILE: src/lib/stack/stack.py

from typing import TypeVar, Generic


"""doc.src.libs.stack
    Purpose:
      - i have implemented this because i need it in history, and to able user to redo a move.
"""


T = TypeVar('T')

class Stack(Generic[T]):
  _stack:list[T]
    
  def __init__(self):
    self._stack:list[T] = []
  

  def isEmpty(self):
    return self.length() == 0
    
  def isNotEmpty(self):
    return not self.isEmpty()
  
  def length(self):
    return len(self._stack)
  
  def top(self)->T:
    if self.isEmpty():
      return None  
    return self._stack[-1]
  
  def pop(self)->T:
    if self.isEmpty():
      return None
  
    return self._stack.pop()

  def push(self, value:T)->T:
    self._stack.append(value)
    return value
    
  def __str__(self):
    return f"Stack(length={self.length()}{f', top={self.top()}' if not self.isEmpty() else ''})"