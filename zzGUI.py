from tkinter import *
import zzExtract

#create the window
root = Tk()

#modify root window
root.title("Feature Extractor")
root.geometry("250x125")

#menubar
menu = Menu(root)
root.config(menu=menu)
NLTK_texts = Menu(menu)
Guten = Menu(NLTK_texts)
menu.add_cascade(label = "NLTK texts", menu = NLTK_texts)
NLTK_texts.add_cascade(label = "Gutenberg", menu = Guten)
for text in zzExtract.getGuten():
    Guten.add_command(label = text,
                      command = lambda: print(text))

#status
labeltext = StringVar()
labeltext.set("SELECT A FILE")
label1 = Label(root, textvariable = labeltext, height = 4)
label1.pack()

#file stuff
def extractfromfile():
    root.fileName = filedialog.askopenfilename( filetypes = () )
    labeltext.set("EXTRACTING FEATURES...")
    try:
        zzExtract.extractFile(root.fileName)
        labeltext.set("FEATURES EXTRACTED!")
    except:
        labeltext.set("EXTRACTION FAILED!")
button = Button(root, text = "Open text file and extract features", command = extractfromfile)
button.pack()

#start the event loop
root.mainloop()
