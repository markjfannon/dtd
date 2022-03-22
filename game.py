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

class Shop():
    def __init__(self, x, y, screen):
        self.shopfont=pg.font.SysFont("sans-serif",30)
        self.bodyfont=pg.font.SysFont("sans-serif",25)
        exitCross = pg.image.load("cross.png")
        exitCross = pg.transform.scale(exitCross, (50, 50))
        self.x = x
        self.y = y
        self.l = 600
        self.h = 450
        self.screen = screen
        outline = [Rectangle(self.x, self.y, self.l, self.h, self.screen, "Black"),
                   Rectangle(self.x+2, self.y+2, self.l-4, self.h-4, self.screen, "Grey")]
        self.screen.blit(exitCross,(self.x+self.l-50, self.y))
        lines = [Rectangle(self.x,self.y+50,self.l,2, self.screen, "Black"),
        Rectangle(self.x,self.y+185,self.l,2, self.screen, "Black"),
        Rectangle(self.x,self.y+315,self.l,2, self.screen, "Black")]
        item1 = [Rectangle(self.x+20, self.y+70, 100, 100, self.screen, "Black"),Rectangle(self.x+22, self.y+72, 96, 96, self.screen, "Brown")]
        item2 = [Rectangle(self.x+20, self.y+200, 100, 100, self.screen, "Black"),Rectangle(self.x+22, self.y+202, 96, 96, self.screen, "Yellow")]
        item3 = [Rectangle(self.x+20, self.y+335, 100, 100, self.screen, "Black"),Rectangle(self.x+22, self.y+337, 96, 96, self.screen, "Blue")]
        self.screen.blit(self.shopfont.render(("Bronze Turret"),False,"Black"),(self.x+145,self.y+75))
        self.screen.blit(self.bodyfont.render(("This turret does a small amount of damage"),False,"Black"),(self.x+145,self.y+100))
        self.screen.blit(self.shopfont.render(("Silver Turret"),False,"Black"),(self.x+145,self.y+210))
        self.screen.blit(self.bodyfont.render(("This turret does a medium amount of damage"),False,"Black"),(self.x+145,self.y+235))
        self.screen.blit(self.shopfont.render(("Chrome Turret"),False,"Black"),(self.x+145,self.y+340))
        self.screen.blit(self.bodyfont.render(("This turret does a large amount of damage"),False,"Black"),(self.x+145,self.y+365))
        self.screen.blit(self.shopfont.render(("$100"),False,"Black"),(self.x+self.l-50,self.y+160))
        self.screen.blit(self.shopfont.render(("$200"),False,"Black"),(self.x+self.l-50,self.y+290))
        self.screen.blit(self.shopfont.render(("$500"),False,"Black"),(self.x+self.l-50,self.y+420))
        buy1 = [Rectangle(self.x+145,self.y+130,90,40,self.screen,"Black"),Rectangle(self.x+147,self.y+132,86,36,self.screen,"Green")]
        buy2 = [Rectangle(self.x+145,self.y+260,90,40,self.screen,"Black"),Rectangle(self.x+147,self.y+262,86,36,self.screen,"Green")]
        buy3 = [Rectangle(self.x+145,self.y+394,90,40,self.screen,"Black"),Rectangle(self.x+147,self.y+396,86,36,self.screen,"Green")]
        self.screen.blit(self.shopfont.render(("Buy"),False,"Black"),(self.x+165,self.y+140))
        self.screen.blit(self.shopfont.render(("Buy"),False,"Black"),(self.x+165,self.y+270))
        self.screen.blit(self.shopfont.render(("Buy"),False,"Black"),(self.x+165,self.y+404))
        
    def update (self,position):
        if position[0] in range(self.x+self.l-50,self.x+self.l) and position[1] in range(self.y, self.y + 50):
            global shop, running
            shop=False
            running=True

    def isOver (self, position):
        if position[0] in range(self.x+145,self.x+235) and position[1] in range(self.y+130,self.y+170):
            self.screen.blit(self.shopfont.render(("Buy"),False,"Red"),(self.x+165,self.y+140))
        elif position[0] in range(self.x+145,self.x+235) and position[1] in range(self.y+260,self.y+300):
            self.screen.blit(self.shopfont.render(("Buy"),False,"Red"),(self.x+165,self.y+270))
        elif position[0] in range(self.x+145,self.x+235) and position[1] in range(self.y+394,self.y+434):
            self.screen.blit(self.shopfont.render(("Buy"),False,"Red"),(self.x+165,self.y+404))

    def click (self, position):
        global bank
        if position[0] in range(self.x+145,self.x+235) and position[1] in range(self.y+130,self.y+170):
            bank=bank-100
        elif position[0] in range(self.x+145,self.x+235) and position[1] in range(self.y+260,self.y+300):
            bank=bank-200
        elif position[0] in range(self.x+145,self.x+235) and position[1] in range(self.y+394,self.y+434):
            bank=bank-500
        
class Turret(Rectangle):
    def __init__(self,x,y,size,screen,colour, v):
        self.x = x
        self.y = y
        self.size=size
        self.screen = screen
        self.bullets = pg.sprite.Group()
        self.v = v
        super().__init__(x, y, size, size, screen, "Black")
        pg.draw.rect(screen, colour, pg.Rect(self.x+3, self.y+3, self.l-6, self.h-6))
        pg.draw.rect(screen,"Black", pg.Rect(self.x+size/2 - 6, self.y+4, 12 ,size/2))
        pg.draw.circle(screen, "Black", (self.x+size/2,self.y+size/2), 15)
    def shoot(self):
        los=False
        global enemy_coords
        for item in enemy_coords:
            enemy=item.split(",")
            #print(enemy)
            if int(enemy[0]) > self.x and int(enemy[0]) < self.x+self.size  and int(enemy[1]) > 200:
                #print((item.split(","))[0])
                los=True
                break
        global bullets
        if len(bullets) > 50:
            pass
        elif los == False:
            pass
        else:
            n=r.randint(1,8)
            if n > 2:
                pass
            else:
                bullets.add(Bullet(self.screen,r.randint(self.x,self.x+90),self.y,self.v))
            #print("generated")


class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, x, y, v):
        super().__init__()
        #self.image = pg.draw.rect(screen, "Orange", pg.Rect(x, y, 7, 10))
        self.image = pg.transform.scale((pg.image.load("bullet.png")),(10,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = v

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
            self.rect.y=self.rect.y - self.speed

class main:
    def __init__(self, windowX, windowY):
        self.screen = pg.display.set_mode((windowX, windowY))
        pg.display.set_caption("Discipline Tower Defence")
        self.screen.fill("White")
        pg.display.flip()
        self.turrets=[]

    def initialise(self,points,level,bank,name,health):
        font=pg.font.SysFont("sans-serif",60)
        shopfont=pg.font.SysFont("sans-serif",50)
        topBar=Rectangle(0,0,1000,40,self.screen,"Grey")
        self.screen.blit(logoIcon,(0,0))
        self.screen.blit(font.render(str(points),False,"Black"),(160,2))
        self.screen.blit(font.render(("Level "+str(level)),False,"Black"),(310,2))
        self.screen.blit(font.render(("$"+str(bank)),False,"Black"),(600,2))
        self.screen.blit(font.render(name,False,"Black"),(750,2))
        shopButton=Rectangle(910,0,90,40,self.screen,"Black")
        shopButtonInner=Rectangle(912,2,86,36,self.screen,"Green")
        self.screen.blit(shopfont.render("Shop",False,"Black"),(912,2))
        progBarOutline=Rectangle(60,55,904,28,self.screen,"Black")
        progBar=Rectangle(62,57,health,24,self.screen, "Green")
        
    def generateBlocks(self):
        #rect1=Rectangle(200,300,50,100,self.screen,"Blue")
        #rect2=Rectangle(500,300,300,100,self.screen,"Blue")
        self.turrets = [Turret(50,450,100,self.screen,"Red",4),Turret(850,450,100,self.screen,"Red",2),Turret(450,300,100,self.screen,"Red",5)]
        
        

class enemySprite(pg.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = pg.transform.scale((pg.image.load("creature1.png")),(50,50))
        #pg.draw.rect(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
            if r.randint(1,10) == 7:
                self.rect.x = self.rect.x + r.randint(0,5)
            else:
                self.rect.y = self.rect.y + r.randint(0,5)

start=input("Start?")

sprites = pg.sprite.Group()
bullets = pg.sprite.Group()
init_screen=main(1000,600)
shop1=Shop(20,35,init_screen.screen)
init_screen.generateBlocks()

for item in init_screen.turrets:
    item.shoot()


screen.fill("White")
sprites.draw(screen)
bullets.draw(screen)
pg.display.update()
print(sprites.sprites())

shop=False
running=True

while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos=pg.mouse.get_pos()
            if pos[0] >= 910 and pos[1] >= 0 and pos[1] <= 40:
                print("shop!")
                shop=True
                running=False
            if shop == True:
                shop1.update(pos)
                shop1.click(pos)
                
    
    if len(sprites) > 10:
        pass
    else:
        sprites.add(enemySprite(r.randint(1,900),100,init_screen.screen))
    enemy_coords= []

    if running == True:
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
    if shop == True:
        shop1=Shop(20,35,init_screen.screen)
        shop1.isOver(pg.mouse.get_pos())
        pg.display.flip()
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(20)
