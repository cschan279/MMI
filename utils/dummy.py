#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import cv2
from time import sleep
import numpy as np
class Detect:
    def __init__(self):
        self.progress = 0 #0~100
        self.crop = np.zeros((100,100,3),np.uint8)
        self.train_thread = Thread(target=self.__train)
        
    def detect(self, img):
        image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.crop=img
        sleep(0.1)
        return image, img
    
    def save_img(self, name):
        print("image with size", self.crop.shape,  "saved for", name)
        return True
    
    def __train(self):
        count = 0
        total = 120
        print("start training with", total, "persons")
        for i in range(total):
            count+= 1
            self.progress = int(float(count*100)/total)
            #print(self.progress)
            sleep(0.1)
        return
    
    def start_train(self):
        self.train_thread = Thread(target=self.__train)
        self.train_thread.start()
