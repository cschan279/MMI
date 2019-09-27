#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import Label, StringVar
from PIL import Image, ImageTk


class TextLabel(Frame):
    def __init__(self, parent, width=300, height=150, 
                 text='label', font=('Times', 12), var=False, 
                 bd=1, relief='solid', bg='#FFFFFF', justify='center'):
        Frame.__init__(self, parent, bd=bd, bg=bg, relief=relief, 
                       width=width, height=height)
        self.pack_propagate(0)
        if justify == 'left':
            anchor = 'w'
        elif justify == 'right':
            anchor = 'e'

        if var:
            self.var = True
            self.strVar = StringVar()
            self.strVar.set(text)
            self.label = Label(self, textvariable=self.strVar, font=font, 
                               bg=bg, anchor=anchor, justify=justify)
        else:
            self.var = False
            self.label = Label(self, text=text, font=font, 
                               bg=bg, anchor=anchor, justify=justify)
        
        self.label.pack(fill='both', expand=True)
        
    def update(self, text):
        if self.var:
            self.strVar.set(str(text))
        else:
            print('This is a fix label')
        return
    
class ImgLabel(Label):
    def __init__(self, parent, width=300, height=150, resize='n', 
                 img='imgpath', bd=1, relief='solid'):
        self.image, self.w, self.h = self.fl2tk(img, width, height, resize)
        
        Label.__init__(self, parent, width=self.w, height=self.h, image=self.image,
                       relief=relief, bd=bd)
        return
        
    @staticmethod
    def fl2tk(filename, width, height, resize):
        img = Image.open(filename)
        wf, hf = img.size
        if wf > width or resize == 'w':
            resizeH = int(hf*width/wf)
            im = img.resize((width, resizeH), Image.ANTIALIAS)
            return ImageTk.PhotoImage(im), width, resizeH
        elif hf > height or resize == 'h':
            resizeW = int(wf*height/hf)
            im = img.resize((resizeW, height), Image.ANTIALIAS)
            return ImageTk.PhotoImage(im), resizeW, height
        elif resize == 'b':
            im = img.resize((height, width), Image.ANTIALIAS)
            return ImageTk.PhotoImage(im), width, height
        else:
            return ImageTk.PhotoImage(img), wf, hf
        
