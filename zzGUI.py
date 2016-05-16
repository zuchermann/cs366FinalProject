from tkinter import filedialog
from tkinter import *
import zzExtract
import copy
import os

#create the window
root = Tk()

#modify root window
root.title("Feature Extractor")
root.geometry("250x125")

    

#menubar
menu = Menu(root)
help_menu = Menu(menu)
root.config(menu=menu)
NLTK_texts = Menu(menu)
Guten = Menu(NLTK_texts)
menu.add_cascade(label = "NLTK texts", menu = NLTK_texts)
menu.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "Open Feature Extractor Help", command = lambda: os.system("open help.txt"))
NLTK_texts.add_cascade(label = "Gutenberg", menu = Guten)

#menubar: Gutenberg stuff
def guten(text):
    labeltext.set("EXTRACTING FEATURES")
    zzExtract.extractGuten(text)
    labeltext.set("FEATURES EXTRACTED!")
    
def makeGutenFunc(text):
    return lambda: guten(text)
for text in zzExtract.getGuten():
    Guten.add_command(label = text, command = makeGutenFunc(text))

#status
labeltext = StringVar()
labeltext.set("SELECT A FILE")
label1 = Label(root, textvariable = labeltext, height = 4)
label1.pack()

#file stuff
def extractfromfile():
    fileName = filedialog.askopenfilename( filetypes = () )
    labeltext.set("EXTRACTING FEATURES...")
    try:
        zzExtract.extractFile(fileName)
        labeltext.set("FEATURES EXTRACTED!")
    except:
        labeltext.set("EXTRACTION FAILED!")
button = Button(root, text = "Open text file and extract features", command = extractfromfile)
button.pack()

#start the event loop
root.mainloop()
