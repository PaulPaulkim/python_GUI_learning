import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+100+300") #가로 x 세로 + x좌표 + y 좌표

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")

# progressbar.start(10) #10 ms 마다 움직임
# progressbar.pack()
# def btncmd():
#    progressbar.stop()



# btn = Button(root, text="stop", command=btncmd)
# btn.pack()
p_var2 = DoubleVar()
progresbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progresbar2.pack()


def btncmd2():
    for i in range(101):
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i)
        progresbar2.update()
        print(p_var2.get())

btn = Button(root, text="start", command=btncmd2)
btn.pack()

root.mainloop()