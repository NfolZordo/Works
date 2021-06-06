from tkinter import *
import numpy as np
import random
from PIL import Image, ImageTk, ImageDraw  #Подключим необходимые библиотеки. 
from tkinter import filedialog
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

def open_img():
    btn.grid_forget()
    global x 
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel= Label(root, image=img)
    panel.image = img
    panel.grid(row=2, column=1, padx=5, pady=5)
    btn2.grid(row=1, column=1, padx=5, pady=5)


def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


def qwe():
    global x
    #mode = int(input('mode:')) #Считываем номер преобразования. 
    imageO = Image.open(x) #Открываем изображение. 
    draw = ImageDraw.Draw(imageO) #Создаем инструмент для рисования. 
    width = imageO.size[0] #Определяем ширину. 
    height = imageO.size[1] #Определяем высоту. 	
    pix = imageO.load() #Выгружаем значения пикселей.
    pixarr = np.array(imageO)
    xyi=pixarr.shape
    shap = int(np.prod(xyi)/3)
    pixarr.shape=(shap,3)
    pixarr2 = np.unique(pixarr, axis=0)
    differ = pixarr.shape[0] - pixarr2.shape[0]
    sa = 0
    sb = 0
    sc = 0

    for i in range(width):
        for j in range(height):
#-------------------------------------------------------
            a = pix[i, j][0]
            sa += a
            b = pix[i, j][1]
            sb += b
            c = pix[i, j][2]
            sc += c
            
    return(sa,sb,sc,differ,draw,imageO)
    #		S = (a + b + c) // 3
    #		draw.point((i, j), (S, S, S))
    #image.save("c:\\Python\\tx2.jpg", "JPEG")
#--------------------------------------------------------
    del draw


def Graf():
    global x
    sa,sb,sc,differ,draw,imageO= qwe()
    del draw
    data_names = ['Червоний', 'Зелений', 'Синій']
    data_values = [sa, sb, sc]

    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
    mpl.rcParams.update({'font.size':20})

    xs = range(len(data_names))

    plt.pie(
        data_values, autopct='%.1f', radius = 1.5,colors=('r','g','b'))
    fig.savefig('pie.png')

    img = Image.open('pie.png')
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel2 = Label(root, image=img)
    panel2.image = img
    btn2.grid_forget()
    KLSK.grid(row=1, column=2, padx=5, pady=5)
    KLOR.grid(row=1, column=1, padx=5, pady=5)
    panel2.grid(row=2, column=2, padx=5, pady=5)
    Kkoe = Label(text='Кіл. однак. елем. ' + str(differ) ,font="Arial 12")
    Kkoe.grid(row=3, column=1, padx=5, pady=5)
    btnmenu.grid(row=1, column=3, padx=5, pady=5)


    os.remove('pie.png')
def Menu():
    btngray.grid(row=1, column=4, padx=5, pady=5)
    btnsep.grid(row=1, column=5, padx=5, pady=5)
    btnneg.grid(row=1, column=6, padx=5, pady=5)
    btnnoi.grid(row=1, column=7, padx=5, pady=5)
    btnbw.grid(row=1, column=8, padx=5, pady=5)

    
def Gray():
    sa,sb,sc,differ,draw,imageO= qwe()
    width = imageO.size[0] #Определяем ширину. 
    height = imageO.size[1] #Определяем высоту. 	
    pix = imageO.load() #Выгружаем значения пикселей.
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))
    img = imageO
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel= Label(root, image=img)
    panel.image = img
    panel.grid(row=3, column=1, padx=5, pady=5)
    del draw

def Sep():
    sa,sb,sc,differ,draw,imageO= qwe()
    width = imageO.size[0] #Определяем ширину. 
    height = imageO.size[1] #Определяем высоту. 	
    pix = imageO.load() #Выгружаем значения пикселей.
    depth = 40
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))    
    img = imageO
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel= Label(root, image=img)
    panel.image = img
    panel.grid(row=3, column=1, padx=5, pady=5)
    del draw
def Neg():
    sa,sb,sc,differ,draw,imageO= qwe()
    width = imageO.size[0] 
    height = imageO.size[1] 
    pix = imageO.load() 
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))    
    img = imageO
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel= Label(root, image=img)
    panel.image = img
    panel.grid(row=3, column=1, padx=5, pady=5)
    del draw
def Noi():
    sa,sb,sc,differ,draw,imageO= qwe()
    width = imageO.size[0] 
    height = imageO.size[1] 
    pix = imageO.load() 
    factor = 50
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    img = imageO
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel= Label(root, image=img)
    panel.image = img
    panel.grid(row=3, column=1, padx=5, pady=5)
    del draw
def Bw():
    sa,sb,sc,differ,draw,imageO= qwe()
    width = imageO.size[0] 
    height = imageO.size[1] 
    pix = imageO.load() 
    factor = 10
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    img = imageO
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel= Label(root, image=img)
    panel.image = img
    panel.grid(row=3, column=1, padx=5, pady=5)
    del draw



root = Tk()
root.geometry("1100x600+200+50")
root.resizable(width=True, height=True)
btn = Button(root, text='Відкрити зобрпження',font="Arial 16", command=open_img)
btn.grid(row=1, column=1, padx=250, pady=300)
btn2 = Button(root, text='Провести аналіз', command=Graf)
KLSK = Label(text='Cпіввідношшення кольорів',font="Arial 16")
KLOR = Label(text='Оригінал',font="Arial 16")
btnmenu = Button(root, text='Редагувати зображення', command=Menu)
btngray = Button(root, text='Віддінки сірого', command=Gray)
btnsep = Button(root, text='Сепія', command=Sep)
btnneg = Button(root, text='Негатив', command=Neg)
btnnoi = Button(root, text='Шуми', command=Noi)
btnbw = Button(root, text='Чорно-біле', command=Bw)

root.mainloop()


