
from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry('800x500')



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
week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for y in range(0,5):
    for x in range(1,8):
        if (x+y*7)<=max:
         btn_1=ttk.Button(text=x+y*7,width=10,command=create_event).place(x=90*x,y=80*y,rely=0.1)
         for i in week:
            for o in range(0,7):
             label_day=Label(justify=CENTER,text=week[o],width=9).place(x=90*x,rely=0.05)
    for m in range(0,7):
        for n in range (0,4):
            if x+y*7:
             label = Label(root,bg='red',width=7,height=3).place(x=90*m,y=80*n,relx=0.12,rely=0.15)

 

root.mainloop()