#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""


from tkinter import Tk

import traceback


class App(Tk):
    def __init__(self, title="APP", scale=10, delay=500, fullscreen=False, fix=False):
        super().__init__()
        self.title(title)
        self.headtitle = title
        self.scale = scale
        self.delay = delay
        self.attributes('-fullscreen', fullscreen)
        self.mod = {}
        
        if fix:
            self.resizable(False, False)
        self.bind('<Escape>', lambda e: self.destroy())
        
        self.setup()
        self.layout()
        return
        
    def mainloop(self): #call this to start app
        self.start()
        self.again()
        super().mainloop()
        return
    
    def again(self):
        try:
            self.update()
        except:
            print("error in update")
            traceback.print_exc()
        self.after(self.delay, self.again)
        
    def destroy(self):
        super().destroy()
        self.onDestroy()
        return
    
    def start(self):
        #kick start of required threads
        return
    
    def setup(self):
        #setup variable or threading
        return
    
    def update(self):#put required update
        #update the all module required
        print("null")
        return
    
    def layout(self):# put module here
        #Build with Custom Widget
        print("null layout")
        return
    
    def onDestroy(self):
        #close everything before exit
        return
