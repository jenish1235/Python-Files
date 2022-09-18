from turtle import *
import turtle
speed(100)
color('yellow')
bgcolor('black')
b = 200
while b >0 :
    left(b)
    forward(b*3)
    b = b-1

    if b>150 :
        color('yellow')
        
    elif b > 100 :
        color('red')
    
    elif b>50:
        color('green')
    elif b>0: 
        color('white')
    
turtle.done()