from ctypes import windll
from tkinter import *
import keyboard
from infi.systray import SysTrayIcon
import os
import time
systray = SysTrayIcon("D:\test.jpg", "Example tray icon")
systray.start()


class App:
    def __init__(self, master):
        self.master = master

        self.down = Button(master, text="Згорн", command=self.startf)
        self.down.grid()

        self.blok = Button(master, text="Блок клав", command=self.pausef)
        self.blok.grid()

        self.sec_b = Button(master, text="Сек", command=self.sec)
        self.hv_b = Button(master, text="Хв", command=self.hv)
        self.hr_b = Button(master, text="Год", command=self.hr)

        self.tyme_entry = Entry(master,width=25)
        #self.size_arr_entry.grid()

    def sec(self):
        global tymer
        global num
        global local_time
        global tymer2
        global menu
        num = int(self.tyme_entry.get())
        local_time = float(time.time())
        tymer2 = local_time + num
        if menu == 1:
            self.down_win()
        if menu == 2:
            self.block_klav()

    def hv(self):
        global tymer
        global num
        global local_time
        global tymer2
        global menu
        num = int(self.tyme_entry.get())*60
        local_time = float(time.time())
        tymer2 = local_time + num
        if menu == 1:
            self.down_win()
        if menu == 2:
            self.block_klav()

    def hr(self):
        global tymer
        global num
        global local_time
        global tymer2
        num = int(self.tyme_entry.get())*1200
        local_time = float(time.time())
        tymer2 = local_time + num
        if menu == 1:
            self.down_win()
        if menu == 2:
            self.block_klav()


    def time_men(self):
        self.sec_b.grid()
        self.hv_b.grid()
        self.hr_b.grid()
        self.tyme_entry.grid()
    def down_win(self):
        global num
        global a
        global tymer2
        local_time = float(time.time())
        self.master.after(num*1000, self.down_win)
        if a==0 and local_time > tymer2:
            os.system("%windir%\explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}")
            a=1

    def block_klav(self):
        global num
        global a
        global tymer2
        local_time = float(time.time())
        self.master.after(num*1000, self.block_klav)
        if a==0 and local_time > tymer2:
            windll.user32.BlockInput(True)
            a=1
        keyboard.add_hotkey('Q', lambda: windll.user32.BlockInput(False))
        if local_time > tymer2+5:
            windll.user32.BlockInput(False)


    def startf(self):
        global menu
        menu = 1
        self.down.grid_forget()
        self.blok.grid_forget()
        self.time_men()


    def pausef(self):
        global menu
        menu = 2
        self.down.grid_forget()
        self.blok.grid_forget()
        self.time_men()




global a
global tymer
global menu
menu=0
a=0
root = Tk()
myapp = App(root)
root.mainloop()
