from tkinter import *

root = Tk()

root.title("Pauls GUI")

root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "schreiben sie bitte Text")

e = Entry(root, width=30) #entry kann man nicht Enter drucken.
e.pack()
e.insert(0, "nur ein line")

def btncmd():
    print(txt.get("1.0", END)) #1.0 = erste line, 0: 0te column 
    #bringen die Sache von Entry
    print(e.get())
    #delete 
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text="click", command=btncmd)
btn.pack()
 
root.mainloop()