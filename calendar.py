
from tkinter import*
from tkinter import ttk

root=Tk()
root.geometry('800x400')




# def create_event(index):
#     # window=Tk()
#     window=Toplevel()
#     window.title('New window')
#     window.geometry('100x100')
#     entry=Entry(window,background='blue')
#     entry.pack()

#     # def click():
#     #     global label
#     #     print(entry.get())
#     #     print(btn_1_list[index]['text'])
#     #     # label['text']=entry.get()
#     #     # btn_ok = ttk.Button(window,text='OK',command=click)
#     #     # btn_ok.place(x=50

#     btn_ok = ttk.Button(window, text='OK', command=click)
#     btn_ok.place(x=50, y=50)


week=['|','Mon','Tue','Wed','Thu','Fri','Sat','Sun']
months=['January','February','March','April','May','June','July','August','September','October','November','December']



info_label = Label(root, text='December', width=10, height=1, 
            font=('Verdana', 16, 'bold'), fg='blue')
info_label.place(x=200)

def fill():
    info_label['text'] = months[11] 

    



max=31



for x in range(1,8):
    for y in range(7):
        if (x+y*7)<=max:
            #btn_1_list.append(ttk.Button(text=x+y*7,width=10,command=lambda: create_event(btn_1_list[x+y*7])).place(x=120*x,y=80*y,relx=0.01,rely=0.1))
            
            label = Label(root,bg='grey',fg='darkblue',text=x+y*7, width=6, height=3).place(x=100*x, y=70*y,rely=0.13)
            label_days = Label(justify=CENTER, bg='red',text=week[x], width=6).place(x=100*x,rely=0.07)
            # b_day=Button(text=x+y*7,width=1,height=1,bg='grey').place(x=100*x, y=70*y,rely=0.13)
    
            # for i in week:
            #     for o in range(0,7):

    # # for m in range(0,7):
    # #     for n in range (0,4):
    # #         if x+y*7:
    #          label = Label(root,bg='red',width=7,height=3).place(x=90*m,y=80*n,relx=0.12,rely=0.15)

 

root.mainloop()