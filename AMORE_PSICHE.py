# IMPORT LIBRARIES
import pygame as pg
import sys

from utils import *

# GENERAL SETUP
pg.init()
clock = pg.time.Clock()

# SCREEN SETUP
display = {
    'width': 720,
    'height': 480,
    'caption': "AMORE ~ PSICHE",
    "color": "white"
}
pg.display.set_caption(display['caption'])
surface = pg.display.set_mode((display['width'], display['height']))
surface.fill(display["color"])

font = pg.font.SysFont("Arial", 20)

# ------------------------------------- MENU ------------------------------------- #

# BUTTON SETUP
play = Button((0,0)).B_text("Play", ["Arial", 50], bg= (255, 0, 0))
audio = Button((295, 280)).B_text("Audio ON", ["Arial", 25], bg = "Blue", color="White")

play.rect.center = [surface.get_rect().centerx/2, surface.get_rect().centery]
audio.rect.centerx = surface.get_rect().centerx/2

menu = pg.sprite.Group()

# CREDITS SETUP
text_credits = """
    DEVELOPER: Marco Mazzeo 
    GRAPHICS: Mia Masetti   
    SOUNDS: Luca Pasqualetti & Cosimo Losurdo    
    DOPPIAGGIO: Tiago Pisanti Vieira    
    MAPPA ESPOLORAZIONE: Milo Binetti   

"""

credits = sprite_font(surface, text_credits, (140, 310), 10, bg=(100, 100, 100))

menu.add(audio)
menu.add(play)
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
            if audio.content.lower() == "audio on":
                surface.fill(display["color"])
                audio.change_text("Audio off ", bg="white")
                audio.rect.centerx = surface.get_rect().centerx
            else:
                audio.change_text("Audio ON", bg="blue", txt_color= pg.Color("white"))
                audio.rect.centerx = surface.get_rect().centerx
    
    menu.draw(surface)
    clock.tick(60)
    pg.display.update()