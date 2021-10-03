import turtle as tl
import math as ms
tl.shape('turtle')

def go(x:float, y:float):
    tl.penup()
    tl.goto(x, y)
    tl.pendown()

def ex3():
    tl.forward(50)
    tl.left(90)
    tl.forward(50)
    tl.left(90)
    tl.forward(50)
    tl.left(90)
    tl.forward(50)
    tl.left(90)

def ex4():
    for i in range(0, 360, 1):
        tl.forward(2*ms.pi*50/360)
        tl.left(1)

def ex5():
    tl.penup()
    tl.goto(-50, -50)
    tl.pendown()
    for i in range(1, 11, 1):
        tl.forward(50 + 20*i)
        tl.left(90)
        tl.forward(50 + 20*i)
        tl.left(90)
        tl.forward(50 + 20*i)
        tl.left(90)
        tl.forward(50 + 20*i)
        tl.left(90)
        tl.penup()
        tl.goto(-50-10*i, -50-10*i)
        tl.pendown()

def ex6():
    n = 11
    for i in range(1, n, 1):
        tl.forward(50)
        tl.stamp()
        tl.left(180)
        tl.forward(50)
        tl.left(180)
        tl.right(360/n)

def ex7():
    for i in range (0, 800, 1):
        tl.forward(2*ms.pi*(i)/360)
        tl.left(5)

def ex8():
    for i in range(0, 20, 1):
        tl.forward(10*i)
        tl.left(90)

def ex9():
    for i in range(3, 20, 1):
        tl.penup()
        tl.goto(10*i, 0)
        tl.pendown()
        tl.left(180-180*(i-2)/(2*i))
        for k in range(1, i+1, 1):
            tl.forward(10*i*(2*ms.sin(ms.pi/i)))
            tl.left(180-(180*(i-2)/i))
        tl.right(180 - 180 * (i - 2) / (2 * i))

def ex10():
    for k in range (1, 4, 1):
        for i in range(0, 360, 5):
            tl.forward(2*ms.pi*500/360)
            tl.left(5)
        for i in range(0, 360, 5):
            tl.forward(2 * ms.pi * 500 / 360)
            tl.right(5)
        tl.right(60)

def ex11():
    tl.right(90)
    for k in range (1, 11, 1):
        for i in range(0, 360, 5):
            tl.forward(2*ms.pi*(250 + 50*k)/360)
            tl.left(5)
        for i in range(0, 360, 5):
            tl.forward(2 * ms.pi * (250 + 50*k) / 360)
            tl.right(5)

def ex12():
    tl.right(90)
    for i in range(0, 360, 5):
        tl.forward(2 * ms.pi * 250 / 360)
        tl.right(5)

#a = "ex" + input() + "()"
#eval(a)

def ex14():
    n = 5
    for i in range(1, n+1, 1):
        tl.forward(100)
        tl.right(180 - 180/n)
    tl.penup()
    tl.goto(200, 0)
    tl.pendown()
    n = 11
    for i in range(1, n + 1, 1):
        tl.forward(100)
        tl.right(180 - 180 / n)

def ex13():
    tl.color("yellow")
    tl.begin_fill()
    for i in range(0, 360, 1):
        tl.forward(2 * ms.pi * 100 / 360)
        tl.left(1)
    tl.end_fill()
    tl.color("blue")
    tl.begin_fill()
    go(40, 130)
    for i in range(0, 360, 1):
        tl.forward(2 * ms.pi * 10 / 360)
        tl.left(1)
    tl.end_fill()
    go(-40, 130)
    tl.begin_fill()
    for i in range(0, 360, 1):
        tl.forward(2 * ms.pi * 10 / 360)
        tl.left(1)

    tl.end_fill()
    tl.color("black")
    go(0, 100)
    tl.right(90)
    tl.width(10)
    tl.forward(40)
    tl.color("red")
    tl.left(45+22.5)
    go(-57, 60)
    for i in range(0, 45, 1):
        tl.forward(2 * ms.pi * 150 / 360)
        tl.left(1)




ex13()