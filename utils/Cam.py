#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2
from threading import Thread
import numpy as np
class Cam:
    def __init__(self, source, width=1920, height=1080):
        self.cam = cv2.VideoCapture(source)
        self.looping = False
        
        self.width = width
        self.height = height
        self.setCam(3,width)
        self.setCam(4,height)
        
        self.blank = np.zeros((width,height,3),np.uint8)
        
        
        self.ret = True
        self.frame = self.blank
        self.thd = Thread(target=self.loop)
        self.thd.start()
        return
    
    def read(self):
        return self.ret, self.frame
    
    def release(self):
        self.looping = False
        self.cam.release()
    
    def loop(self):
        self.looping = True
        while self.looping:
            try:
                r, f = self.cam.read()
                self.ret = r
                if r:
                    self.frame = f
                else:
                    self.frame = self.blank
            except:
                print('error in capture')
        return
    
    def getCam(self, index):
        return self.cam.get(index)
    
    def setCam(self, index, value):
        if index == 3:
            self.width=value
            self.blank = np.zeros((self.width,self.height,3),np.uint8)
        elif index == 4:
            self.height=value
            self.blank = np.zeros((self.width,self.height,3),np.uint8)
        return self.cam.set(index, value)
        