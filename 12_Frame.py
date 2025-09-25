from tkinter import *

root = Tk()
root.title("pauls GUI")
root.geometry("640x480")

Label(root, text="wählen sie bitte die Menu").pack(side="top")

Button(root, text="order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="hamburger").pack()
Button(frame_burger, text="cheeshamburger").pack()
Button(frame_burger, text="chickenhamburger").pack()


frame_drink = LabelFrame(root, text="drinks")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Cola").pack()
Button(frame_drink, text="Mezomix").pack()
Button(frame_drink, text="Sprite").pack()

root.mainloop()