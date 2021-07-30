# IMPORT LIBRARIES
import pygame as pg
import sys

from utils import *

# GENERAL SETUP
pg.init()
clock = pg.time.Clock()

font = "./font/diogenes/DIOGENES.ttf"

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

# ------------------------------------- MENU ------------------------------------- #

# BUTTON SETUP
play = Button((0,0)).B_text(
    " Play ", [font, 65], 
    bg= (124, 99, 156), color="White", radius=20
)
audio = Button((295, 420)).B_text(
    " Audio ON ", [font, 25],
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
    text_credits, (10, 0), 
    15, font = font, 
    bg=(62, 62, 62), 
    txt_color="White"
)

credits.rect.bottom = surface.get_rect().bottom - 10
credits.image.set_alpha(157)
credits.image = credits.image.convert_alpha()

menu.add(credits)


# SKIN SETUP
skin = {
    "button": Button((0, 0)).B_text(
        " SKIN ", [font, 25], 
        bg = (255, 174, 0), color="white", radius=15
    ),
    "image": Button((865, 100), path = "./assets/pg_pattuglie/pg_tigre.png"),
    "menu": Button(
        (0, 0),                         # POS
        size = [752, 641]               # SIZE
    )
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
        #pg.time.delay(25)
        
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

# draw rect skin menu
pg.draw.rect(skin["menu"].image, ("white"), skin["menu"].rect, border_radius= 30)
skin["menu"].image = skin["menu"].image.convert()
skin["menu"].image.set_colorkey((0, 0, 0))

skin["menu"].rect.center = surface.get_rect().center  # POS
skin["menu"].rect.top = surface.get_rect().bottom# POS

# animation variable
def restart_animation():
    global exit_SkinMenu, open_SkinMenu, click
    global vel, a
    exit_SkinMenu = False
    open_SkinMenu = False
    click = False
    vel = 0
    a = 0.5 
restart_animation()
# TODO: add select skins buttons
# TODO: add exit button 

menu.add(skin["asset"])
menu.add(skin["button"])

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
        
        if play.click(event) and not click:
            print("FUNGEEEEEEE")
        
        if audio.click(event) and not click:
            if audio.content.lower().strip() == "audio on":
                audio.change_text(" Audio OFF ", bg=(255, 174, 0), txt_color="white", radius=15)
                audio.image.set_alpha(157)
                audio.image = audio.image.convert_alpha()
                audio.rect.centerx = surface.get_rect().centerx
            else:
                audio.change_text(" Audio ON ", bg=(255, 174, 0), txt_color= pg.Color("white"), radius=15)
                audio.rect.centerx = surface.get_rect().centerx
        
        if skin["button"].click(event) and not click:
            open_SkinMenu = True
            menu.add(skin["menu"])
        
        if event.type == pg.MOUSEBUTTONDOWN and not skin["menu"].rect.collidepoint(mx, my) and click:
            exit_SkinMenu = True
        
    if exit_SkinMenu:
        if skin["menu"].rect.y >= surface.get_rect().bottom:
            menu.remove(skin["menu"])
            restart_animation()
        else:                
            vel += a
            skin["menu"].rect.y += vel 
    
    if open_SkinMenu:
        if skin["menu"].rect.center >= surface.get_rect().center:
            vel += a
            skin["menu"].rect.y -= vel
            
            if pg.MOUSEBUTTONDOWN in pg.event.get(eventtype=pg.MOUSEBUTTONDOWN): print("click")
        else:
            restart_animation()
            click = True
    
    surface.blit(display["background"], (0,0))
    menu.draw(surface)
    menu.update()
    clock.tick(60)
    pg.display.update()