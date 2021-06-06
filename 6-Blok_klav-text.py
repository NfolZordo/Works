import os
import time
import keyboard


menu = int(input(  "Виберіть дію: 1-Згорнути всі вікна 2-Блокування клавіатури і миші "))
yorch = int(input(  "Ви бажаєте виконати дію: 1-У заданий час, 2-Через заданий час "))
if(menu == 2):
    sleept = int(input(  "На який час (в секундах) буде заблоковано. (Увага до закінчення часу неможливо відмінити)"))

if yorch == 2:
    format = int(input(  "Виберіть формат таймера: 1-Секунди 2-Хвилини 3-Години "))
    tymer = int(input(  "Виберіть через який час відбудиться вибрана дія "))
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
                os.system("%windir%\explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}")
            if menu == 2:
                windll.user32.BlockInput(True)
                tm = 0
                while(tm != sleept):
                    tm += 1
                    time.sleep(1)
                    keyboard.add_hotkey('Ctrl + 1', lambda: windll.user32.BlockInput(False))

                windll.user32.BlockInput(False)
       time.sleep(5)

if yorch == 1:
    HZ = int(input("Виберіть години "))
    MZ = int(input("Виберіть хвилинм "))
    H = int(time.strftime("%H ", time.gmtime()))
    H += 2
    if H> 23: H-=24
    q=0
    if H > HZ: q=1
    a = 0
    while (a == 0):
        H = int(time.strftime("%H ", time.gmtime()))
        H += 2
        if H > 23: H -= 24
        if H == 0: q = 0
        M = int(time.strftime("%M ", time.gmtime()))
        if H >= HZ and M >= MZ and q == 0:
            a= 1
            if menu == 1:
               os.system("%windir%\explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}")
            if menu == 2:
                sleept = int(input(  "На який час (в секундах) буде заблоковано. (Увага до закінчення часу неможливо відмінити)"))
                windll.user32.BlockInput(True)
                time.sleep(sleept)
                windll.user32.BlockInput(False)

        time.sleep(5)

