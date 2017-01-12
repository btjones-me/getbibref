#!/usr/bin/env python

''' getbibref.py
Author: Ben Jones 
Version: 0.2
Small attempt at a program to take a DOI input (unique address for research papers) and 
    return the Bibtex formatted result from the above website in a copy/pastable form. '''

import urllib.request
from tkinter import *

##This is the logic
# x = urllib.request.urlopen('http://api.crossref.org/works/10.1098/rsta.2010.0348/transform/application/x-bibtex')
# data = x.read()
# print(data)

class MyFirstGUI(Tk):

    def __init__(self):
        # create main window by calling the __init__ method of parent class Tk
        Tk.__init__(self)
        self.geometry("600x400")
        self.title("DOI to Bibtex Tool")

        label1 = Label(self, text="Enter DOI")
        label1.pack()

        ##Give a default, customisable DOI value
        self.entry1 = Entry(self, bd=5)
        self.entry1.insert(0, '10.1098/rsta.2010.0348')
        self.entry1.pack()

        submit = Button(self, text ="Submit", command = self.update)
        submit.pack()

        close_button = Button(self, text="Close", command=self.quit)
        close_button.pack()

        ##Here I want to produce the result of my http request call
        self.w = Text(self, relief='flat', 
                      bg = self.cget('bg'),
                      highlightthickness=0, height=100) 
        # trick to make disabled text copy/pastable
        self.w.bind("<1>", lambda event: self.w.focus_set())
        self.w.insert('1.0', "Bibtex Reference Here")
        self.w.configure(state="disabled", inactiveselectbackground=self.w.cget("selectbackground"))
        self.w.pack()

        self.mainloop()

    def update_text(self, new_text):
        """ update the content of the text widget """
        new_text = new_text.decode('unicode-escape').replace("%2F", "/", 1).encode() ##Removes the %2F that replaces the / in the URL
        print(type(new_text))
        self.w.configure(state='normal')
        self.w.delete('1.0', 'end')    # clear text
        self.w.insert('1.0', new_text) # display new text
        self.w.configure(state='disabled') 


    def update(self):
        doi = str(self.entry1.get()) ##Get the user inputted DOI 
        print(str(self.entry1.get()))
        url = 'http://api.crossref.org/works/'+ doi + '/transform/application/x-bibtex'
        print(url)

        try:
            x = urllib.request.urlopen(url)
        except urllib.error.URLError as e: 
            ##Show user an error if they put in the wrong DOI
            self.update_text(str(e)) 

        else:
            ##Update the output area to the returned form of the text entry, ideally highlightable for copying
            data = x.read()
            self.update_text(data) 

if __name__ == '__main__':
    my_gui = MyFirstGUI()




__author__ = "Ben Jones"
__version__ = "0.2"