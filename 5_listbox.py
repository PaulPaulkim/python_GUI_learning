from tkinter import *

root = Tk()

root.title("Pauls GUI")

root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=2)
listbox.insert(0, "Apfel")
listbox.insert(1, "banana")
listbox.insert(2, "Erdbeer")
listbox.insert(END, "wassermelone")

listbox.pack()



def btncmd():
    #delete
    #listbox.delete(0)
    #Zählen
    #print("list hat ", listbox.size(), "Sachen")
    #drinen (start, ende)
    #print("erste bis dritte", listbox.get(0,2))
    #ausgewählte Sachen(위치로 반환)
    print("ausgewählt", listbox.curselection())



btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
