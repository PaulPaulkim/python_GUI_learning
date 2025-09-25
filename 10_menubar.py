import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+100+300") #가로 x 세로 + x좌표 + y 좌표

menu = Menu(root)

def create_new_file():
    print("making new file")

#file menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Neu File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()#구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator()#구분자
menu_file.add_command(label="save all", state="disabled")
menu_file.add_separator()#구분자
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu = menu_file)


#edit
menu.add_cascade(label="Edit")


#langugae menu
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

#checkbox

menu_view = Menu(menu, tearoff=0 )
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="view", menu=menu_view)

root.config(menu=menu)
root.mainloop()