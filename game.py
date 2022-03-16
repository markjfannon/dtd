import pygame as pg
import random as r

global bigLogo
logoIcon = pg.image.load("logo.png")
logoIcon= pg.transform.scale(logoIcon, (40, 40))

screen = pg.display.set_mode((1000,450))
taken_coords = ["50:150,450:550","850:950,450:550","450:550,300:400"]
enemy_coords = []
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

def hasHit(taken,bullet_x,bullet_y):
    hit=False
    #print(taken)
    for item in taken:
        split=item.split(",")
        #print(split[0]+" - "+str(bullet_x))
        #print(split[1]+" - "+str(bullet_y))
        #if bullet_x + 10 >= int(split[0]) and bullet_x <= int(split[0]+50) and bullet_y <= int(split[1]) and bullet_y >= int(split[1]) + 50:
            #return True
        if bullet_x >= int(split[0]) and bullet_x <= int(split[0])+50 and bullet_y >= int(split[1]) and bullet_y <= int(split[1])+50:
            hit=True
            break
    if hit == True:
        for item in sprites:
            #print(str(item.rect.x)+" - "+split([0]))
            #print(str(item.rect.y)+" - "+split([1]))
            if item.rect.x == int(split[0]) and item.rect.y == int(split[1]):
                item.kill()
                global points
                global bank
                points=points+10
                bank=bank+r.randint(30,50)
                
        return True, split[0], split[1]
    else:
        return False, 0, 0

            

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
        self.size=size
        self.screen = screen
        self.bullets = pg.sprite.Group()
        super().__init__(x, y, size, size, screen, "Black")
        pg.draw.rect(screen, colour, pg.Rect(self.x+3, self.y+3, self.l-6, self.h-6))
        pg.draw.rect(screen,"Black", pg.Rect(self.x+size/2 - 6, self.y+4, 12 ,size/2))
        pg.draw.circle(screen, "Black", (self.x+size/2,self.y+size/2), 15)
    def shoot(self):
        los=False
        global enemy_coords
        for item in enemy_coords:
            enemy=item.split(",")
            print(enemy)
            if int(enemy[0]) > self.x and int(enemy[0]) < self.x+self.size  and int(enemy[1]) > 200:
                print((item.split(","))[0])
                los=True
                break
        global bullets
        if len(bullets) > 50:
            pass
        elif los == False:
            pass
        else:
            bullets.add(Bullet(self.screen,r.randint(self.x,self.x+90),self.y))
            print("generated")


class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        #self.image = pg.draw.rect(screen, "Orange", pg.Rect(x, y, 7, 10))
        self.image = pg.transform.scale((pg.image.load("bullet.png")),(10,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, coords):
        if self.rect.y <= 40:
            self.kill()
        else:
            self.enemy_x=0
            self.enemy_y=0
            c, self.enemy_x, self.enemy_y = hasHit(coords,self.rect.x,self.rect.y)
            if c == True:
                print("Hit")
                self.kill()
            self.rect.y=self.rect.y - 5

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
        #rect1=Rectangle(200,300,50,100,self.screen,"Blue")
        #rect2=Rectangle(500,300,300,100,self.screen,"Blue")
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
        self.hit = False 
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
init_screen.generateBlocks()

e1=enemySprite(100,200,10,init_screen.screen)
e2=enemySprite(200,200,10,init_screen.screen)
e3=enemySprite(300,300,10,init_screen.screen)
e4=enemySprite(400,200,10,init_screen.screen)
e5=enemySprite(500,200,10,init_screen.screen)
e6=enemySprite(600,200,10,init_screen.screen)
e7=enemySprite(700,200,10,init_screen.screen)
e8=enemySprite(800,200,10,init_screen.screen)
e9=enemySprite(900,200,10,init_screen.screen)

b1=Bullet(init_screen.screen,311,400)
b2=Bullet(init_screen.screen,400,400)

sprites.add(e1,e2,e3,e4,e5,e6,e7,e8,e9)

for item in init_screen.turrets:
    item.shoot()

screen.fill("White")
sprites.draw(screen)
bullets.draw(screen)
pg.display.update()
print(sprites.sprites())

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

    enemy_coords= []
    for item in sprites:               
        item.moveRandomDown(taken_coords)
        enemy_coords.append(str(item.rect.x)+","+str(item.rect.y))
    for item in init_screen.turrets:
        item.shoot()
    for item in bullets:
        item.move(enemy_coords)
    for item in sprites:
        if item.hit == True:
            item.kill()
    screen.fill("White")
    init_screen.initialise(points,level,bank,name,health)
    init_screen.generateBlocks()
    #bullets.add(init_screen.turret1.bullet1)
    sprites.draw(screen)
    bullets.draw(screen)
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(20)
