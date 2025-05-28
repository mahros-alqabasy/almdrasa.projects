# FILE: src/libs/queue/queue.py


"""doc.src.libs.queue
  
  Purpose:
    - I have implemented this queue because i need it in the players turns,
"""


class Queue:
  _list = []
  
  def __init__(self):
    pass
  
  def isEmpty(self):
    return len(self._list) == 0
  
  
  def enqueue(self, value):
    self._list.insert(0, value)
  
  def dequeue(self):
    if not self.isEmpty():
      return self._list.pop()
  
  def top(self):
    if not self.isEmpty():
      return self._list[-1]
  
  def bottom(self):
    if not self.isEmpty():
      return self._list[0]
  
  def shuffle(self):
    print('[WARNING!] Shuffle not implemented yet.')
    
  def length(self):
    return len(self._list)
  
  def __str__(self):
    return f"Queue(length={self.length()}{f', top={self.top()}, bottom={self.bottom()}' if self.length() > 0 else 'isEmpty=True'})"
  
