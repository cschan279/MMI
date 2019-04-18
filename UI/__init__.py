#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""
import cv2
from PIL import Image, ImageTk
import numpy as np

def im2tk(img, w, h):
    #print(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (w,h), interpolation=cv2.INTER_AREA)
    #cv2.imshow('hihi', img)
    #cv2.waitKey(1)
    
    tk_img = ImageTk.PhotoImage(image=Image.fromarray(img))
    
    return tk_img

def fl2tk(filename, w=None, h=None):
    img = Image.open(filename)
    if w and h:
        im = img.resize((int(w), int(h)),
                        Image.ANTIALIAS)
    elif w:
        wf, hf = img.size
        h = w * hf / wf 
        im = img.resize((int(w), int(h)),
                        Image.ANTIALIAS)
    elif h:
        wf, hf = img.size
        w = h * wf / hf
        im = img.resize((int(w), int(h)),
                        Image.ANTIALIAS)
    else:
        im=img
    return ImageTk.PhotoImage(im)

def blanktkimage(w, h):
    img = Image.new('RGB', (w,h), color='blue')
    return ImageTk.PhotoImage(img)
