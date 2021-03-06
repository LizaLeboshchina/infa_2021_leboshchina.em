#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:51:22 2021

@author: elizavetalebosina
"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 900))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (248, 203, 172)
BROWN = (188, 116, 66)
GRAY = (153, 153, 153)
DARKGRAY = (51, 51, 51)
SAGEGREEN = (220, 253, 232)
BLUE = (150, 201, 218)
BG1 = (123, 103, 30)
BG2 = (82, 69, 17)
GREEN = (141, 170, 52)
PURPLE = (255, 0, 255)
pi = 3.14



#Поверхность для кота 
cat_surface = pygame.Surface((800, 900))
cat_surface.fill(PURPLE)
cat_surface.set_colorkey(PURPLE) 

#Поверзность для клубка 

clew_surface = pygame.Surface((800, 900))
clew_surface.fill(PINK)
clew_surface.set_colorkey(PINK)

#фон
rect(screen, BG2, (0, 0, 800, 400))
rect(screen, BG1, (0, 400, 800, 500))


def window (x, y, scale = 1):
    rect(screen, SAGEGREEN, (x, y, 250*scale, 325*scale))
    rect(screen, BLUE, (x + 25*scale, y + 25*scale, 90*scale, 75*scale))
    rect(screen, BLUE, (x + 135*scale, y + 25*scale, 90*scale, 75*scale))
    rect(screen, BLUE, (x + 25*scale, y + 125*scale, 90*scale, 175*scale))
    rect(screen, BLUE, (x + 135*scale, y + 125*scale, 90*scale, 175*scale))

def cat (center_x, center_y, scale = 1, main_colour = BROWN, eyes_colour = GREEN, flip = False):
    
    ##Рисование кота 
    
    
    #Хвост кота 
    surf_tail= pygame.Surface((160, 65))
    surf_tail.fill(PINK)
    surf_tail.set_colorkey(PINK)
    ellipse(surf_tail, main_colour, (0, 0, 160, 65))
    ellipse(surf_tail, BLACK, (0, 0, 160, 65), 1)
    tail_rect = surf_tail.get_rect(
        center=(80, 32.5))


    rot_surf_tail = pygame.transform.rotate(surf_tail, 45)
    rot_tail_rect = rot_surf_tail.get_rect(center = (715, 555))

    cat_surface.blit(rot_surf_tail, rot_tail_rect)


    #Кот крпные детали

    ellipse(cat_surface, main_colour, (350, 500, 350, 150))#тело
    ellipse(cat_surface, BLACK, (350, 500, 350, 150), 1)#обводка тела

    ellipse(cat_surface, main_colour, (300, 525, 40, 65))#самая маленькая лапка
    ellipse(cat_surface, BLACK, (300, 525, 40, 65), 1)#самая маленькая лапка

    poligon1_points = [(250,425),(310,440),(280,485)]#точки левого уха
    polygon(cat_surface, main_colour, poligon1_points)#левое ухо
    polygon(cat_surface, BLACK, poligon1_points, 1)

    poligonm1_points = [(265,440),(300,445),(285,470)]#точки левого уха маленького
    polygon(cat_surface, PINK, poligonm1_points)#левое маленькое ухо

    poligon2_points = [(450,425),(390,440),(420,485)]#точки правого уха
    polygon(cat_surface, main_colour, poligon2_points)#правое ухо
    polygon(cat_surface, BLACK, poligon2_points, 1)

    poligonm2_points = [(432,440),(400,445),(415,470)]#точки маленького правого уха
    polygon(cat_surface, PINK, poligonm2_points)#правое маленькое ухо

    circle(cat_surface, main_colour, (350, 500), 75)#голова 
    circle(cat_surface, BLACK, (350, 500), 75, 1)#обводка головы

    circle(cat_surface, main_colour, (700, 625), 50)#бедро
    circle(cat_surface, BLACK, (700, 625), 50, 1)#обводка бедра

    ellipse(cat_surface, main_colour, (300, 600, 100, 50))#передняя лапка
    ellipse(cat_surface, BLACK, (300, 600, 100, 50), 1)#обводка

    ellipse(cat_surface, main_colour, (725, 640, 30, 75))#маленькая задняя лапка
    ellipse(cat_surface, BLACK, (725, 640, 30, 75), 1)#обводка

    #Глаза


    circle(cat_surface, eyes_colour, (315, 500), 20)#левый глаз
    circle(cat_surface, eyes_colour, (385, 500), 20)#правый глаз
    ellipse(cat_surface, BLACK, (305, 480, 20, 40))#левый эллепс
    ellipse(cat_surface, BLACK, (375, 480, 20, 40))


    #Повёрнутые элепсы 

    #левый глаз
    surf_eye_1= pygame.Surface((7, 25))
    surf_eye_1.fill(BLACK)
    surf_eye_1.set_colorkey(BLACK)
    ellipse(surf_eye_1, WHITE, (0, 0, 7, 25))
    eye_1_rect = surf_eye_1.get_rect(
        center=(3.5, 12.5))


    rot_surf_eye_1 = pygame.transform.rotate(surf_eye_1, 45)
    rot_eye_1_rect = rot_surf_eye_1.get_rect(center = (310, 490))


    # правый глаз 
    surf_eye_2= pygame.Surface((7, 25))
    surf_eye_2.fill(BLACK)
    surf_eye_2.set_colorkey(BLACK)
    ellipse(surf_eye_2, WHITE, (0, 0, 7, 25))
    eye_2_rect = surf_eye_2.get_rect(
        center=(3.5, 12.5))


    rot_surf_eye_2 = pygame.transform.rotate(
        surf_eye_2, 45)
    rot_eye_2_rect = rot_surf_eye_2.get_rect(center = (380, 490))



    cat_surface.blit(rot_surf_eye_1, rot_eye_1_rect)
    cat_surface.blit(rot_surf_eye_2, rot_eye_2_rect)



    #Нос и рот

    poligon_nose_points = [(335,520),(365,520),(350,535)]

    polygon(cat_surface, PINK, poligon_nose_points)
    polygon(cat_surface, BLACK, poligon_nose_points, 1)#нос
    aaline(cat_surface, BLACK, 
                   [350, 535], 
                   [350, 550], 3)  
    arc(cat_surface, BLACK, (350, 550, 15, 5), 3.14, 0, 5)  
    arc(cat_surface, BLACK, (335, 550, 15, 5), 3.14, 0, 5) 

    #УСЫ
    surf_1= pygame.Surface((35, 15))
    surf_1.fill(PINK)
    surf_1.set_colorkey(PINK)
    arc(surf_1, BLACK, (0, 0, 35, 15), 0, pi)
    surf_1_rect = surf_eye_1.get_rect(
        center=(358, 550))


    surf_2 = pygame.transform.rotate(
        surf_1, 345)
    surf_2_rect = surf_2.get_rect(center = (370, 555))

    surf_3 = pygame.transform.rotate(
        surf_1, 353)
    surf_3_rect = surf_3.get_rect(center = (370, 550.5))

    surf_4_rect = surf_eye_1.get_rect(center = (313, 550))

    surf_5 = pygame.transform.rotate(
        surf_1, 7)
    surf_5_rect = surf_5.get_rect(center = (327, 550.5))

    surf_6 = pygame.transform.rotate(
        surf_1, 15)
    surf_6_rect = surf_6.get_rect(center = (330, 555))


    cat_surface.blit(surf_1, surf_1_rect)
    cat_surface.blit(surf_2, surf_2_rect)
    cat_surface.blit(surf_3, surf_3_rect)
    cat_surface.blit(surf_1, surf_4_rect)
    cat_surface.blit(surf_5, surf_5_rect)
    cat_surface.blit(surf_6, surf_6_rect)
    
    
    
    #Изменение размера и поворот 
    new_cat_surface = pygame.transform.scale(
    cat_surface, (cat_surface.get_width() // scale,
               cat_surface.get_height() // scale))
    new_cat_surface_rect = new_cat_surface.get_rect(center = 
                                                    (center_x, center_y))
    if flip == True:
        new_cat_surface = pygame.transform.flip(new_cat_surface, True, False)
        
    screen.blit(new_cat_surface, new_cat_surface_rect)


def clew(center_x, center_y, scale, flip = False):
    
    #Клубок 
    circle(clew_surface, GRAY, (175, 700), 50)
    circle(clew_surface, BLACK, (175, 700), 50, 1)
    #GПолосочки на клубке 
    arc(clew_surface, BLACK, (70,720, 75, 30), pi, 2*pi)
    arc(clew_surface, BLACK, (10,720, 60, 30), 0, pi)
    arc(clew_surface, BLACK, (150,690, 40, 40), pi, 3*pi/2, 1)
    arc(clew_surface, BLACK, (145,670, 60, 60), 0, pi/2, 1)
    arc(clew_surface, BLACK, (140,680, 60, 60), pi, 5*pi/3, 1)
    
    new_clew_surface = pygame.transform.scale(clew_surface, (round(clew_surface.get_width() * scale),
               round(clew_surface.get_height() * scale)))
    new_clew_surface_rect = new_clew_surface.get_rect(center = 
                                                    (center_x, center_y))
    if flip == True:
        new_clew_surface = pygame.transform.flip(new_clew_surface, True, False)
        
    screen.blit(new_clew_surface, new_clew_surface_rect)
    
   


window(600,50, 0.8)
window (300, 50, 0.8)
window(10, 50, 0.8)
cat (550, 450, 2)
cat (400, 700, 4)
cat (620, 730, 4, DARKGRAY, BLUE)
cat (300, 520, 2, DARKGRAY, BLUE, True)
cat (100, 700, 4, DARKGRAY, BLUE, True)
cat (100, 420, 4, BROWN, GREEN, True)
cat (700, 620, 4, BROWN, GREEN, True)
clew(580, 400, 1.4)
clew(150, 550, 0.4)
clew(340, 320, 0.5)
clew(200, 380, 1, True)
clew(550, 500, 0.4, True)
clew(510, 530, 0.7, True)



pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
