import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("pauls GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("information", "ihre Buchung ist erfolgreich")

def warn():
    msgbox.showwarning("warning", "ihre Buchung ist nicht erfolgreich")

def error():
    msgbox.showerror("error", "gibt error")   

def okcancel():
    msgbox.askokcancel("ok/cancle", "wollen sie sicher?")

def retrycancel():
    msgbox.askretrycancel("retry/cancel", "wollen sie nochmal probieren?")

def yesno():
    msgbox.askyesno("yes/no", "möchten sie sicher?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="die Daten sind nicht gespeichert, sicher quit?")
    print("answer", response)
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")

Button(root, command=info, text="information").pack()

Button(root, command=warn, text="Warning").pack()

Button(root, command=error, text="error").pack()

Button(root, command=okcancel, text="ok cancel").pack()

Button(root, command=retrycancel, text="retry").pack()

Button(root, command=yesno, text="yesno").pack()

Button(root, command=yesnocancel, text="yesnocancel").pack()
root.mainloop()