import tkinter as tk
from src.ui.style_manager import StyleManager
from dataclasses import dataclass

@dataclass
class WindowConf:
    title: str
    size: tuple

@dataclass
class AppConf:
    window: WindowConf

class Gui:
  def __init__(
      self, conf: AppConf,
      theme_path='themes/theme.json',
      component_styles_dir='themes/',
    ):
    self.root = tk.Tk()
    # self.root.wm_attributes('-zoomed', True)
    # self.root.wm_attributes('-fullscreen', True)
    self.root.configure(background= "#ffffff", borderwidth =2)
    self.conf = conf
    self.style_manager = StyleManager(theme_path, component_styles_dir)
    self.init()

  def init(self):
    self.__init_window_conf()
    self.__apply_global_theme()

  def __init_window_conf(self):
    width, height = self.conf.window.size
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    self.root.geometry(f"{width}x{height}+{x}+{y}")
    self.root.title(self.conf.window.title)

  def __apply_global_theme(self):
    theme = self.style_manager.get_theme()
    bg = theme.get("bg_color", "#ffffff")
    self.root.configure(bg=bg)

  def style_widget(self, widget, component_name):
    self.style_manager.apply_style(widget, component_name)

  def run(self):
    self.root.mainloop()

  def close(self):
    self.root.destroy()


