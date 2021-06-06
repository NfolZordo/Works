import time
import os
import platform

system = (platform.system())
menu = int(input(  "Виберіть дію: 1-Сон 2-Виключення 3-Перезагрузка "))
yorch = int(input(  "Ви бажаєте виконати дію: 1-У заданий час, 2-Через заданий час "))
if yorch == 2:
    format = int(input(  "ВИберіть формат таймера: 1-Секунди 2-Хвилини 3-Години "))
    tymer = int(input(  "ВИберіть через який час відбудиться вибрана дія "))
    if format == 2: tymer = tymer * 60
    elif format == 3: tymer = tymer * 60 * 60
    local_time = float(time.time())
    tymer2 = local_time+tymer

    a = 0
    while (a == 0):
       local_time = float(time.time())
       if local_time >= tymer2:
            a= 1
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
       time.sleep(10)

if yorch == 1:
    HZ = int(input("Виберіть години "))
    MZ = int(input("Виберіть хвилинм "))
    H = int(time.strftime("%H "))
    if H> 23: H-=24
    q=0
    if H > HZ: q=1
    a = 0
    while (a == 0):
        H = int(time.strftime("%H "))
        if H > 23: H -= 24
        if H == 0: q = 0
        M = int(time.strftime("%M ", time.gmtime()))
        if H >= HZ and M >= MZ and q == 0:
            a= 1
            if menu == 1:
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
        time.sleep(10)

