import math

while True:
    menu = int(input(  "Ведіть номер задачі: 46,56,38,48,58,41,51,33,43,64: 999 для заверщення роботи "))
    if menu == 36:
        a = input("а =  ")
        b = input("b =  ")
        c = input("c =  ")

        if (a < b):
            if (b < c):
                print("Виконується " + "\n")
            else:
                print("Ні" + "\n")
        else:
            print("Ні" + "\n")

    if menu == 46:
        x = float(input("x =  "))
        y = float(input("y =  "))

        if x < 0 and y < 0:
            x = abs(x)
            y = abs(y)
        elif (x < 0 and y >= 0) or (x >= 0 and y < 0):
            x = x * 0.5
            y = y * 0.5
        elif (x >= 0 and y >= 0) or (x < 0.5 and y < 0.5) or (x > 2 and y > 2) or (x < 0.5 and y > 2) or (x > 0.5 and y < 2):
            x = x * 10
            y = y * 10
        print("x = " + str(x) + "\n")
        print("y = " + str(y) + "\n")

    if menu == 56:
        x = float(input("x =  "))
        y = float(input("y =  "))
        a = float(input("a =  "))
        b = float(input("b =  "))
        c = float(input("c =  "))

        if (x > a and y > b) or (x > a and y > c) or (x > b and y > a) or (x > b and y > c) or (x > c and y > a) or (
                x > c and y > b):
            print("Пройде " + "\n")
        else:
            print("Hi")

    if menu == 38:
        x = float(input("x =  "))
        y = float(input("y =  "))

        if x > y:
            z = x - y
        else:
            z = y - x + 1
            print("Z= " + str(z) + "\n")
    if menu == 48:

        a = float(input("a =  "))
        b = float(input("b =  "))
        c = float(input("c =  "))

        d = b * b - 4 * a * c

        if d<0:
            print("Коренiв не iснує  " + "\n")
        else:
            x1 = ((-b + math.sqrt(d))/2)
            x2 = ((-b - math.sqrt(d))/2)
            print("x1=  " + str(x1)+"\n")
            print("x2=  " + str(x2)+"\n")
    if menu == 58:
        pit = int(input(  "Виберіть завдання вшд 1 до 4 "))
        if pit == 1:
            x = float(input("a =  "))


            if x < 0:
                y = -x
            else:
                y = -(x * x)

            print("f(a)=  " + str(y) + "\n")

        if pit == 2:
            x = float(input("a =  "))

            if x < -1:
                y = -(1 / (x * x))
            elif -1 <= x <= 2:
                y = (x * x)
            else:
                y = 4
            print("f(a)=  " + str(y) + "\n")

        if pit == 3:
            x = float(input("a =  "))

            if x < -1:
                y = -x-1
            elif -1 <= x <= 0:
                y = x-1
            elif 0 < x < 1:
                y = -x+1
            else:
                y = x+1
            print("f(a)=  " + str(y) + "\n")

        if pit == 4:
            x = float(input("a =  "))

            if x < 0:
                y = -x
            elif 0 <= x <= 1:
                y = x
            elif 1 < x <= 2:
                y = 1
            else:
                y = -x * 0.5
            print("f(a)=  " + str(y) + "\n")

    if menu == 41:
        x = float(input("x =  "))
        y = float(input("y =  "))
        z = float(input("z =  "))

        if 1 < x < 3:
            print("x=  " + str(x) + "\n")
        if 1 < y < 3:
            print("y=  " + str(y) + "\n")
        if 1 < z < 3:
            print("z=  " + str(z) + "\n")

    if menu == 51:
        import math

        a = float(input("a =  "))
        b = float(input("b =  "))
        c = float(input("c =  "))
        # bx4+bx2+c=0

        d = b * b - 4 * a * c

        if d < 0:
            print("Коренiв не iснує  " + "\n")
        else:
            y1 = ((-b + math.sqrt(d)) / 2)
            y2 = ((-b - math.sqrt(d)) / 2)
            if y1 >= 0:
                x1 = math.sqrt(y1)
                x2 = -math.sqrt(y1)
            if y2 >= 0:
                x3 = math.sqrt(y2)
                x4 = -math.sqrt(y2)
            else:
                print("Коренiв не iснує  " + "\n")

            print("x1=  " + str(x1))
            print("x2=  " + str(x2))
            print("x3=  " + str(x3))
            print("x4=  " + str(x4))
    if menu == 33:
        pit = int(input(  "Виберіть завдання вшд 1, 2, 3 "))

        if pit == 1:
            x = float(input("x =  "))
            y = float(input("y =  "))

            print("max=  " + str(max(x,y)))

        if pit == 2:
            x = float(input("x =  "))
            y = float(input("y =  "))

            print("min=  " + str(min(x,y)))
 
        if pit == 3:
            x = float(input("x =  "))
            y = float(input("y =  "))

            print("max=  " + str(max(x,y)))
            print("min=  " + str(min(x,y)))
    if menu == 43:
        a = float(input("a =  "))
        b = float(input("b =  "))
        c = float(input("c =  "))

        if a >= 0:
            print("a=  " + str(a))
        if b >= 0:
            print("b=  " + str(b))
        if c >= 0:
            print("c=  " + str(c))



    if menu == 64:
        x = int(input("n =  "))

        print("Кілкість сотень  " + str(x//100))

        74
        n = int(input("n =  "))
        if n == 1:
            print(str(n) + " рік")
        elif 1 < n < 10:
            print(str(n) + " роки")
        elif 1 < n < 10:
            print(str(n) + " років")
    if menu == 999:
        break
