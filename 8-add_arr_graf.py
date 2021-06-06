from tkinter import *
import numpy as np
import time 
import os
#from tkinter import filedialog

size_arr = [("10", 1), ("100", 2), ("1000", 3), ("10000", 4),("1000000000",5),("Своє зеачення",6)]
avt_arr = [("Ручне введенян",1),("Автоматичну заповнення",2)] 
form_arr = [("Цілі числа",1),("Дробові числа",2),("Символи",3)] 
dimstat_arr = [("Динамічний масив",1),("Статичний масив",2)] 

def select_si():
    global num
    global y
    l = size_arr_val.get()
    if l == 1:
        num=10
    elif l == 2:
        num=100
    elif l == 3:
        num=1000
    elif l == 4:
        num=10000
    elif l == 5:
        num=1000000000
    elif l == 6:
        if size_arr_entry.get()=="": num = 1
        else: num = int(size_arr_entry.get())
        
def si():
    l = size_arr_val.get()

    if l == 6:
        size_arr_entry.grid(column=0, row=7, padx=6, pady=6)
        

def delet():
    header1.grid_forget()
    header2.grid_forget()
    header3.grid_forget()
    cont_button.grid_forget()
    size_arr_entry.grid_forget()


def assing():
    global avt
    global num
    global arr
    global form
    global y
    avt = avt_arr_val.get()
    form = form_arr_val.get()
    hand_button.grid_forget()
    stat_button.grid_forget()
    save_button.grid_forget()
    ops_button.grid_forget()
    header4.grid_forget()
    header5.grid_forget()
    hand_arr_entry.grid_forget()
    select_si()
    y=-1
    if avt == 1:

        if form == 1 :
            arr  = np.array(range(num), int)

        if form == 2 :
            arr  = np.array(range(num), float)

        if form == 3 :
     #           arr = np.chararray(num)
            arr = np.array(['a' for _ in range(num)])
    prin()

    
global y
y=-1
def prin():
    global form
    global avt
    
    start_time = time.time()
    avt = avt_arr_val.get()
    size_arr_entry.grid_forget()
    select_si()
    form = form_arr_val.get()
    global hand_n
    global num
    global y
    global arr
    global timer
    if avt ==2:
        if form == 1 :
            arr=np.random.randint(100,999,num)
        if form == 2 :
            arr=np.random.rand(num)
        if form == 3 :
            arr2=np.random.rand(num)
            arr2=arr2*100
            arr2 = arr2.astype(np.int64)
            arr = np.chararray(num)
            for i in range(0,num): 
                arr[i]= chr(arr2[i])
       
    if avt == 1:
        if form == 1 :
            if hand_arr_entry.get()=="": hand_n = 0
            else: hand_n = int(hand_arr_entry.get())

        if form == 2 :
            if hand_arr_entry.get()=="": hand_n = 0
            else: hand_n = float(hand_arr_entry.get())

        if form == 3 :
 #           arr = np.chararray(num)
            if hand_arr_entry.get()=="": hand_n = ""
            else: hand_n = str(hand_arr_entry.get())
        hand_arr_entry.grid_forget()
        hand_arr_entry.grid(column=2, row=7, padx=6, pady=6)
        header4.grid(row=5, column=2, sticky=W)
        header5.grid(row=6, column=2, sticky=W)
        hand_button.grid(row=2, column=3, padx=1, pady=1) 
        arr[y] = hand_n
        y=y+1

    if avt == 1 and y==num:
        stat_button.grid(row=3, column=3, padx=1, pady=1)
        save_button.grid(row=4, column=3, padx=1, pady=1)
        ops_button.grid(row=5, column=3, padx=1, pady=1)
        hand_button.grid_forget()

    if avt == 2:
        stat_button.grid(row=3, column=3, padx=1, pady=1)
        save_button.grid(row=4, column=3, padx=1, pady=1)
        ops_button.grid(row=5, column=3, padx=1, pady=1)

    timer = round((time.time() - start_time),4)

def out():
    global num
    global y
    global arr
    global form
    if form == 1 :
        a=[1]
        arr2=np.array(a)
    if form == 2 :
        b=[1.1]
        arr2=np.array(b)
    if form == 3 :
        c="o"
        arr2=np.array(c)
    for i in range(num):
        if i==0: arr2[0]=arr[0]
        else:arr2 = np.append(arr2,arr[i])
    header6.config(text=arr2)
    header6.grid(row=9, column=0, columnspan=3, sticky=W)

def stat_out():
    global timer
    global arr
    header6.config(text=("Час-",timer,",Розмір", (arr.itemsize*arr.size),",Тип", arr.dtype ))
    header6.grid(row=9, column=0, columnspan=3, sticky=W)

def save_out():
    global timer
    global arr
#    filename = filedialog.asksaveasfile(title='save')
    f = open("stat.txt",'a')
#   f.readline()
    f.write(("Кількість елементів "+str(arr.size)+" Час створення маcиву: "+str(timer)+"c ,Його розмір "+ str(arr.itemsize*arr.size)+"байт, Тип "+ str(arr.dtype) ) + '\n')
    arr = np.array(0,arr.dtype)
    f.close()

def ops_out():
    os.system("stat.txt")

root = Tk()

root.title("Сreating an array")
root.geometry("720x240+500+300")
#root.resizable(width=False, height=False)

header1 = Label(text="Виберіть розмірність масиву:", padx=15, pady=10)
header1.grid(row=0, column=0, sticky=W)
header2 = Label(text="Виберіть спосіб заповнення:", padx=15, pady=10)
header2.grid(row=0, column=1, sticky=W)
header3 = Label(text="Виберіть тип значень:", padx=15, pady=10)
header3.grid(row=0, column=2, sticky=W)
header4 = Label(text="Введіть елемінт i")
header5 = Label(text="натисніть Enter")
header6 = Label(text="")

size_arr_val = IntVar()
avt_arr_val = IntVar()
form_arr_val = IntVar()
cont_button = Button(text="Створити масив",command =assing, width=20)
hand_button = Button(text="Ввести наступне",command =prin, width=20)
stat_button = Button(text="Показати статистику",command =stat_out, width=20)
save_button = Button(text="Зберегти статистику",command =save_out, width=20)
ops_button = Button(text="Відкрити статистику",command =ops_out, width=20)
size_arr_entry = Entry(width=25)
hand_arr_entry = Entry(width=10)
cont_button.grid(row=1, column=3,columnspan=1, padx=1, pady=1) 
row = 1

for txt, val in size_arr:
    Radiobutton(text=txt, value=val, variable=size_arr_val,command=si, padx=15, pady=1)\
                .grid(row=row, sticky=W)
    row += 1


row =1
for txt, val_av in avt_arr:
    Radiobutton(text=txt, value=val_av, variable=avt_arr_val, padx=15, pady=1)\
                .grid(row=row, column=1, sticky=W)
    row += 1
row =1
for txt, val_form in form_arr:
    Radiobutton(text=txt, value=val_form, variable=form_arr_val, padx=15, pady=1)\
                .grid(row=row, column=2, sticky=W)
    row += 1
row =1
 
root.mainloop()