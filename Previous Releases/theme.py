#Raw theme used in the project.
import tkinter as tk
from tkinter import ttk
import os
os.chdir('C:\\Users\\ojasw\\Downloads\\Create-main\\Create-main')
root = tk.Tk()
root.title("hope")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False)
root.geometry("1000x600")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)
style = ttk.Style(root)
root.tk.call("source", "proxttk-dark.tcl")
style.theme_use("proxttk-dark")

d = tk.IntVar(value=2)
frame1 = ttk.Frame(root, padding=(40,0,0,10))
frame1.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
frame1.columnconfigure(index=0, weight=1)
# Label
text1 = ttk.Label(frame1, text="BoredFlix",font="colortube" ,justify="center",foreground="white")
text1.grid(row=0, column=0, pady=50, columnspan=2)  
# Entry
box = ttk.Entry(frame1)
box.insert(0,'')
box.grid(row=2, column=0, padx=200, pady=0, sticky="ew")
button1 = ttk.Button(frame1, text="Search",style="AccentButton")
button1.grid(row=10, column=0, padx=300, pady=10, sticky="nsew")
root.mainloop()
