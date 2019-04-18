#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import Label, Frame, StringVar
from tkinter.ttk import Progressbar


class BarS(Frame):
    def __init__(self, parent, fs=16,
                 width=1600, height=50, ratio=0.7):
        Frame.__init__(self, parent, width=width, height=height)
        self.pack_propagate(0)
        self.font = 'Times', int(fs)
        
        self.sF = Frame(self, height=height, width=int(width*abs(ratio)))
        self.sF.pack_propagate(0)
        
        self.pF = Frame(self, height=height, width=int(width*(1-abs(ratio))))
        self.pF.pack_propagate(0)
        
        if ratio >= 0:
            self.sF.pack(side='left')
            self.pF.pack(side='left')
        else:
            self.pF.pack(side='left')
            self.sF.pack(side='left')
        
        self.msg = StringVar()
        self.status = Label(self.sF, textvariable=self.msg,
                            font=self.font, justify='left')
        self.status.pack(expand=1, fill='both')
        
        self.progress = Progressbar(self.pF, orient="horizontal", mode="determinate")
        self.progress.pack(expand=1, fill='both')
        self.current_val = 0

    def update(self, msg, val):
        self.msg.set(str(msg))
        increase = 100-self.current_val+val
        self.progress.step(float(increase))
        self.current_val = val
        return
