from tkinter import *
import zzExtract

#create the window
root = Tk()

#modify root window
root.title("Feature Extractor")
root.geometry("200x100")

#file stuff
def extractfromfile():
    root.fileName = filedialog.askopenfilename( filetypes = () )
    zzExtract.extractFile(root.fileName)
button = Button(root, text = "Open file and extract features", command = extractfromfile)
button.pack()


#start the event loop
root.mainloop()
