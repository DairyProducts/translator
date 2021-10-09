import tkinter as tk
from googletrans import Translator
import sys
from time import strftime
import time
import calendar
import datetime as dt
import os
import webbrowser
import functions as fc

#from time import gmtime, strfttime
#time=strfttime("%Y-%m-%d %H:%M:%S", gmtime())
#print(time)
trans=Translator()
bgcolor='#1f2126'
root=tk.Tk()
canvas=tk.Canvas(root,width=400,height=400,relief='raised',bg=bgcolor)
canvas.pack()
#pixel=tk.PhotoImage(width=1, height=1)

outputthis=tk.Label(root, text='', wraplength=375, bg=bgcolor, fg='white')
canvas.create_window(200,325, window=outputthis)
outputlabel=tk.Label(root, text='', wraplength=375, bg=bgcolor, fg='white')
canvas.create_window(200,325, window=outputlabel)
label1=tk.Label(root, text='', wraplength=375, bg=bgcolor, fg='white')
canvas.create_window(200,325, window=outputlabel)

version = "Version 1.3.0b"

def openlight():
    global outputthis
    global outputlabel
    global label1
    label1.destroy()
    outputthis.destroy()
    outputlabel.destroy()
    label1 = tk.Label(root, text='Feature in development!')
    label1.config(font=('helvetica', 13), bg=bgcolor, fg='white')
    canvas.create_window(200, 280, window=label1)
    '''
    root.destroy()
    #canvas.destroy()
    import light
    #tk.destroy()
    '''
new = 1
url = "https://cloud.google.com/translate/docs/languages"
url2 = "https://github.com/DairyProducts/translator"
def codes():
    webbrowser.open(url, new=new);
def github():
    webbrowser.open(url2, new=new);
    
def translate():
    global outputthis
    global outputlabel
    global label1
    label1.destroy()
    outputthis.destroy()
    outputlabel.destroy()
    fromcode=transfrom.get()
    fromcode=str(fromcode)
    tocode=transto.get()
    tocode=str(tocode)
    transthis=transinput.get("1.0","end")
    #transthis=transinput.get()
    #print(tocode)
    #print(fromcode)
    try:
        if(fromcode.lower() == "bin" and tocode.lower() == "dec"):
            output = fc.bintodec(transthis)
        elif(fromcode.lower() == "dec" and tocode.lower() == "bin"):
            output = fc.dectobin(transthis)
        else:

            output=trans.translate(transthis, src=fromcode, dest=tocode)
            output=output.text
        outputlabel=tk.Label(root, text='Output:')
        outputlabel.config(font=('lightcyan,13'), fg='aqua', bg=bgcolor)
        outputthis=tk.Label(root, text=output, wraplength=375, bg=bgcolor, fg='white')
        outputthis.config(font=('Helvetica,13 '))
    except:
        output="The language code(s) may be invalid or the text inputted cannot be processed. See dairyproducts.github.io for troubleshooting."
        outputlabel=tk.Label(root, text='An error has occurred:')
        outputlabel.config(font=('lightcyan,13'), fg='red', bg=bgcolor)
        outputthis=tk.Label(root, text=output, wraplength=375, bg=bgcolor, fg='red')
        outputthis.config(font=('Helvetica,13 '))
    canvas.create_window(200, 280, window=outputlabel)
    canvas.create_window(200, 325, window=outputthis)

transfromlabel=tk.Label(root, text='Translate from:', bg=bgcolor, fg='white')
transfromlabel.config(font=('Helvetica,13 '))
canvas.create_window(200, 25, window=transfromlabel)
transfrom=tk.Entry(root) 
canvas.create_window(200, 50, window=transfrom)

transtolabel=tk.Label(root, text='Translate to:', bg=bgcolor, fg='white')
transtolabel.config(font=('Helvetica,13 '))
canvas.create_window(200, 80, window=transtolabel)
transto=tk.Entry(root) 
canvas.create_window(200, 105, window=transto)

textinput=tk.Label(root, text='Input:', bg=bgcolor, fg='white')
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

themebutton=tk.Button(root, text='☀', command=openlight, bd=0)
themebutton.config(bg="gray", fg="yellow")
canvas.create_window(390, 385, window=themebutton, anchor=tk.CENTER)

themebutton=tk.Button(root, text='❓', command=codes, bd=0)
themebutton.config(bg="gray", fg="yellow")
canvas.create_window(370, 385, window=themebutton, anchor=tk.CENTER)

themebutton=tk.Button(root, text='📁', command=github, bd=0)
themebutton.config(bg="gray", fg="yellow")
canvas.create_window(350, 385, window=themebutton, anchor=tk.CENTER)

verlabel=tk.Label(root, text=version, bg=bgcolor, fg='white')
verlabel.config(font=('Helvetica,8 '))
canvas.create_window(115, 385, window=verlabel,anchor=tk.E)

root.resizable(0,0)
root.title('Translator')
root.mainloop()

#For those of you poking through the source code: the below portion is for future plans :)

