#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:32:54 2021

@author: elizavetalebosina
"""
import pygame
from pygame.draw import *

def main():
    
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((500, 650))

    background()

    surf1 = pygame.Surface((225, 206))
    surf2 = pygame.Surface((225, 206))
    surf3 = pygame.Surface((225, 206))
    surfHouse1 = pygame.Surface((565, 700))

    ghost(surf1, 0.6, 1)
    surf1.set_colorkey('green')
    surf1.set_alpha(255)
    ghost(surf2, 0.3, 1)
    surf2.set_colorkey('green')
    surf2.set_alpha(200)
    ghost(surf3, 0.3, -1)
    surf3.set_colorkey('green')
    surf3.set_alpha(200)
    screen.blit(surf1, (350, 480), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf2, (320, 500), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf2, (400, 400), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf2, (420, 430), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf3, (50, 530), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf3, (70, 560), special_flags=pygame.BLEND_ALPHA_SDL2)

    house(surfHouse1, 0.3)
    surfHouse1.set_colorkey('green')
    surfHouse1.set_alpha(200)
    screen.blit(surfHouse1, (160, 226), special_flags=pygame.BLEND_ALPHA_SDL2)
    surfHouse1.set_alpha(150)
    screen.blit(surfHouse1, (350, 132), special_flags=pygame.BLEND_ALPHA_SDL2)
    surfHouse1.set_alpha(500)
    screen.blit(surfHouse1, (0, 294), special_flags=pygame.BLEND_ALPHA_SDL2)

    ellipse(screen, (77, 77, 77), (300, 105, 400, 40))


    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

def transform(t, a, b):
    """
    Функция преобразует координаты 
    t - координаты изначальной фигуры 
    a - увеличение координаты 
    b - сдвиг 
    """
    # для каждого элемента x из t вычислить ax+b и возвратить, как tuple
    return tuple(x * a + b for x in t)

def p(x, y, ax, bx, ay, by):
    """
    Функция преобразует координаты 
    """
    return (x * ax + bx, y * ay + by)

def background():
    """
    Функция рисует фон изображения 
    """
    rect(screen, (102, 102, 102), (0, 0, 500, 300))
    circle(screen, (255, 255, 255), (415, 73), 45)
    ellipse(screen, (51, 51, 51), (10, 75, 380, 40))
    ellipse(screen, (77, 77, 77), (200, 55, 300, 45))
    ellipse(screen, (77, 77, 77), (80, 280, 450, 40))
    ellipse(screen, (26, 26, 26), (250, 165, 300, 50))
    ellipse(screen, (26, 26, 26), (210, 333, 400, 50))
    ellipse(screen, (42, 42, 42), (-150, 373, 400, 45))

def house(dest, scale = 1, main_color = (40, 34, 10), tubes_color = (26, 26, 26), cloud_color = (51, 51, 51), upper_windows_colour = (72, 62, 55), balkony_color = (26, 26, 26), bottom_windows_color1 = (43, 17, 0), bottom_windows_color2 = (212, 170, 0),  cloud = False):
    """Функция рисует дом
    dest (destination) - поверхность, на которой будет отрисован дом 
    main_color - цвет фасада дома
    tubes_color - цвет труб 
    cloud_color - цвет облака дыма
    upper_windows_colour - цвет верхних окон
    balkony_color - цвет балкона 
    bottom_windows_color1 - цвет левых окон нижнего этажа
    bottom_windows_color2  - цвет правых окон нижнего этажа
    scale - масштаб 
    cloud - наличие облака дыма cloud = True - нужно, cloud = False - нет
    """
    rect(dest, 'green', (0, 0, 600, 700))
    color = (40, 34, 10)
    rect(dest, color, (33 * scale, 144 * scale, 417 * scale, 566 * scale))

    t = (0, 145, 60, 100, 420, 100, 490, 145, 0, 145)
    x = transform(t[::2], scale, 0)
    y = transform(t[1::2], scale, 0)
    polygon(dest, 'black', tuple(zip(x, y)))

    #отрисовка труб + облако дыма(если надо)
    def tubes(dest, tubes_color, scale, cloud):
        '''
        Функция рисует трубы и облако дыма, если надо
        tubes_color - цвет трубы
        scale - масштаб
        cloud - наличие облака дыма cloud = True - нужно, cloud = False - нет
        '''
        
        rect(dest, tubes_color, (93 * scale, 60 * scale, 17 * scale, 62 * scale))
        rect(dest, tubes_color, (282 * scale, 71 * scale, 13 * scale, 30 * scale))
        
        if cloud == True:
            ellipse(dest, cloud_color, (31 * scale, 2 * scale, 600 * scale, 74 * scale))
    
        
        rect(dest, tubes_color, (117 * scale, 0 * scale, 30 * scale, 130 * scale))
        rect(dest, tubes_color, (385 * scale, 42 * scale, 15 * scale, 86 * scale))

    #отрисовка окон верхнего этажа
    def upper_windows(dest, upper_windows_colour, scale):
        """
        функция рисует привидение
        dest (destination) - поверхность, на которой будут отрисованы верхние окна
        upper_windows_colour - цвет окон первого этажа
        scale - масштаб изображения, относительно исходного
        """
        rect(dest, upper_windows_colour, (63 * scale, 146 * scale, 46 * scale, 214 * scale))
        rect(dest, upper_windows_colour, (145 * scale, 146 * scale, 46 * scale, 214 * scale))
        rect(dest, upper_windows_colour, (247 * scale, 146 * scale, 46 * scale, 214 * scale))
        rect(dest, upper_windows_colour, (355 * scale, 146 * scale, 46 * scale, 214 * scale))

    
    def balkony(dest, balkony_color, scale):
        """
        функция рисует балкон
        dest (destination) - поверхность, на которой будет отрисован балкон
        balkony_color - цвет балкона 
        scale - масштаб изображения, относительно исходного
        """
        rect(dest, balkony_color, (17 * scale, 290 * scale, 455 * scale, 26 * scale))
        rect(dest, balkony_color, (3 * scale, 316 * scale, 14 * scale, 51 * scale))
        rect(dest, balkony_color, (472 * scale, 316 * scale, 14 * scale, 51 * scale))
        rect(dest, balkony_color, (57 * scale, 316 * scale, 26 * scale, 51 * scale))
        rect(dest, balkony_color, (134 * scale, 316 * scale, 26 * scale, 51 * scale))
        rect(dest, balkony_color, (211 * scale, 316 * scale, 26 * scale, 51 * scale))
        rect(dest, balkony_color, (301 * scale, 316 * scale, 26 * scale, 51 * scale))
        rect(dest, balkony_color, (389 * scale, 316 * scale, 26 * scale, 51 * scale))
        rect(dest, balkony_color, (0 * scale, 366 * scale, 498 * scale, 58 * scale))

    def bottom_windows(dest, scale, bottom_windows_color1, bottom_windows_color2):
        """
        функция рисует привидение
        dest (destination) - поверхность, на которой будет отрисовано привидение
        bottom_windows_color1 - цвет левых окон нижнего этажа
        bottom_windows_color2  - цвет правых окон нижнего этажа       
        scale - масштаб изображения, относительно исходного
        flip - отражение изображения (flip = 1 изображение стандартное, flip = -1 изображение отраженное)
        """
        
        rect(dest, bottom_windows_color1, (80 * scale, 550 * scale, 80 * scale, 100 * scale))
        rect(dest, bottom_windows_color1, (206 * scale, 550 * scale, 80 * scale, 100 * scale))
        rect(dest, bottom_windows_color2, (325 * scale, 550 * scale, 80 * scale, 100 * scale))


def ghost(dest, body_color =  (179, 179, 179), eyes_color = (135, 205, 222), eyes_center_color = 'black', blick_color =  (255, 255, 255), scale = 1, flip = 1):
    """
    функция рисует привидение
    dest (destination) - поверхность, на которой будет отрисовано привидение
    body_color - цвет тела приведения 
    eyes_color - цвет глаз приведения
    eyes_center_color - цвет зрачка приведения 
    blick_color - цвет блика на глазах приведения 
    scale - масштаб изображения, относительно исходного
    flip - отражение изображения (flip = 1 изображение стандартное, flip = -1 изображение отраженное)

    """
    rect(dest, 'green', (0, 0, 225, 206))

    def body(dest, scale , body_color):
        """
        Функция рисует тело приведения 
        dest - поверхность, на которой будет отрисовано тело приведения
        body_color - цвет тела приведения 
        scale - масштаб изображения, относительно исходного
        flip - отражение изображения (flip = 1 изображение стандартное, flip = -1 изображение отраженное)
        """
        t = (55, 46, 121, 21, 135, 24, 167, 51, 169, 52, 198, 80, 214, 90, 221, 97, 224, 111, 225, 127, 220, 134,
         212, 136, 199, 139, 192, 143, 187, 155, 185, 164, 176, 179, 151, 180, 138, 176, 123, 183, 108, 198,
         98, 204, 89, 207, 81, 205, 65, 184, 57, 179, 37, 168, 29, 169, 2, 173, 0, 173, 0, 170, 10, 155,
         16, 136, 32, 112, 39, 99, 41, 94, 49, 78, 55, 46)
    
    
        ax = scale * flip
        bx = 225 * scale if flip < 0 else 0
        ay = scale
        by = 0
        x = transform(t[::2], ax, bx)
        y = transform(t[1::2], ay, by)
        polygon(dest, body_color, tuple(zip(x, y)))
        circle(dest, body_color, p(92, 38, ax, bx, ay, by), 38 * scale)

    def eyes(dest, eyes_color, eyes_center_color, scale, flip):
        """
        Функция рисует галаз  приведения 
        dest - поверхность, на которой будет отрисовано тело приведения
        eyes_color - цвет глаз приведения
        eyes_center_color - цвет зрачка приведения 
        blick_color - цвет блика на глазах приведения        
        scale - масштаб изображения, относительно исходного
        flip - отражение изображения (flip = 1 изображение стандартное, flip = -1 изображение отраженное)
        """        
        
        circle(dest, eyes_color, p(70, 31, ax, bx, ay, by), 10 * scale)
        circle(dest, eyes_color, p(102, 27, ax, bx, ay, by), 10 * scale)
        
        circle(dest, eyes_center_color, p(67, 32, ax, bx, ay, by), 4 * scale)
        circle(dest, eyes_center_color, p(99, 27, ax, bx, ay, by), 3.4 * scale)
    
        t = (69, 31, 69, 29, 75, 25, 77, 25, 77, 28, 71, 31, 69, 31)
        x = transform(t[::2], ax, bx)
        y = transform(t[1::2], ay, by)
        polygon(dest, blick_color, tuple(zip(x, y)))
        t = (100, 26, 100, 24, 106, 20, 108, 20, 108, 22, 102, 26, 100, 26)
        x = transform(t[::2], ax, bx)
        y = transform(t[1::2], ay, by)
        polygon(dest, blick_color, tuple(zip(x, y)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()