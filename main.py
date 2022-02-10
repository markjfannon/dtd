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
title_font=pg.font.SysFont("sans-serif", 65)
buttonList=['"menuScreen.startButton"']

#images!
bigLogo=pg.image.load("logo.png")
bigLogo=pg.transform.scale(bigLogo, (600, 600))

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

def updateButtons(button):
    button.update()
    button.changeColour(pg.mouse.get_pos())
    button.checkForInput(pg.mouse.get_pos())


#button class
class Button():
    #initialises button
    def __init__(self, image, x_pos, y_pos, text_input, action):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.message = action
    #keeps button updated
    def update(self):
        startScreen.screen_item.blit(self.image, self.rect)
        startScreen.screen_item.blit(self.text, self.text_rect)

    #checks for clicks
    def checkForInput(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            print(self.message)
    
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
        self.startButton=Button(button_surface, 300, 500, "Start!", "Start button pressed")
        self.infoButton=Button(button_surface, 100, 500, "Info", "Info button pressed")
        self.rulesButton=Button(button_surface, 500, 500, "Rules", "Rules button pressed")
        self.screen_item.blit(bigLogo, (300, 300))
        self.title=title_font.render("Discipline Tower Defence",True,"Black")


#actually calls startScreen class (about time lol)
startScreen=startScreen(600,600,3,3,3)
startScreen.screen_item.blit(bigLogo, (300,300))


#game loop, checks for updates and events
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            for button in buttonList:
               startScreen.startButton.checkForInput(pg.mouse.get_pos())
               startScreen.infoButton.checkForInput(pg.mouse.get_pos())
               startScreen.rulesButton.checkForInput(pg.mouse.get_pos())
               #updateButtons(button)

    startScreen.screen_item.fill("white")

    startScreen.screen_item.blit(bigLogo, (0,0))
    startScreen.screen_item.blit(startScreen.title,(34,275))

   # for button in buttonList:
    startScreen.startButton.update()
    startScreen.startButton.changeColour(pg.mouse.get_pos())
    startScreen.infoButton.update()
    startScreen.infoButton.changeColour(pg.mouse.get_pos())
    startScreen.rulesButton.update()
    startScreen.rulesButton.changeColour(pg.mouse.get_pos())
    #updateButtons(button)
    pg.display.update()
