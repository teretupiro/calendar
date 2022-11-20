from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry('500x500')

label = Label(root)
label.pack()

def create_event():
    # window=Tk()
    window=Toplevel()
    window.title('New window')
    window.geometry('100x100')
    entry=Entry(window,background='blue')
    entry.pack()

    def click():
        label['text']=entry.get()
        # btn_ok = ttk.Button(window,text='OK',command=click)
        # btn_ok.place(x=50

    btn_ok = ttk.Button(window, text='OK', command=click)
    btn_ok.place(x=50, y=50)

max=28
for y in range(0,5):
    for x in range(1,8):
        if (x+y*7)<=max:
         btn_1=ttk.Button(text=(x+y*7),width=10,command=create_event)
         for y in range(0,5):
             for x in range(1,8):

              btn_1.place(x=0+(x+y*7),y=100+(x+y*7))


root.mainloop()