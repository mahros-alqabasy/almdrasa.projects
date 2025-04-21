# Created by Mahros

# dependencies
import tkinter as tk
from dataclasses import dataclass




@dataclass
class WindowConf:
  title:str
  size:tuple

  
@dataclass
class AppConf:
  window:WindowConf
  

# Gui
class Gui:
  def __init__(self, conf):
    self.root = tk.Tk()
    self.conf = conf

    # init
    self.init()


  # source code
  def init(self):
    # init window size
    self.__init_window_conf()

  
  def __init_window_conf(self):
    # set window title
    self.root.title(self.conf.window.title)

    # set window size and position
    size = self.conf.window.size
    width, height = size
    
    # set width, height, and center
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    
    # center it
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    self.root.geometry(f"{size[0]}x{size[1]}+{x}+{y}")  
    


  def run(self):
    self.root.mainloop()


  def close(self):
    self.root.destroy()
