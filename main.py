#import relavent packages
import pygame as pg
import os
import time as t
import numpy as np
import pygame_widgets as pw
from pygame_widgets.button import Button

#initialises lists used in the program
names=[]
enemies=[]

#init running state
global running
running = True
pg.init()

#subroutine to check for duplicate names
def nameCheck(name):
    namelist=open("names.txt")
    for item in namelist:
        names.append(item)
    namelist.close()
    for item in names:
        if name==item:
            return false
    return true


#inheritable dimenions for each window-based class
class main:
    def __init__(self,windowX,windowY):
        background_colour = (234,212,252)
        initscreen=pg.display.set_mode((windowX,windowY))
        pg.display.set_caption("Discipline Tower Defence")
        initscreen.fill(background_colour)
        pg.display.flip()

        running=True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running=False

#sarting screen class
class startScreen(main):
    def __init__(self,windowX,windowY,imgX,imgY,textSize):
        super().__init__(windowX,windowY)

screen1=startScreen(600,600,3,3,3)

