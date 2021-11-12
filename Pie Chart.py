from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plot

root = Tk()
root.title("Pie Chart Creater")
root.geometry('400x220')
root.resizable(False, False)

Label(root, text="Create Your Pie Chart", font=('arial', 15
                    , 'bold', 'italic'), fg='black', bg='lime').pack(pady=5, fill=X)
Label(root, text='Enter the Values Below').pack()
v = Entry(root, width=50, bg='systembuttonface')
v.pack(pady=4)
Label(root, text='Enter The Labels Below').pack()
l = Entry(root, width=50, bg='systembuttonface')
l.pack(pady=4)
Label(root, text='Enter The Title Of the Pie Chart Below').pack()
title = Entry(root, width=50, bg='systembuttonface')
title.pack(pady=4)


def Pie_Chart():
    value = v.get()
    label = l.get()
    values = list(value.split(','))
    labels = list(label.split(','))

    if len(value) == 0:
        ValueError(messagebox.showerror('Pie Chart', 'Values Not Entered'))
    elif len(label) == 0:
        ValueError(messagebox.showerror('Pie Chart', 'Labels Not Entered'))
    else:
        plot.pie(values, labels=labels)
        plot.title(title.get())
        if len(title.get()) != 0:
            messagebox.showinfo('Pie Chart', 'Pie Chart Generated, \n Click OK To View The Chart')
            plot.show()
        else:
            messagebox.showwarning('Pie Chart', 'Title Is Not Spesified! Continue Anyway?')
            plot.show()
    
    

    v.delete(0,END)
    l.delete(0,END)
    title.delete(0, END)


Button(root, command=Pie_Chart, text='Generate', activebackground='lime').pack()

root.mainloop()
