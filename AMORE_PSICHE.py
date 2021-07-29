# IMPORT LIBRARIES
import pygame as pg
import sys

from utils import *

# GENERAL SETUP
pg.init()
clock = pg.time.Clock()

# SCREEN SETUP
display = {
    'width': 1280,
    'height': 720,
    'caption': "AMORE ~ PSICHE",
    "color": "white"
}
pg.display.set_caption(display['caption'])
surface = pg.display.set_mode((display['width'], display['height']), pg.SCALED + pg.RESIZABLE)
surface.fill(display["color"])

font = pg.font.SysFont("Arial", 20)

# ------------------------------------- MENU ------------------------------------- #

# BUTTON SETUP
play = Button((0,0)).B_text(
    " Play ", ["Arial", 50], 
    bg= (255, 0, 0), radius=20
)
audio = Button((295, 395)).B_text(
    " Audio ON ", ["Arial", 25],
    bg = (255, 174, 0), color="white", radius = 15 
)
skin = {
    "button": Button((0, 0)).B_text(
        " SKIN ", ["Arial", 25], 
        bg = (255, 174, 0), color="white", radius=15
    ),
    "asset": Button((865, 50), path = "./assets/pg_pattuglie/pg_tigre.jpeg")
}
print (skin["asset"].image.get_size())
skin["asset"].image = pg.transform.scale(skin["asset"].image, (300, 400))
# skin["asset"].image.fill

play.rect.center = [surface.get_rect().centerx, surface.get_rect().centery]
audio.rect.centerx = surface.get_rect().centerx
skin["button"].rect.center = (1000, 450)

menu = pg.sprite.Group()
menu.add(audio)
menu.add(play)
menu.add(skin["asset"])
menu.add(skin["button"])

# CREDITS SETUP
text_credits = """
    DEVELOPER: Marco Mazzeo 
    GRAPHICS: Mia Masetti   
    SOUNDS: Luca Pasqualetti & Cosimo Losurdo    
    DOPPIAGGIO: Tiago Pisanti Vieira    
    MAPPA ESPOLORAZIONE: Milo Binetti   

"""

credits = sprite_font(surface, text_credits, (10, 0), 15, bg=(0, 0, 0, 3.0), txt_color="White")

credits.rect.bottom = surface.get_rect().bottom - 10

menu.add(credits)
move = False


while True:
    
    mouse = pg.mouse
    mx, my = mouse.get_pos()
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        if event.type == pg.MOUSEBUTTONDOWN:
            print(mouse.get_pos())
        
        if play.click(event):
            print("FUNGEEEEEEE")
        
        if audio.click(event):
            if audio.content.lower().strip() == "audio on":
                surface.fill(display["color"])
                audio.change_text(" Audio OFF ", bg=(255, 174, 0), txt_color="white", radius=15)
                audio.rect.centerx = surface.get_rect().centerx
            else:
                surface.fill(display["color"])
                audio.change_text(" Audio ON ", bg=(255, 174, 0), txt_color= pg.Color("white"), radius=15)
                audio.rect.centerx = surface.get_rect().centerx
    
    menu.draw(surface)
    clock.tick(60)
    pg.display.update()