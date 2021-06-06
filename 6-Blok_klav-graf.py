import os
from tkinter import *
import time
 
 
menu = [("Згорнути всі вікна", 1), ("Блокування клавіатури і миші", 2)]
format = [("Секунди", 1), ("Хвилини", 2), ("Години", 3)]
def time_in(tymer):
    local_time = float(time.time())
    tymer2 = local_time+tymer

    a = 0
    while (a == 0):
       local_time = float(time.time())
       if local_time >= tymer2:
            a= 1
            os.system("%windir%\explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}")
       time.sleep(5)
       #-------------------------------------------------
def sleep(tymer):
    local_time = float(time.time())
    tymer2 = local_time+tymer

    a = 0
    while (a == 0):
       local_time = float(time.time())
       if local_time >= tymer2:
            a= 1
            windll.user32.BlockInput(True)
            tm = 0
            while(tm != sleept):
                tm += 1
                time.sleep(1)
                keyboard.add_hotkey('Ctrl + 1', lambda: windll.user32.BlockInput(False))

            windll.user32.BlockInput(False)
       time.sleep(5)

        #----------------------------------------------------------------
def select():
    l = lan.get()

    if l == 1:        #Згорнути всі вікна
        lan2 = IntVar()
        row=1
        for txt, val in format:
            Radiobutton(text=txt,width=30, value=val, variable=lan2, padx=15, pady=10, command=format_t)\
                .grid(row=row, sticky=W)
            row += 1
    elif l == 2:                                    #блок  
        lan2 = IntVar()
        row=1
        for txt, val in format:
            Radiobutton(text=txt,width=30, value=val, variable=lan2, padx=15, pady=10, command=format_t)\
                .grid(row=row, sticky=W)
            row += 1
#---------------------------------------
def time_in_1():
    global message_entry 
    tymer = int(message_entry.get())
    time_in(tymer)
def time_in_2():
    global message_entry 
    tymer = int(message_entry.get()) *60
    time_in(tymer)
def time_in_3():
    global message_entry 
    tymer = int(message_entry.get()) * 60 * 60
    time_in(tymer)
def time_in_4():
    global message_entry 
    tymer = int(message_entry.get())
    sleep(tymer)
def time_in_5():
    global message_entry 
    tymer = int(message_entry.get()) *60
    sleep(tymer)
def time_in_6():
    global message_entry 
    tymer = int(message_entry.get()) * 60 * 60
    sleep(tymer)

def format_t():
    l = lan.get()
    if l == 1:                       
        global message_entry 
        message_entry = Entry()
        message_entry.place(relx=.5, rely=.1, anchor="c")
        message_button = Button(text="Next", command=time_in_1)
        message_button.place(relx=.5, rely=.5, anchor="c")
 
    elif l == 2:                                  
        message_entry = Entry()
        message_entry.place(relx=.5, rely=.1, anchor="c")
        message_button = Button(text="Next", command=time_in_2)
        message_button.place(relx=.5, rely=.5, anchor="c")
    elif l == 3:                                  
        message_entry = Entry()
        message_entry.place(relx=.5, rely=.1, anchor="c")
        message_button = Button(text="Next", command=time_in_3)
        message_button.place(relx=.5, rely=.5, anchor="c")
def format_t2():
    l = lan.get()
    if l == 1:                       
        global message_entry 
        message_entry = Entry()
        message_entry.place(relx=.5, rely=.1, anchor="c")
        message_button = Button(text="Next", command=time_in_4)
        message_button.place(relx=.5, rely=.5, anchor="c")
 
    elif l == 2:                                  
        message_entry = Entry()
        message_entry.place(relx=.5, rely=.1, anchor="c")
        message_button = Button(text="Next", command=time_in_5)
        message_button.place(relx=.5, rely=.5, anchor="c")
    elif l == 3:                                  
        message_entry = Entry()
        message_entry.place(relx=.5, rely=.1, anchor="c")
        message_button = Button(text="Next", command=time_in_6)
        message_button.place(relx=.5, rely=.5, anchor="c")


#------------------------------------------- 
root = Tk()
root.title("GUI на Python")
root.geometry("600x300")
 
header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)
 
lan = IntVar()
 
row = 1
for txt, val in menu:
    Radiobutton(text=txt, value=val, variable=lan, padx=15, pady=10, command=select)\
        .grid(row=row, sticky=W)
    row += 1
 
sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)
 
root.mainloop()
