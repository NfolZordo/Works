from tkinter import *





def one_sv():
    b_1sv.grid_forget()
    b_2sv.grid_forget()
    l_nsm.grid(row=0, column=1, sticky=W)
    l_tz.grid(row=1, column=1, sticky=W)
    e_nsm.grid(row=0, column=0)
    e_tz.grid(row=1, column=0)
    b_ob1.grid(row=4, column=1, sticky=W)
def two_sv():
    b_1sv.grid_forget()
    b_2sv.grid_forget()
    l_nsm.grid(row=0, column=1, sticky=W)
    l_tz.grid(row=1, column=1, sticky=W)
    l_lsv.grid(row=2, column=1, sticky=W)
    e_nsm.grid(row=0, column=0)
    e_tz.grid(row=1, column=0)
    e_lsv.grid(row=2, column=0)
    b_ob2.grid(row=3, column=1, sticky=W)

def assing1():
    nsm = int(e_nsm.get())
    tz = int(e_tz.get())

    rez=int(tz/0.8)*nsm

    l_rez.config(text=rez)
    l_rez.grid(row=4, column=0)

def assing2():
    nsm = int(e_nsm.get())
    tz = int(e_tz.get())
    lsv =int(e_lsv.get())
    nmms=int(lsv/5)        #кількість машин між світлофорами
    rez=int(tz/0.8)*nsm
    if nmms < rez: 
        rez=rez-(1*nsm)
    l_rez.config(text=rez)
    l_rez.grid(row=4, column=0)


root = Tk()

root.title("Сreating an array")
root.geometry("720x240+500+300")

l_nsm = Label(text="Кiлькiсть смуг", padx=15, pady=10)
l_tz = Label(text="Час доки світить зелений(сек)", padx=15, pady=10)
l_nsv = Label(text="Кількість світлофорів", padx=15, pady=10)
l_lsv = Label(text="Відстань між світлофорами(м)", padx=15, pady=10)
l_rez = Label(text="", padx=15, pady=10)

e_nsm = Entry(width=10)
e_tz = Entry(width=10)
e_nsv = Entry(width=10)
e_lsv = Entry(width=10)

b_ob1 = Button(text="Обрахувати",command =assing1, width=20)
b_ob2 = Button(text="Обрахувати",command =assing2, width=20)
b_1sv = Button(text="1 Світлофор",command =one_sv, width=20)
b_1sv.grid(row=0, column=0, sticky=W)
b_2sv = Button(text="2 світлофори",command =two_sv, width=20)
b_2sv.grid(row=0, column=1, sticky=W)





root.mainloop()