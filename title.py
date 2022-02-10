import pygame
import sys
# Initialize pygame
pygame.init()
#scren dimension
sur_obj=pygame.display.set_mode((300,200))
# Screen caption
pygame.display.set_caption("Text in Pygame")
font_color=(0,150,250)
font_obj=pygame.font.SysFont("sans-serif",25)
# Render the objects
text_obj=font_obj.render("Welcome to Pygame",True,font_color)
while True:
   sur_obj.fill((255,255,255))
   sur_obj.blit(text_obj,(22,0))
   for eve in pygame.event.get():
      if eve.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
   pygame.display.update()
