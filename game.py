import pygame as pg
import random as r

screen = pg.display.set_mode((1000,500))

class Rectangle():
    def __init__(self, x, y, l, h, screen):
        self.x = x
        self.y = y
        self.l = l
        self.h = h
        pg.draw.rect(screen, "Blue", pg.Rect(self.x, self.y, self.l, self.h))

    
class main:
    def __init__(self, windowX, windowY):
        self.screen = pg.display.set_mode((windowX, windowY))
        pg.display.set_caption("Discipline Tower Defence")
        self.screen.fill("Black")
        rect1=Rectangle(200,300,50,100,self.screen)
        pg.display.flip()


class enemySprite(pg.sprite.Sprite):
    def __init__(self, x, y, v, screen):
        super().__init__()
        self.image = pg.transform.scale((pg.image.load("creature1.png")),(50,50))
        #pg.draw.rect(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = v
        #screen.blit(self.image, (x,y))
    def moveDown(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 450:
            print("No longer possible")
            self.kill()
    def moveRandomDown(self):
        self.rect.y = self.rect.y + r.randint(0,10)
        if self.rect.y > 450:
            print("No longer possible")
            self.kill()
        
    
sprites = pg.sprite.Group()
init_screen=main(1000,500)

e1=enemySprite(100,200,10,init_screen.screen)
e2=enemySprite(200,200,10,init_screen.screen)
e3=enemySprite(300,200,10,init_screen.screen)
e4=enemySprite(400,200,10,init_screen.screen)
e5=enemySprite(500,200,10,init_screen.screen)
e6=enemySprite(600,200,10,init_screen.screen)
e7=enemySprite(700,200,10,init_screen.screen)
e8=enemySprite(800,200,10,init_screen.screen)
e9=enemySprite(900,200,10,init_screen.screen)

sprites.add(e1,e2,e3,e4,e5,e6,e7,e8,e9)

for item in sprites:
    print(item.rect.x)

screen.fill("Black")
sprites.draw(screen)
pg.display.update()
print(sprites.sprites())

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                #screen.fill("Black")
                for item in sprites:
                    item.moveRandomDown()
                #print(item.rect.y)
                screen.fill("Black")
                print("DOWN")

    sprites.draw(screen)
    pg.display.update()