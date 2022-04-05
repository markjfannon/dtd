#import relavent packages
import pygame as pg
import os
import time as t
import numpy as np
import sys
import pygame_textinput as pgtxt

#initialises lists used in the program
names = ["joe"]
enemies = []

#username variable for text input 
username=""

#init running state
global running
running = True
pg.init()

#button stuff - image scaling and font settings
button_surface = pg.image.load("button.png")
button_surface = pg.transform.scale(button_surface, (200, 75))
main_font = pg.font.SysFont("sans-serif", 30)
title_font = pg.font.SysFont("sans-serif", 65)
buttonList = ['"menuScreen.startButton"']

#images!
bigLogo = pg.image.load("logo.png")
bigLogo = pg.transform.scale(bigLogo, (600, 600))


#subroutine to check for duplicate names
def nameCheck(name):
    namelist = open("names.txt")
    for item in namelist:
        names.append(item)
    namelist.close()
    for item in names:
        print(item)
        if name == item:
            return True
    return False

#update button method
def updateButtons(button):
    button.update()
    button.changeColour(pg.mouse.get_pos())
    button.checkForInput(pg.mouse.get_pos())

#Rectangle class
class Rectangle():
    #actually creates the box
    def __init__(self, x_pos, y_pos, x_size, y_size, colour, titleFont,
                 mainFont, title, body, screenID):
        exitCross = pg.image.load("cross.png")
        exitCross = pg.transform.scale(exitCross, (50, 50))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_size = x_size
        self.y_size = y_size
        self.colour = colour
        self.titleFont = titleFont
        self.mainFont = mainFont
        self.title = title
        self.body = body
        self.screenID = screenID
        self.cross_x = self.x_pos + self.x_size - 50
        self.cross_y = self.y_pos
        pg.draw.rect(
            self.screenID.screen_item, "Black",
            pg.Rect(self.x_pos - 2, self.y_pos - 2, self.x_size + 4,
                    self.y_size + 4))
        pg.draw.rect(self.screenID.screen_item, self.colour,
                     pg.Rect(self.x_pos, self.y_pos, self.x_size, self.y_size))
        self.screenID.screen_item.blit(
            self.titleFont.render(self.title, True, "Black"), (210, 75))
        self.screenID.screen_item.blit(
            self.mainFont.render(self.body, True, "Black"), (175, 120))
        self.screenID.screen_item.blit(exitCross, (self.cross_x, self.cross_y))

    #checks to see if mouse over exit button lol
    def update(self, position):
        if position[0] in range(self.cross_x,
                                self.cross_x + 50) and position[1] in range(
                                    self.cross_y, self.cross_y + 50):
            print("Click")
            initScreen()

#Class that inherits from rectangle class above, pretty much the same but it features a text box for input
class startWindow(Rectangle):
    def __init__(self, x_pos, y_pos, x_size, y_size, colour, titleFont,
                 mainFont, title, body, screenID):
        super().__init__(x_pos, y_pos, x_size, y_size, colour, titleFont,
                         mainFont, title, body, screenID)
        pg.draw.rect(self.screenID.screen_item, "Black",pg.Rect(100,250,400,75))
        pg.draw.rect(self.screenID.screen_item, "White",pg.Rect(102,252,396,71))
        pg.draw.rect(self.screenID.screen_item, "Black",pg.Rect(205,330,200,50))
        pg.draw.rect(self.screenID.screen_item, "Green",pg.Rect(207,332,196,46))
        self.screenID.screen_item.blit(self.titleFont.render("Continue", True, "Black"), (220, 340))
        self.Activated=False
    def boxUpdate(self, position):
        if position[0] in range(100,500) and position[1] in range(250,325):
            if self.Activated == False:
                self.Activated=True
                print("Activated!")
            else:
                self.Activated=False
                print("Deactivated!")

    def buttonUpdate(self, position):
        if position[0] in range (205,405) and position[1] in range(330,380):
            print("click!")
            return True

    #takes in keyboard input and displays it on box
    def displayText(self,content):
        pg.draw.rect(self.screenID.screen_item, "White",pg.Rect(102,252,396,71))
        self.screenID.screen_item.blit(self.titleFont.render(content, True, "Black"), (110, 275))

    def clearScreen(self):
        pg.draw.rect(self.screenID.screen_item, "White", pg.Rect(102,252,396,71))

#button class
class Button():
    #initialises button
    def __init__(self, image, x_pos, y_pos, text_input, action, title, body,
                 screenID):
        self.screenID = screenID
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.message = action
        self.title = title
        self.body = body
        self.titleFont = pg.font.SysFont("sans-serif", 50)
        self.mainFont = pg.font.SysFont("sans-serif", 25)

    #keeps button updated
    def update(self):
        self.screenID.screen_item.blit(self.text, self.text_rect)

    def init_image(self):
        self.screenID.screen_item.blit(self.image, self.rect)

    #checks for clicks
    def checkForInput(self, position):
        if position[0] in range(self.rect.left,
                                self.rect.right) and position[1] in range(
                                    self.rect.top, self.rect.bottom):
            print(self.message)
            if self.text_input == "Start!":
                self.startRect = startWindow(50, 50, 500, 400, "Grey",
                                         self.titleFont, self.mainFont,
                                         self.title, self.body, self.screenID)
                pg.display.flip()
            else:
                #made rectangle before class was made - old
                #pg.draw.rect(screenID.screen_item, "Black", pg.Rect(48, 48, 504, 404))
                #pg.draw.rect(screenID.screen_item, "Grey", pg.Rect(50, 50, 500, 400))
                self.rect1 = Rectangle(50, 50, 500, 400, "Grey",
                                       self.titleFont, self.mainFont,
                                       self.title, self.body, self.screenID)
                #making text outside of class - old way
                #screenID.screen_item.blit(self.titleFont.render(self.title, True, "Black"), (210, 75))
                #screenID.screen_item.blit(self.mainFont.render(self.body, True, "Black"), (175, 120))
                pg.display.flip()

    #checks for being hovered over. If so, changes colour
    def changeColour(self, position):
        if position[0] in range(self.rect.left,
                                self.rect.right) and position[1] in range(
                                    self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")


#inheritable dimenions for each window-based class
class main:
    def __init__(self, windowX, windowY):
        background_colour = (234, 212, 252)
        self.initscreen = pg.display.set_mode((windowX, windowY))
        pg.display.set_caption("Discipline Tower Defence")
        self.initscreen.fill(background_colour)
        pg.display.flip()


#starting screen class
class startScreen(main):
    def __init__(self, windowX, windowY, imgX, imgY, textSize):
        super().__init__(windowX, windowY)
        self.screen_item = self.initscreen
        self.startButton = Button(button_surface, 300, 500, "Start!",
                                  "Start button pressed", "Game Start",
                                  "Enter your preferred username here!", self)
        self.infoButton = Button(button_surface, 100, 500, "Info",
                                 "Info button pressed", "Game Info",
                                 "Mark made this game in 2022", self)
        self.rulesButton = Button(button_surface, 500, 500, "Rules",
                                  "Rules button pressed", "Game Rules",
                                  "This is how you play the game", self)
        self.screen_item.blit(bigLogo, (300, 300))
        self.title = title_font.render("Discipline Tower Defence", True,
                                       "Black")


#actually calls startScreen class (about time lol)
startScreen = startScreen(600, 600, 3, 3, 3)
startScreen.screen_item.blit(bigLogo, (300, 300))


#resets screen to starting state
def initScreen():
    startScreen.screen_item.fill("white")
    startScreen.screen_item.blit(bigLogo, (0, 0))
    startScreen.screen_item.blit(startScreen.title, (34, 275))

    startScreen.startButton.init_image()
    startScreen.infoButton.init_image()
    startScreen.rulesButton.init_image()


initScreen()

#game loop, checks for updates and events
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            startScreen.startButton.checkForInput(pg.mouse.get_pos())
            startScreen.infoButton.checkForInput(pg.mouse.get_pos())
            startScreen.rulesButton.checkForInput(pg.mouse.get_pos())
            startScreen.startButton.startRect.update(pg.mouse.get_pos())
            startScreen.startButton.startRect.boxUpdate(pg.mouse.get_pos())
            clicked=startScreen.startButton.startRect.buttonUpdate(pg.mouse.get_pos())
            if clicked == True:
                print(username)
                picked=nameCheck(username)
                if picked == True:
                    print("THIS HAS ALREADY BEEN PICKED HAHA LOSER")
                else:
                    print("Name Valid")
                    nameWrite=open("chosenname.txt","w")
                    nameWrite.write(username)
                    nameWrite.close()
                    os.system('python3 game.py')
                    exit()
        if event.type == pg.KEYDOWN and startScreen.startButton.startRect.Activated == True:
            if event.key == pg.K_RETURN:
                print("ENTER")
                print(username)
                picked=nameCheck(username)
                print(picked)
                if picked == True:
                    print("THIS HAS ALREADY BEEN PICKED HAHA LOSER")
                else:
                    print("Name Valid")
                    nameWrite=open("chosenname.txt","w")
                    nameWrite.write(username)
                    nameWrite.close()
                    os.system('python3 game.py')
                    exit()
            if event.key == pg.K_BACKSPACE:
                username=username[:-1]
                startScreen.startButton.startRect.displayText(username)
            else:
                username += event.unicode
                startScreen.startButton.startRect.displayText(username)

# for button in buttonList:
    startScreen.startButton.update()
    startScreen.startButton.changeColour(pg.mouse.get_pos())
    startScreen.infoButton.update()
    startScreen.infoButton.changeColour(pg.mouse.get_pos())
    startScreen.rulesButton.update()
    startScreen.rulesButton.changeColour(pg.mouse.get_pos())
    #updateButtons(button)
    pg.display.update()
