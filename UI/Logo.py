#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import Label, Frame
from os.path import isfile
from . import *


class Logo(Frame):
    def __init__(self, parent, width=None,height=None,
                 img=None, ):
        Frame.__init__(self, parent)
        
        if not isfile(img):
            raise FileNotFoundError('No such file: <<' + str(img) + '>>')
        self.width=width
        self.height=height

        self.img = fl2tk(img, w=self.width, h=self.height)
        self.head = Label(self, image=self.img)
        self.head.image=self.img
        self.head.pack()
        
        

