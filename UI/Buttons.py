#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Button, Frame


# import os
# import requests


class RButton(Frame):
    def __init__(self, parent,
                 fs=16, width=300, height=300, command=None):
        Frame.__init__(self, parent, width=width, height=height)
        self.pack_propagate(0)
        self.font = 'Times', int(fs), 'bold'
        self.start = False
        self.btn = Button(self, text='Register', font=self.font,
                          command=command)
        self.btn.pack(expand=1, fill='both')
