from tkinter import *

root = Tk()

root.title("Pauls GUI")

root.geometry("640x480")

chkvar = IntVar() #체크바에 인트형으로 값을 저장한다.
chkbox = Checkbutton(root, text="heute nicht mehr zeigen", variable=chkvar)
#chkbox.select()
#chkbox.deselect()

chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Wochenlang nicht mehr zeigen", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
