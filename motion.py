import turtle as tl
import math as ms
import numpy as np

def parabola():
    x = 0
    y = 0.1
    Vx = 10
    Vy = 20
    ay = -0.5
#    tl.goto(500, 0)
#    tl.goto(-500, 0)
    for t in np.arange(0, 500, 1):
        x += Vx / 5
        y += Vy / 5
        if y <= -5: Vy = -0.8 * Vy
        else: Vy += ay
        tl.goto(x, y)
        print(x, y)

tl.shape('turtle')
parabola()
