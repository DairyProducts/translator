import tkinter as tk
from googletrans import Translator
import sys
from time import strftime
import time
import calendar
import datetime as dt
import os
#from time import gmtime, strfttime
#time=strfttime("%Y-%m-%d %H:%M:%S", gmtime())
#print(time)
trans=Translator()
bgcolor="whitesmoke"
root=tk.Tk()
canvas=tk.Canvas(root,width=400,height=400,relief='raised',bg=bgcolor)
canvas.pack()
#pixel=tk.PhotoImage(width=1, height=1)

outputthis=tk.Label(root, text='', wraplength=375, bg=bgcolor, fg='black')
canvas.create_window(200,325, window=outputthis)
outputlabel=tk.Label(root, text='', wraplength=375, bg=bgcolor, fg='black')
canvas.create_window(200,325, window=outputlabel)

class Clock(tk.Label): #I copy/pasted this from https://stackoverflow.com/questions/57632265/how-to-get-the-current-date-to-display-in-a-tkinter-window
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        tk.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%I:%M:%S %p')
        else:
            self.time     = time.strftime('%I:%M:%S %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%I:%M:%S %p')
        else:
            new_time = time.strftime('%I:%M:%S %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)
clock=Clock(root)
clock.config(font=('Helvetica,13 '))
clock1=tk.Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}",fg="black", bg=bgcolor, font=("helvetica", 13))
canvas.create_window(85, 380, window=clock1)

def opendark():
    root.destroy()
    os.system('101.py')

def translate():
    global outputthis
    global outputlabel
    outputthis.destroy()
    outputlabel.destroy()
    fromcode=transfrom.get()
    tocode=transto.get()
    transthis=transinput.get("1.0","end")
    #transthis=transinput.get()
    #print(tocode)
    #print(fromcode)
    '''
    if fromcode==('b2'):
        if tocode==('b10'):
            output=str(int(transthis, 2))
        if tocode==('b8'):
            output=str(int(transthis, 8))
        if tocode==('b6'):
            output=str(hex(int(transthis)))
            output=output[2:]
    elif fromcode==('b10'):
        if tocode==('b2'):
            output=bin(int(transthis))
            output=output[2:]
        if tocode==('b8'):
            output=str(int(transthis, 8))
        if tocode==('b6'):
            output=str(hex(int(transthis)))
            output=output[2:]
    else:
        output=trans.translate(transthis, src=fromcode, dest=tocode)
        output=output.text
    '''
    try:
        output=trans.translate(transthis, src=fromcode, dest=tocode)
        output=output.text
        outputlabel=tk.Label(root, text='Output:')
        outputlabel.config(font=('lightcyan,13'), fg='blue', bg=bgcolor)
        outputthis=tk.Label(root, text=output, wraplength=375, bg=bgcolor, fg='black')
        outputthis.config(font=('Helvetica,13 '))
    except:
        output="The language code(s) may be invalid or the text inputted cannot be processed. See dairyproducts.github.io for troubleshooting."
        outputlabel=tk.Label(root, text='An error has occurred:')
        outputlabel.config(font=('lightcyan,13'), fg='red', bg=bgcolor)
        outputthis=tk.Label(root, text=output, wraplength=375, bg=bgcolor, fg='red')
        outputthis.config(font=('Helvetica,13 '))
    canvas.create_window(200, 280, window=outputlabel)
    canvas.create_window(200, 325, window=outputthis)

transfromlabel=tk.Label(root, text='Translate from:', bg=bgcolor, fg='black')
transfromlabel.config(font=('Helvetica,13 '))
canvas.create_window(200, 25, window=transfromlabel)
transfrom=tk.Entry(root) 
canvas.create_window(200, 50, window=transfrom)

transtolabel=tk.Label(root, text='Translate to:', bg=bgcolor, fg='black')
transtolabel.config(font=('Helvetica,13 '))
canvas.create_window(200, 80, window=transtolabel)
transto=tk.Entry(root) 
canvas.create_window(200, 105, window=transto)

textinput=tk.Label(root, text='Input:', bg=bgcolor, fg='black')
textinput.config(font=('Helvetica,13 '))
canvas.create_window(200, 130, window=textinput)
transinput=tk.Text(root, wrap=tk.WORD)
transinput.configure(font=("calibri, 10"))
transinput.place(x=200, y=175, width=200, height=65, anchor=tk.CENTER) 

button=tk.Button(root, text='Translate', command=translate, bd=0, height=1, width=9)
button.config(bg="lightgreen", fg="black")
button.pack(pady=10)
canvas.create_window(200, 250, window=button, anchor=tk.CENTER)
#canvas.create_window(window=input)

themebutton=tk.Button(root, text='💡', command=opendark, bd=0)
themebutton.config(bg="gray", fg="yellow")
canvas.create_window(390, 385, window=themebutton, anchor=tk.CENTER)

root.resizable(0,0)
root.title('Translator')
root.mainloop()

#For those of you poking through the source code: the below portion is for future plans :)

