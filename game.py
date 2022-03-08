import pygame as pg
import random as r

global bigLogo
logoIcon = pg.image.load("logo.png")
logoIcon= pg.transform.scale(logoIcon, (40, 40))

screen = pg.display.set_mode((1000,450))
taken_coords = ["200:250,300:400","500:800,300:400","50:150,450:550","850:950,450:550","450:550,300:400"]
points=0
level=1
bank=0
name="Joe"

global health
health=900

pg.init()

def hasCollided(taken,rect_x,rect_y):
    for item in taken:
        split=item.split(",")
        x=split[0]
        y=split[1]
        x=x.split(":")
        y=y.split(":")
        if rect_x  >= int(x[0]) and rect_x <= int(x[1]) and rect_y + 50 >= int(y[0]) and rect_y <= int(y[1]):
            return True

class Rectangle():
    def __init__(self, x, y, l, h, screen, colour):
        self.x = x
        self.y = y
        self.l = l
        self.h = h
        pg.draw.rect(screen, colour, pg.Rect(self.x, self.y, self.l, self.h))

class Turret(Rectangle):
    def __init__(self,x,y,size,screen,colour):
        self.x = x
        self.y = y
        self.screen = screen
        self.bullets = pg.sprite.Group()
        super().__init__(x, y, size, size, screen, "Black")
        pg.draw.rect(screen, colour, pg.Rect(self.x+3, self.y+3, self.l-6, self.h-6))
        pg.draw.rect(screen,"Black", pg.Rect(self.x+size/2 - 6, self.y+4, 12 ,size/2))
        pg.draw.circle(screen, "Black", (self.x+size/2,self.y+size/2), 15)

    def bulletGen(self):
        bulletTest=Bullet(self.screen,50,100)
        self.bullets.add(bulletTest)

class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        #self.image = pg.draw.rect(screen, "Orange", pg.Rect(x, y, 7, 10))
        self.image = pg.transform.scale((pg.image.load("bullet.png")),(10,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.y-1
        print("moved")

class main:
    def __init__(self, windowX, windowY):
        self.screen = pg.display.set_mode((windowX, windowY))
        pg.display.set_caption("Discipline Tower Defence")
        self.screen.fill("White")
        pg.display.flip()
        self.turrets=[]

    def initialise(self,points,level,bank,name,health):
        font=pg.font.SysFont("sans-serif",60)
        topBar=Rectangle(0,0,1000,40,self.screen,"Grey")
        self.screen.blit(logoIcon,(0,0))
        self.screen.blit(font.render(str(points),False,"Black"),(160,2))
        self.screen.blit(font.render(("Level "+str(level)),False,"Black"),(310,2))
        self.screen.blit(font.render(("$"+str(bank)),False,"Black"),(600,2))
        self.screen.blit(font.render(name,False,"Black"),(750,2))
        progBarOutline=Rectangle(60,55,904,28,self.screen,"Black")
        progBar=Rectangle(62,57,health,24,self.screen, "Green")
        
    def generateBlocks(self):
        rect1=Rectangle(200,300,50,100,self.screen,"Blue")
        rect2=Rectangle(500,300,300,100,self.screen,"Blue")
        self.turrets = [Turret(50,450,100,self.screen,"Red"),Turret(850,450,100,self.screen,"Red"),Turret(450,300,100,self.screen,"Red")]
        
        

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

    def moveRandomDown(self,taken):
        collided=hasCollided(taken, self.rect.x, self.rect.y)
        if collided == True:
            #print("Moving around")
            self.rect.x = self.rect.x + r.randint(0,5)
        elif self.rect.y + 50 > 600:
            global health
            health=health-20
            self.kill()
        else:
            #print("Moving Down")
            self.rect.y = self.rect.y + r.randint(0,5)

sprites = pg.sprite.Group()
bullets = pg.sprite.Group()
init_screen=main(1000,600)

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

#for item in sprites:
    #print(item.rect.x)

screen.fill("White")
sprites.draw(screen)
pg.display.update()
print(sprites.sprites())
for instance in init_screen.turrets:
        instance.bulletGen()


while True:
    #for event in pg.event.get():
        #if event.type == pg.KEYDOWN:
            #if event.key == pg.K_DOWN:
                #screen.fill("Black")
                #for item in sprites:
                    #item.moveRandomDown(taken_coords)
                    #print("Again!")
                #print(item.rect.y)
                #screen.fill("Black")
                #print("DOWN")

    for item in sprites:               
        item.moveRandomDown(taken_coords)
    for instance in init_screen.turrets:
        print("Loop1")
        for item in instance.bullets:
            print("Loop2")
            item.move()
    screen.fill("White")
    init_screen.initialise(points,level,bank,name,health)
    init_screen.generateBlocks()
    #bullets.add(init_screen.turret1.bullet1)
    sprites.draw(screen)
    for instance in init_screen.turrets:
        instance.bullets.draw(init_screen.screen)
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(20)
