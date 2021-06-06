import os
from tkinter import *
import time
import platform
system = (platform.system())
menu=0
form_time=0
a=0
tymer2=0

def doit():
    global menu
    if menu == 1:
        if system == "Windows":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif menu == 2:
        if system == "Windows":
            os.system("shutdown /p")
        else:
            os.system("shutdown now -h")
    elif menu == 3:
        if system == "Windows":
            os.system("shutdown /r")
        else: os.system('reboot')


#---------------------------Основа Через-----------------------------
def click_ok_thr_button():
    global form_time
    tymer = int(mess_thr.get())
    global menu
    global a
    global tymer2
    if form_time == 2: 
        tymer = tymer * 60
    elif form_time == 3: 
        tymer = tymer * 60 * 60
    local_time = float(time.time())
    if a == 0 :
        tymer2 = local_time+tymer
        a+=1
    local_time = float(time.time())
    if local_time < tymer2:
         root.after(1000, lambda: click_ok_thr_button())
    if local_time >= tymer2:
        doit()
#---------------------------Основа В------------------------
def click_ok_in_button():
    HZ = int(mess_in_hr.get())
    MZ = int(mess_in_min.get())
    H = int(time.strftime("%H "))
    if H> 23: H-=24
    q=0
    if H > HZ: q=1
    a = 0
    H = int(time.strftime("%H "))
    if H > 23: H -= 24
    if H == 0: q = 0
    M = int(time.strftime("%M ", time.gmtime()))
    if H >= HZ and M >= MZ and q == 0:
        a= 1
        doit()
        sys.exit()
    else:
        root.after(1000, lambda: click_ok_in_button())

#--------------------------------------------------------
def inorth():
    sl_btn.grid_forget()
    vkl_btn.grid_forget()
    rel_btn.grid_forget()
    inti_btn.grid(row=1, column=1, padx=5, pady=5)
    thr_btn.grid(row=1, column=2, padx=5, pady=5)

def click_sl_button():                           #Сон
    global menu
    menu=1
    inorth()
def click_vkl_button():                           #Викл
    global menu
    menu=2
    inorth()
def click_rel_button():                           #Перезап
    global menu
    menu=3
    inorth()


def click_thr_button():                         # Через
    inti_btn.grid_forget()
    thr_btn.grid_forget()
    sec_btn.grid(row=1, column=1, padx=5, pady=5)
    min_btn.grid(row=1, column=2, padx=5, pady=5)
    hr_btn.grid(row=2, column=1, padx=5, pady=5)
def click_inti_button():                         # В
    inti_btn.grid_forget()
    thr_btn.grid_forget()
    mess_in_hr.grid(row=1, column=1, padx=5, pady=5)
    label_in_hr.grid(row=1, column=2, padx=5, pady=5)
    mess_in_min.grid(row=2, column=1, padx=5, pady=5)
    label_in_min.grid(row=2, column=2, padx=5, pady=5)
    ok_in_btn.grid(row=3, column=1, padx=5, pady=5)

def t_del():
    sec_btn.grid_forget()
    min_btn.grid_forget()
    hr_btn.grid_forget()
def click_sec_button():                         # Секунди
    t_del()
    global form_time
    form_time=1
    mess_thr.grid(row=1, column=1, padx=5, pady=5)
    ok_thr_btn.grid(row=1, column=2, padx=5, pady=5)
def click_min_button():                         # Хвилини
    t_del()
    global form_time
    form_time=2
    mess_thr.grid(row=1, column=1, padx=5, pady=5)
    ok_thr_btn.grid(row=1, column=2, padx=5, pady=5)
def click_hr_button():                         # Години
    t_del()
    global form_time
    form_time=3
    mess_thr.grid(row=1, column=1, padx=5, pady=5)
    ok_thr_btn.grid(row=1, column=2, padx=5, pady=5)

root = Tk()
root.title("GUI на Python")
root["bg"] = "#ccc"
root.geometry("300x250")

sl_btn = Button(text="Сон",height=1, width=10, background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_sl_button)
sl_btn.grid(row=1, column=1, padx=5, pady=5)

vkl_btn = Button(text="Вимкненя",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_vkl_button)
vkl_btn.grid(row=1, column=2, padx=5, pady=5)

rel_btn = Button(text="Перезагрузка",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_rel_button)
rel_btn.grid(row=2, column=1, padx=5, pady=5)
inti_btn = Button(text="У заданий час",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_inti_button)
thr_btn = Button(text="Через заданий час",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_thr_button)
sec_btn = Button(text="Секунди",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_sec_button)
min_btn = Button(text="Хвилини",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_min_button)
hr_btn = Button(text="Години",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_hr_button)
ok_thr_btn = Button(text="ok",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_ok_thr_button)
ok_in_btn = Button(text="ok",height=1, width=10, background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", command=click_ok_in_button)
label = Label(text='Виберіть через який час відбудиться вибрана дія', font="Arial "+ "14", bg="#555",fg='#ccc')
label_in_hr = Label(text='Години', font="Arial "+ "14", bg="#ccc",fg="#555")
label_in_min = Label(text='Хвилини', font="Arial "+ "14", bg="#ccc",fg="#555")
mess_thr = Entry()
mess_in_hr = Entry()
mess_in_min = Entry()
 
root.mainloop()