import turtle as tl
import math as ms
from random import *

tl.shape('turtle')

'''
 def numbers(s:list):
     def a():
         tl.penup()
         tl.left(90)
         tl.forward(40)
         tl.right(90)
         tl.pendown()
         tl.forward(20)
         tl.penup()
         tl.right(90)
         tl.forward(20)
         tl.right(45)
         tl.forward(20*ms.sqrt(2))
         tl.left(135)
     def b():
         tl.penup()
         tl.left(90)
         tl.forward(20)
         tl.right(45)
         tl.forward(20*ms.sqrt(2))
         tl.right(135)
         tl.pendown()
         tl.forward(20)
         tl.penup()
         tl.forward(20)
         tl.right(90)
         tl.forward(20)
         tl.right(180)
     def c():
         tl.penup()
         tl.left(45)
         tl.forward(20*ms.sqrt(2))
         tl.right(135)
         tl.pendown()
         tl.forward(20)
         tl.penup()
         tl.right(90)
         tl.forward(20)
         tl.right(180)
     def d():
         tl.pendown()
         tl.forward(20)
         tl.penup()
         tl.right(180)
         tl.forward(20)
         tl.right(180)
     def e():
         tl.penup()
         tl.left(90)
         tl.pendown()
         tl.forward(20)
         tl.penup()
         tl.right(180)
         tl.forward(20)
         tl.left(90)
     def f():
         tl.penup()
         tl.left(90)
         tl.forward(20)
         tl.pendown()
         tl.forward(20)
         tl.penup()
         tl.right(180)
         tl.forward(40)
         tl.left(90)
     def g():
         tl.penup()
         tl.left(45)
         tl.pendown()
         tl.forward(20*ms.sqrt(2))
         tl.penup()
         tl.right(180)
         tl.forward(20*ms.sqrt(2))
         tl.left(135)
     def h():
         tl.penup()
         tl.left(90)
         tl.forward(20)
         tl.right(90)
         tl.pendown()
         tl.forward(20)
         tl.penup()
         tl.right(90)
         tl.forward(20)
         tl.right(90)
         tl.forward(20)
         tl.right(180)
     def i():
         tl.penup()
         tl.left(90)
         tl.forward(20)
         tl.right(45)
         tl.pendown()
         tl.forward(20*ms.sqrt(2))
         tl.penup()
         tl.right(135)
         tl.forward(40)
         tl.right(90)
         tl.forward(20)
         tl.right(180)

     def x():
         tl.penup()
        tl.forward(30)

     def one():
         i()
         b()
         c()
         x()
     def two():
         a()
         b()
         g()
         d()
         x()
     def three():
         a()
         i()
         h()
         g()
         x()
     def four():
         f()
         h()
         b()
         c()
         x()
     def five():
         a()
         f()
         h()
         c()
         d()
         x()
     def six():
         i()
         e()
         d()
         c()
         h()
         x()
     def null():
         e()
         f()
         a()
         b()
         c()
         d()
         x()
     def seven():
         a()
         i()
         e()
         x()
     def eight():
         a()
         f()
         e()
         d()
         c()
         b()
         h()
         x()
     def nine():
         g()
         b()
         a()
         f()
         h()
         x()

     for n in range(len(s)):
         if s[n] == 1:
             one()
         elif s[n] == 2:
             two()
         elif s[n] == 3:
             three()
         elif s[n] == 4:
             four()
         elif s[n] == 5:
             five()
         elif s[n] == 6:
             six()
         elif s[n] == 7:
             seven()
         elif s[n] == 8:
             eight()
         elif s[n] == 9:
             nine()
         elif s[n] == 0:
             null()
'''

text = open('141700.txt', 'r')
#    s = input.readlines()
#    for n in range(len(s)):
#        s[n] = s[n].rstrip()

#    for k in range(len(s)):
#        exec(s[k])
exec(text.read())
inp = input()

a = len(inp)
num = [0] * a
inp = int(inp)

for h in range(a):
    num[-h-1] = inp % 10
    inp = inp // 10


numbers(num)
text.close()
