import pyautogui

import tkinter as tk

from tkinter import filedialog

r1 = tk.Tk()

canvas1 = tk.Canvas(r1,width=300,height=300)

canvas1.pack()

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    
    myScreenshot.save(file_path)
    


myButton = tk.Button(text="Take Screenshot",command=takeScreenshot,bg='green',fg='white',font=10)

canvas1.create_window(150,150,window=myButton)


r1.mainloop()