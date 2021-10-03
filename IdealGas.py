from random import random
from random import randint
import turtle as tl
import numpy as np

num = 20
tl.penup()
tl.goto(-300, -300)
tl.pendown()
tl.goto(-300, 300)
tl.goto(300, 300)
tl.goto(300, -300)
tl.goto(-300, -300)

pool = [tl.Turtle(shape='circle') for i in range(num)]
for unit in pool:
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-290, 290), randint(-290, 290))

Vx = np.zeros(num)
Vy = np.zeros(num)

for k in range(num):
    Vx[k] = ((random() - 0.5) / 0.5) * 5
    Vy[k] = ((random() - 0.5) / 0.5) * 5

for i in range(1000):
    for k in range(len(pool)):
        x = pool[k].pos()[0]
        y = pool[k].pos()[1]
        if x <= -300 or x >= 300: Vx[k] = -Vx[k]
        if y <= -300 or y >= 300: Vy[k] = -Vy[k]
        pool[k].goto(x + Vx[k], y + Vy[k])