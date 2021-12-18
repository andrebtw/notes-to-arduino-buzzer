from tkinter import *
import tkinter as tk


import constants

def start():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.grid(columnspan=3, rowspan=3)


    root.mainloop()


if __name__=="__main__":
    start()