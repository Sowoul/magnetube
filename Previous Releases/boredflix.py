# The complete, and for now, the final version of boredflix, with no external downloads required, other than the libraries themselives of course,
# its faster, cleaner and easier than any other streaming software that i use, which was the goal.
# For now, it only supports linux deb based systems.
from urllib.request import Request, urlopen
import re
import webbrowser
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import os
from tkinterweb import HtmlFrame
import webview
import sys
import subprocess
#-------------------------------------------------------run torrent-stream-server serve in terminal------------------------------------------------------------
a=0
# os.chdir('C:\\Users\\ojasw\\Desktop\\C\\movitime')
root=Tk() 
root.title('BoredFlix')
root.option_add("*tearOff", False)
root.resizable(False,False)
root.geometry('800x600')
style = ttk.Style(root)
root.tk.call("source", "proxttk-dark.tcl")
style.theme_use("proxttk-dark")
Desired_font = tkinter.font.Font(family="Ciutadella Rounded",size=15)
d = tk.IntVar(value=2)
frame1 = ttk.Frame(root, padding=(30,0,0,10))
frame1.grid(row=0, column=1, padx=0, pady=(100,10), sticky="nsew", rowspan=3)
frame1.columnconfigure(index=0, weight=1)
# p1=PhotoImage(file='icon.png')
# root.iconphoto(False, p1)
text2 = ttk.Label(frame1, text="",font="colortube" ,justify="center",foreground="white")
text2.grid(row=0, column=0, pady=25, columnspan=2)
text1 = ttk.Label(frame1, text="B o r e d F l i x",font="Davinci 23" ,justify="center",foreground="white")
text1.grid(row=1, column=0, pady=25, columnspan=2)
cond=1
buttonFont = font.Font(family='colortube', size=16, weight='bold')

def desp(x):
    mylabel=Label(frame1,text=x)
    mylabel.grid()
    Desired_font = tkinter.font.Font(family="DAVINCI",size=12)
    mylabel.configure(font=Desired_font)
cond=1
box = ttk.Entry(frame1)
box.insert(0,'')
box.grid(row=2, column=0, padx=190, pady=0, sticky="ew")
play=2
def entry(movie):
    a=5
    frame2 = ttk.Frame(root, padding=(0, 0, 0, 10))
    frame2.grid(row=0, column=1, padx=0, pady=(100, 10), sticky="nsew", rowspan=3)
    frame2.columnconfigure(index=0, weight=1)
    text3 = ttk.Label(frame2, text="", font="colortube", justify="center", foreground="white")
    text3.grid(row=0, column=0, pady=33, columnspan=2)
    def desp2(x):
        mylabel = Label(frame2, text=x)
        mylabel.grid()
        Desired_font = tkinter.font.Font(family="colortube", size=12)
        mylabel.configure(font=Desired_font)
        yts
    ytsmov=movie.replace(' ',"-")
    movie=movie.replace(' ','%20')  
    pmovie=movie.replace(' ','+') 
    def sarc(movie):
        try:
            shreetama=1
            f=Request("""YOUR MOVIE SOURCE HERE""", headers={'User-Agent': 'Mozilla/5.0'})
            f=urlopen(f).read().decode()
            f=re.split('<a href="magnet:',f)
            stop1=re.search('"',f[1])
            play=1  
            pirate1='magnet:'+str((f[1])[:stop1.start()])
            magnet = 'magnet:' + str((f[1])[:stop1.start()])
            # magnet = 'https://webtor.io/#/' + magnet
            webview.create_window('BoredFlix: By OjaShree <3', f'http://127.0.0.1:3000/play?torrent={magnet}',width=1080, height=720)
            webview.start(gui='cef')
        except:
            sarc2(movie)
    def sarc2(movie):
        try:
            shreetama=1
            f=Request(f'https://piratebay.party/search/{movie}/1/99/0', headers={'User-Agent': 'Mozilla/5.0'})
            f=urlopen(f).read().decode()
            f=re.split('<a href="magnet:',f)
            stop1=re.search('"',f[1])
            play=1 
            pirate1='magnet:'+str((f[1])[:stop1.start()])
            magnet = 'magnet:' + str((f[1])[:stop1.start()])
            # magnet = 'https://webtor.io/#/' + magnet
            webview.create_window('BoredFlix: By OjaShree <3', f'http://127.0.0.1:3000/play?torrent={magnet}',width=1080, height=720)
            webview.start(gui='cef')

        except:
            sarc(movie)
    try:
        # shreetama=1
        # f=Request(f'https://piratebay.party/search/{movie}/1/99/0', headers={'User-Agent': 'Mozilla/5.0'})
        # f=urlopen(f).read().decode()
        # f=re.split('<a href="magnet:',f)
        # stop1=re.search('"',f[1])
        sarc(movie)
        # play=1
    except IndexError:
        pass
    try:
        frame1.grid_forget()
        try:
            yts=Request(f'https://wwy.yts.vc/?s={movie}', headers={'User-Agent': 'Mozilla/5.0'})
            # yts=urlopen(yts).read().decode()
            # yts=re.split('<a class="magnet-download" href="magnet:',yts)
            # ytstop=re.search('"',yts[1])
            # shreetama=2
        except:
            pass
    except IndexError:
        pass
    try:
        # pirate1='magnet:'+str((f[1])[:stop1.start()])
        # magnet = 'magnet:' + str((f[1])[:stop1.start()])
        # # magnet = 'https://webtor.io/#/' + magnet
        # webbrowser.open(magnet)
        a=1 
        def ytscom():
            pass
            # magnet = 'magnet:' + str((yts[1])[:ytstop.start()])
            # webbrowser.open(magnet)
        def change_to_f1():
           frame1.grid(row=0, padx=0, pady=(100,10))
        desp2('Stuttering/buffering issues?')
        desp2('Try using another seed')
        button2 = ttk.Button(frame2, text="Switch seed", style="AccentButton", command=ytscom,width=20)
        button2.grid(row=20, column=0, padx=270, pady=10, sticky="nsew")
        button3 = ttk.Button(frame2, text="Search more movies", style="AccentButton", command=change_to_f1,width=20)
        button3.grid(row=21, column=0, padx=270, pady=10, sticky="nsew")
    except:
        pass
    # if a!=1:
        #  try:
        # #     yts1='magnet:'+str((yts[1])[:ytstop.start()])
        # #     magnet = 'magnet:' + str((yts[1])[:ytstop.start()])
        # #     magnet = 'https://webtor.io/#/' + magnet
        # #     webbrowser.open(magnet)
        # #     cond=1
        # except:
        #     desp2('No valid magnets were found')
    # def pirate():
    #     magnet = 'magnet:' + str((f[1])[:stop1.start()])
    #     magnet='https://webtor.io/#/'+magnet
    #     webbrowser.open(magnet)
    #
    # def ytscom():
    #     magnet = 'magnet:' + str((yts[1])[:ytstop.start()])
    #     magnet = 'https://webtor.io/#/' + magnet
    #     webbrowser.open(magnet)
    # if cond == 2:
    #     button1 = ttk.Button(frame1, text="Piratebay seed", style="AccentButton",command=pirate)
    #     button1.grid(row=15, column=0, padx=300, pady=10, sticky="nsew")
    #     button2 = ttk.Button(frame1, text="YTS seed", style="AccentButton",command=ytscom)
    #     button2.grid(row=20, column=0, padx=300, pady=5, sticky="nsew")
    root.mainloop()
def search():
    a=box.get()
    entry(a)
myFont=font.Font(family="DAVINCI")
button1 = Button(frame1, text="Search",style="AccentButton",command=search)

button1.grid(row=10, column=0, padx=300, pady=10, sticky="nsew")

root.bind('<Return>',lambda event:search())
root.mainloop()
