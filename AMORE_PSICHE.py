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
    "color": "white",
    "background": pg.image.load("./assets/bg_menu.jpg")
}
# set surfice
pg.display.set_caption(display['caption'])
surface = pg.display.set_mode((display['width'], display['height']), pg.SCALED + pg.RESIZABLE)

# background
surface.fill(display["color"])
display["background"] =  pg.transform.scale(display["background"], (1280, 720))
surface.blit(display["background"], (0,0))

font = pg.font.SysFont("Arial", 20)

# ------------------------------------- MENU ------------------------------------- #

# BUTTON SETUP
play = Button((0,0)).B_text(
    " Play ", ["Arial", 50], 
    bg= (124, 99, 156), color="White", radius=20
)
audio = Button((295, 395)).B_text(
    " Audio ON ", ["Arial", 25],
    bg = (255, 174, 0), color="white", radius = 15 
)


# SET BUTTONS COORDS
play.rect.center = [surface.get_rect().centerx, surface.get_rect().centery]
audio.rect.centerx = surface.get_rect().centerx

menu = pg.sprite.Group()
menu.add(audio)
menu.add(play)

# CREDITS SETUP
text_credits = """
    DEVELOPER: Marco Mazzeo 
    GRAPHICS: Mia Masetti   
    SOUNDS: Luca Pasqualetti & Cosimo Losurdo    
    DOPPIAGGIO: Tiago Pisanti Vieira    
    MAPPA ESPOLORAZIONE: Milo Binetti   

"""

credits = sprite_font(
    surface, 
    text_credits, (10, 0), 15, 
    bg=(62, 62, 62), 
    txt_color="White"
)

credits.rect.bottom = surface.get_rect().bottom - 10

menu.add(credits)


# SKIN SETUP
skin = {
    "button": Button((0, 0)).B_text(
        " SKIN ", ["Arial", 25], 
        bg = (255, 174, 0), color="white", radius=15
    ),
    "image": Button((865, 100), path = "./assets/pg_pattuglie/pg_tigre.png"),
    "menu": Button((0, 0)) # TODO: set pos and size 
}

skin["image"].image = pg.transform.scale(skin["image"].image, (300, 400))

# set button coords
skin["button"].rect.centerx = 1000
skin["button"].rect.top = 510

# Animation variables
class skin_animation(Button):
    def __init__(self, pos, image = "", path = "", vel = 1):
        super().__init__(pos)
                
        # sprite variables
        if path != "":
            self.image = pg.image.load(path)
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
        if image != "":
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
            
        if path == "" and image == "":
            print("Error: make sure to set a path or an image")
        
        # animation variables
        self.vel = vel
        self.move = True
        self.center = self.rect.centery
        
        return
    
    def update(self):
        
        # SET ANIMATION VARIABLES    
        Ypoint = self.rect.centery
        distance = Ypoint - self.center -25 
        pg.time.delay(25)
        
        # GO DOWN
        if Ypoint >= self.center -26 and self.move == True:
            self.rect.centery += self.vel
            if Ypoint == self.center +25:
                self.move = False
        
        # GO UP
        if Ypoint <= self.center +25 and self.move == False:
            self.rect.centery -= self.vel
            if Ypoint == self.center-25:
                self.move = True
        return
        
skin["asset"] = skin_animation(skin["image"].pos, skin["image"].image)

# SKIN MENU
# TODO: draw rectangle
# TODO: blit skins 
# TODO: add select skins buttons
# TODO: add exit button 

menu.add(skin["asset"])
menu.add(skin["button"])
# menu.add(skin["menu"])

while True:
    
    mouse = pg.mouse
    mx, my = mouse.get_pos()
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        # DEBUG
        # TODO: levarlo alla fine   
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
           
    
    surface.blit(display["background"], (0,0))
    menu.draw(surface)
    menu.update()
    clock.tick(60)
    pg.display.update()