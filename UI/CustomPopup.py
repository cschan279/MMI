#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""
from tkinter import Toplevel, Label, Entry, Button, StringVar


class CustomPopup(Toplevel):
    def __init__(self, parent, message):
        Toplevel.__init__(self, parent)
        
        self.var = StringVar()
        
        font=('Times', 20)
        self.label = Label(self, text=message, font=font)
        self.label.grid(column=0, row=0, columnspan=2)
        self.entry = Entry(self, textvariable=self.var, font=font)
        self.entry.grid(column=0, row=1, columnspan=2)
        self.ok_btn = Button(self, text='OK', command=self.on_ok)
        self.ok_btn.grid(column=1, row=2)
        
        self.entry.bind('<Return>', self.on_ok)
        return
        
    def on_ok(self, event=None):
        print(event)
        self.destroy()
        return
        
    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get()
        
if __name__ == '__main__':
    def onBtn():
        global root, var
        string = CustomPopup(root, 'Input Below:').show()
        var.set(string)
        return

    root = Tk()
    font = ('Times', 20)
    Label(root, text='click below to show', font=font).pack()

    btn = Button(root, text='click', font=font, command=onBtn)
    btn.pack()

    var = StringVar()
    var.set('N/A')
    lab = Label(root, textvariable=var, font=font)
    lab.pack()

    root.mainloop()
