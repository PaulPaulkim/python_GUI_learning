from tkinter import *

root = Tk()

root.title("Pauls GUI")

root.geometry("640x480")

Label(root, text="wählen sie bitte die Menu").pack()

burger_var = IntVar()

btn_burger1 = Radiobutton(root, text="hambuger",value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="cheesehambuger",value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenhambuger",value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()



Label(root, text="Wählen sie bitte Getränke").pack()
getränke_var = StringVar()
btn_getränke = Radiobutton(root, text="cola", value=str, variable=getränke_var)
btn_getränke2 = Radiobutton(root, text="Mezomix", value=str, variable=getränke_var)
btn_getränke.pack()
btn_getränke2.pack()


def btncmd():
   print(burger_var.get())
   print(getränke_var.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
