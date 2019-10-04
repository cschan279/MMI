#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Button, Frame, Label
from tkinter.simpledialog import askstring
from UI.App import App
from UI.Buttons import RButton
from UI.Display import Display
from UI.Logo import Logo
from UI.Clock import Clock
from UI.Bar import BarS
from utils.Cam import Cam
from utils.dummy import Detect


class tkApp(App):
    def setup(self):
        self.cam = Cam(0)
        self.det = Detect()
        self.asking = False
    
    def layout(self):
        
        return
    
    def update(self):
        print('update')
        return
            
    def onDestroy(self):
        self.cam.release()
        return
    
if __name__ == "__main__":
    x = tkApp(title="User Interface", scale=10, delay=100, fullscreen=False)
    x.mainloop()
