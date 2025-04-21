# Created by Mahros


# imports
from src import gui
from src.components.editing_area import EditingArea
from src.components.status_bar import StatusBar
from src.components.tool_bar import ToolBar



class Editor(gui.Gui):
  def __init__(self):
    conf = gui.AppConf(
      window=gui.WindowConf(
        title="Editor",
        size=(800, 600)
      )
    )
    super().__init__(conf)

    # components
    self.tool_bar     = ToolBar(self.root, onSave=self.onSaveClicked, onOpen=self.onOpenClicked)
    self.editing_area = EditingArea(self.root)
    self.status_bar   = StatusBar(self.root)
    
    self.init_widgets()

  def onSaveClicked(self):
    # get the editor content
    content = self.editing_area.getValue()

    path = self.tool_bar.getFilePath()
    

    # save it to the tool_var.input_file-path
    try:
      file = open(path, "wt")
      file.write(content)
      file.close()
    except Exception as Error:
      self.status_bar.showMessage(f"{Error}")
      print(Error)


  def onOpenClicked(self):
    # get the file path
    # then read it's content 
    # then copy the conten to the editing area
    path = self.tool_bar.save_input.getFilePath()

  
    # read file content
    try:
      file = open(path, "rt")
      content = file.read()
      file.close()
      
    except Exception as Error:
      print(Error)
      self.status_bar.showMessage(f"{Error}")

    # clear  
    self.editing_area.clear()

    # put the string to it
    self.editing_area.insert('1.0', content)
    
  def init_widgets(self):
    # widgets
    # Arrange components using pack/grid/other layout managers
    self.tool_bar.pack(side="top", fill="x")
    self.editing_area.pack(side="top", fill="both", expand=True)
    self.status_bar.pack(side="bottom", fill="x")

  
