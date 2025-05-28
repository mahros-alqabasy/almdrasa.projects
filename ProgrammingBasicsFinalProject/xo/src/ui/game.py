# src/weather_app.py


import src.ui.gui as gui

import tkinter as tk

class Game(gui.Gui):
    def __init__(self):
        conf = gui.AppConf(
            window=gui.WindowConf(
                title="XO Game",
                size=(800, 600)
            )
        )
        super().__init__(conf)

        # components
        # self.body = Body(self.root, self.loadData)
        # self.tool_bar = ToolBar(self.root)
        # self.status_bar = StatusBar(self.root)

        self.init_widgets()


    def init_widgets(self):
        # widgets
        title = tk.Label(text="Mahros")
        title.pack(side='top', fill='y')
        # self.tool_bar.pack(side="top", fill="x")
        # self.body.pack(side="top", fill=tk.BOTH, expand=True)
        # self.status_bar.pack(side="bottom", fill="x")
        pass
    
