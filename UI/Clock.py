#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import Label, Frame, StringVar

import time


class Clock(Frame):
    def __init__(self, parent, width=300, height=100, 
                 fs=16, 
                 form="%Y:%m:%d\n%H:%M:%S"):
        Frame.__init__(self, parent, width=width, height=height)
        self.pack_propagate(0)
        self.w = width
        self.h = height
        self.font = ("Times", int(fs))

        self.msg = form
        self.var = StringVar()
        self.timer = Label(self, textvariable=self.var,
                           font=self.font, width=self.w, justify='center')
        self.timer.pack(expand=1, fill='both')
        self.var.set(self.msg)
        
        return
    
    def update(self, t=None):
        if not t:
            self.var.set(time.strftime(self.msg))
        elif t == 'stay':
            pass
        else:
            self.var.set(t)
        return
