from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+100+300") #가로 x 세로 + x좌표 + y 좌표

root.resizable(False,False) #창 크기변경 불가

btn1 = Button(root, text = "button01")
btn1.pack()

btn2 = Button(root, padx=5 , pady = 10, text = "button02")
btn2.pack()

btn3 = Button(root, padx=10 , pady = 5, text = "button03")
btn3.pack()

btn4 = Button(root, width=10, height=3, text ="button04")
btn4.pack()

btn5 = Button(root, fg = "red", bg= "yellow", text = "button05")
btn5.pack()

def btncmd():
    print("button wurd gedruckt")

btn7 = Button(root, text = "동작하는 버튼", command=btncmd)
btn7.pack()

#width, height = 변경불가 확정, padx, pady는 자동변경 가능, 여백정도로 이해 

root.mainloop()