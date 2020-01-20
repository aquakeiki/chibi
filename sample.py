import sys
from tkinter import Tk, tkinter

root = Tk()
btnframe = ttk.Frame(root)
def button1_clicked():
    print('大吉')
    root.quit()

btn = ttk.Button(btnframe, text = '占ってあげるよ' command=button1_clicked)

btnframe.grid()
btn.grid()

