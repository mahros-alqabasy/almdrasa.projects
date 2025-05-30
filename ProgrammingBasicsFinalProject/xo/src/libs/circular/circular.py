from typing import Generic, TypeVar



"""NOTE: Not completed yet!

"""


T = TypeVar('T')

class Circular(Generic[T]):
  _circular:list
  _currentIndex:int
  def __init__(self):
    self._circular = []
    self._currentIndex=-1
  
  def length(self):
    return len(self._circular)
  
  def next(self, reset:bool=False) -> T:
    if self.length() == 0:
      return None
    
      
    self._currentIndex += 1
    return self._circular[self._currentIndex]
  
  def push(self, value:T):
    self._circular.append(value)
      
  def pop(self)->T:
    return self._circular.pop()



