import tkinter as tk
def func():
    if en1.get() == 'user' and en2.get() == 'pass':
        btn.config(background = 'green')
    else:
        btn.config(background = 'red')
win=tk.Tk()
lb1=tk.Label(win,text='user')
en1=tk.Entry(win)
a=en1.get()
lb2=tk.Label(win,text='pass')
en2=tk.Entry(win)
b=en2.get()
btn=tk.Button(win,text='click here',command=func)
lb1.pack()
en1.pack()
lb2.pack()
en2.pack()
btn.pack()

