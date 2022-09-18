from email.utils import collapse_rfc2231_value
from tkinter.filedialog import SaveAs
import turtle
from turtle import *

bgcolor("black")
turtle.speed(100000000)

for i in range(15):

    if(i<1):
        pencolor("yellow")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
    
    elif(i<2):
        
        pencolor("cyan")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
    
    elif(i<3):
        
        pencolor("red")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
    
    elif(i<4):
        
        pencolor("cyan")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
    
    elif(i<5):
       
        pencolor("green")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
        
    elif(i<6):
        
        pencolor("cyan")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
    
    elif(i<7):
       
        pencolor("blue")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
    
    elif(i<8):
        pencolor("cyan")
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(45)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(180)
        fd(200)
        rt(90)
    
    elif(i<9):
        pu()
        fd(200)
        pd()
        lt(112)
        fd(155)
        lt(46)
        fd(155)
        
    elif(i<10):
       lt(46)
       fd(155)
    
    elif(i<11):
       lt(43)
       fd(155)
    elif(i<12):
       lt(47)
       fd(155)
    elif(i<13):
       lt(45)
       fd(155)
    elif(i<14):
       lt(45)
       fd(155)
    elif(i<15):
       lt(45)
       fd(153)
       ht()
    

turtle.done()
SaveAs("turtle.png", )