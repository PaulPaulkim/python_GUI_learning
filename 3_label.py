from tkinter import*

root = Tk()

root.title("Pauls GUI")

root.geometry("640x480")

Label1 = Label(root, text= "hallo")
Label1.pack()

photo = PhotoImage(file="gui_basic/check.png")
label2 = Label(root, image= photo)
label2.pack()

def change():
    Label1.config(text = "wiedersehen")
    global photo02
    photo02 = PhotoImage(file="gui_basic/img02.png")
    label2.config(image=photo02)

btn = Button(root, text = "click", command = change)
btn.pack()

photo02 = PhotoImage(file="gui_basic/img02.png")


root.mainloop()