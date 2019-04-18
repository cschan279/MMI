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
        '''#############################################'''
        self.mod['top']=Frame(self, width=self.scale*160, height=self.scale*15)
        self.mod['top'].pack()
        self.mod['top'].pack_propagate(0)
        '''---------------------------------------------'''
        self.mod['Logo'] = Logo(self.mod['top'],width=self.scale*20,
                                img='hkpc.png')
        self.mod['Logo'].pack(side='left')
        
        self.mod['Clock']=Clock(self.mod['top'],
                                width=self.scale*25, height=self.scale*8, 
                                fs=self.scale*3)#, form="%Y:%m:%d\n%H:%M:%S")
        self.mod['Clock'].pack(side='right')
        
        self.mod['Title']=Label(self.mod['top'],width=35,justify='left', bg="#FFFFFF",
                                text=self.headtitle, font=("Times", self.scale*4))
        self.mod['Title'].pack(side='left')

        '''#############################################'''
        self.mod['mid']=Frame(self)
        self.mod['mid'].pack()
        '''---------------------------------------------'''
        self.mod['Dis'] = Display(self.mod['mid'], width=self.scale*135, height=self.scale*75)
        self.mod['Dis'].grid(row=0, column=0, rowspan=75)
        
        
        
        self.mod['Crp'] = Display(self.mod['mid'], width=self.scale*25, height=self.scale*36)
        self.mod['Crp'].grid(row=0, column=1, rowspan=20)
        
        self.mod['Btn']=RButton(self.mod['mid'], 
                                width=self.scale*25, height=self.scale*15, 
                                fs=self.scale*4, 
                                command=self.askname)
        self.mod['Btn'].grid(row=74, column=1)
        '''#############################################'''
        self.mod['btm']=Frame(self)
        self.mod['btm'].pack()#fill='x')
        '''---------------------------------------------'''
        self.mod['Bar'] = BarS(self.mod['btm'], fs=self.scale*2, ratio=0.845,
                                  width=self.scale*160, height=self.scale*2.5)
        self.mod['Bar'].pack()
        '''#############################################'''
        return
    
    def update(self):
        self.mod['Clock'].update()
        if self.asking:
            self.mod['Bar'].update("Register", 1.0)
        elif self.det.train_thread.isAlive():
            pgs = self.det.progress
            self.mod['Bar'].update("Training", float(pgs))
        else:
            r, f = self.cam.read()
            res, crop = self.det.detect(f)
            self.mod['Dis'].update(res)
            self.mod['Crp'].update(crop)
            self.mod['Bar'].update("Normal", 100.0)
        return
        
    def askname(self):
        self.asking = True
        self.option_add('*Dialog.msg.font', 'Times '+str(self.scale*2))
        name = askstring("Register", "Please input your name:")
        if name:
            print(name)
            if self.det.save_img(name):
                self.det.start_train()
            else:
                print("error in saving image")
        else:
            print("Cancelled")
        
        self.asking = False
        return
            
    def onDestroy(self):
        self.cam.release()
        return
    
if __name__ == "__main__":
    x = tkApp(title="Face Recog~~~~~", scale=10, delay=100, fullscreen=False)
    x.mainloop()