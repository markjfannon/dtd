#import relavent packages
import pygame as pg
import os
import time as t
import numpy as np
import sys

#initialises lists used in the program
names=[]
enemies=[]

#init running state
global running
running = True
pg.init()

#button stuff - image scaling and font settings
button_surface=pg.image.load("button.png")
button_surface=pg.transform.scale(button_surface, (200, 75))
main_font=pg.font.SysFont("sans-serif", 30)
buttonList=[str.menuScreen.startButton]

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

#button clas
class Button():
    #initialises button
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    #keeps button updated
    def update(self):
        screen.screen_item.blit(self.image, self.rect)
        screen.screen_item.blit(self.text, self.text_rect)

    #checks for clicks
    def checkForInput(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            print("Click")
    
    #checks for being hovered over. If so, changes colour
    def changeColour(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")


#inheritable dimenions for each window-based class
class main:
    def __init__(self,windowX,windowY):
        background_colour = (234,212,252)
        self.initscreen=pg.display.set_mode((windowX,windowY))
        pg.display.set_caption("Discipline Tower Defence")
        self.initscreen.fill(background_colour)
        pg.display.flip()

#starting screen class
class startScreen(main):
    def __init__(self,windowX,windowY,imgX,imgY,textSize):
        super().__init__(windowX,windowY)
        self.screen_item = self.initscreen
        self.startButton=Button(button_surface, 200, 100, "Start!")

menuScreen=startScreen(600,600,3,3,3)


#screen = pg.display.set_mode((800,800))
#pg.display.set_caption("Test")
#button = Button(button_surface, 200, 100, "Click Me!")


#game loop, checks for updates and events
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            for button in buttonList:
                button.checkForInput(pg.mouse.get_pos())


    menuScreen.screen_item.fill("white")

    for button in buttonList:
        button.update()
        button.startButton.changeColour(pg.mouse.get_pos())

    pg.display.update()
