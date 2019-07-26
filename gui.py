from tkinter import filedialog
from tkinter import *

root = Tk()


var1 = StringVar()
var2 = StringVar()







root = Tk()
root.geometry("400x400")

isiPath = ""
htmlPath = ""


def getIsiFile():
    global isiPath
    isiPath = filedialog.askopenfilename(initialdir = "/",title = "Select isi text file",filetypes = (("text ","*.txt"),("all files","*.*")))
    print(isiPath)
    return isiPath



def getHTMLFile():
    global htmlPath
    htmlPath = filedialog.askopenfilename(initialdir="/", title="Select html file", filetypes=(("html", "*.html"), ("all files", "*.*")))
    print(htmlPath)
    return htmlPath

b = Button(root, text="Select ISI text file", width=15, height=2, command=getIsiFile)
label = Label( root, textvariable=var1.set(isiPath), relief=RAISED )
label.place(x=20, y=30)
label.pack()


c = Button(root, text="Select HTML file", width=15, height=2, command= getHTMLFile)
label2 = Label( root, textvariable=var2.set(htmlPath), relief=RAISED )
label2.place(x=20, y=60)

b.pack(in_=root, side=LEFT)
c.pack(in_=root, side=LEFT)

root.mainloop()

# print(isiPath)
# print(htmlPath)