#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:09:52 2021

@author: elizavetalebosina
"""

import tkinter as tk
from tkinter import *
from random import randrange as rnd, choice
import time 


root = Tk() # главное окно - объект класса ТК

root.geometry ('800x900')
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
colors = ['red', 'orange', 'yellow', 'blue']
bombs = (True, False) 

l = Label(root, bg = 'black', fg = 'white', width = 20)

l.pack()


xspeed = rnd(1,5)
xspeed1 = -1*rnd(1,5)
yspeed = rnd(1,5)
yspeed1= -1*rnd(1,5)
    
def new_ball():
    '''
    Функция рисует случайное количество шариков (n) случайного цвета в случаном месте экрана (x,y)
    случайного радиуса r
    balls - массив созданных шариков, которые будут перемещаться
    '''
    canv.delete(ALL)
    global x, y, r, color, balls, n, bombs_coords, rad
    n = rnd(1,5)
    balls = []
    bombs_coords = []
    rad = []
    for i in range (n):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(30, 50)
        rad.append(r)
        bomb = choice(bombs)
        color = choice(colors)
        ball = canv.create_oval(x-r, y-r, x+r, y+r, fill = color, width = 0)
        balls.append(ball)
        if bomb == True:
            bombs_coords.append(ball)
    move_ball()
    canv.after (5000, new_ball)
     
def move_ball():
    '''
    Функция перемещает шарики на xspped - перемещение по оси х, yspeed - перемещение по оси y
    массив balls содержит все шарики, которые создала функция new_ball
    '''
    global xspeed, yspeed, balls, n
    i = 0
    while i < n:
        xspeed = rnd(1,5)
        xspeed1 = -1*rnd(1,5)
        yspeed = rnd(1,5)
        yspeed1= -1*rnd(1,5)
        print(canv.coords(balls[i])[0], canv.coords(balls[i])[1])
        if canv.coords(balls[i])[2] > 740 or canv.coords(balls[i])[0] < 100:
            xspeed = -1 * xspeed 
        if canv.coords(balls[i])[1] < 100 or canv.coords(balls[i])[3] >= 600:
            yspeed = -1 * yspeed 
        canv.move(balls[i], xspeed, yspeed)
        i+=1
    canv.after(100, move_ball)
    

new_ball()   

score = 0

def click(event):
    '''
    Функция осуществляет подсчёт очков 'score'. Очко начислется, если касание мышью экрана находилось внутри шарика
    evet - нажатие левой кнопки мыши
    n - колличество шариков на экране 

    '''
    global score, bombs_coords, n
    for i in range(n):
        if ((event.x - canv.coords(balls[i])[0] - rad[i])**2 + (event.y - canv.coords(balls[i])[1] - rad[i])**2) <= rad[i]**2:
            if balls[i] in bombs_coords:
                score = 0
            else:
                 score+=1    
    l['text'] = str(score)
         

canv.bind('<Button-1>', click)


root.mainloop()

