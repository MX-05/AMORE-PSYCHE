# IMPORT LIBRARIES
import pygame as pg
import sys

from ignore.button_2 import Button

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
play = Button("Play", (300, 210), 50, bg=(225, 0, 0))
audio = Button("Audio ON",(295, 280), 25, bg = "blue", txt_color=pg.Color("white"))

menu = pg.sprite.Group()
menu.add(audio)
menu.add(play)

# CREDITS SETUP
text_credits = """DEVELOPER: Marco Mazzeo
GRAPHICS: Mia Masetti
SOUNDS: Luca Pasqualetti & Cosimo Losurdo
DOPPIAGGIO: Tiago Pisanti Vieira
MAPPA ESPOLORAZIONE: Milo Binetti
"""

credits = sprite_font(surface, text_credits, (20, 330), 20, bg=(100, 100, 100))

menu.add(credits)

while True:
    
    mouse = pg.mouse
    
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
            else:
                audio.change_text("Audio ON", bg="blue", txt_color= pg.Color("white"))
    
    # pg.draw.rect(surface, (40, 44, 52), (0, 330, surface.get_width(), surface.get_height()-330))
    
    menu.draw(surface)
    clock.tick(60)
    pg.display.update()