# FILE: src/ui/style_manager.py

import tkinter as tk
import json
import os

class StyleManager:
  def __init__(self, theme_path, component_styles_dir):
    self.theme_path = theme_path
    self.component_styles_dir = component_styles_dir
    self.theme = self._load_json(theme_path)
    self.component_styles = {}

  def _load_json(self, path):
    if not os.path.exists(path):
      return {}
    with open(path, 'r') as file:
      return json.load(file)

  def get_theme(self):
    return self.theme

  def get_style(self, component_name):
    if component_name not in self.component_styles:
      path = os.path.join(self.component_styles_dir, f"{component_name}.json")
      self.component_styles[component_name] = self._load_json(path)
    return self.component_styles.get(component_name, {})

  def apply_style(self, widget:tk.Widget, component_name):
    style = self.get_style(component_name)
    widget.configure(**style)
