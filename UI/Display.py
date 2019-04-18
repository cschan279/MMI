#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Canvas, Frame
from PIL import Image, ImageTk
import cv2


class Display(Frame):
    def __init__(self, parent, width=200, height=100):
        
        Frame.__init__(self, parent)
        self.w = width
        self.h = height
        
        self.default_image = self.blanktkimage(self.w, self.h)
        
        self.screen = Canvas(self, width=self.w, height=self.h)
        self.screen.pack()
        self.display = self.screen.create_image(0, 0,
                                                image=self.default_image, 
                                                anchor='nw')
        self.image = self.default_image
        return
    
    def update(self, img):
        self.image = self.cv2tk(img, self.w, self.h)
        self.screen.itemconfig(self.display, 
                               image=self.image)
        return
    ######################################################################
    @staticmethod
    def fl2tk(filename, w, h):
        img = Image.open(filename)
        im = img.resize((int(w), int(h)),
                        Image.ANTIALIAS)
        return ImageTk.PhotoImage(im)

    @staticmethod
    def cv2tk(img, w, h):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
        tk_img = ImageTk.PhotoImage(image=Image.fromarray(img))
        
        return tk_img

    @staticmethod
    def blanktkimage(w, h):
        img = Image.new('RGB', (w, h), color='blue')
        return ImageTk.PhotoImage(img)
    #######################################################################
