# IMPORT LIBRARIES
import pygame as pg
import sys

from ignore.button_2 import Button

class sprite_font(pg.sprite.Sprite):
    def __init__(self, screen, text, pos, size, bg = pg.Color("white"), txt_color = pg.Color("black")):
        super().__init__()
        
        self.max_size = screen.get_size()
        
        self.width, self.height = self.get_size(pos, text, size)
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(bg)
        
        self.rect = self.image.get_rect()
                
        self.rect.topleft = pos
        
        self.blit_text(screen, text, (0, 0), size, color = txt_color)        
        return
        
    def blit_text(self, surface, text, pos, size, color=pg.Color('black')):
        font = pg.font.SysFont("Arial", size)
                
        words = self.words
                
        max_width, max_height = self.max_size
        x, y = pos
                
        for line in words:
            text_render = font.render(line, 1, color)
            word_width, word_height = text_render.get_size()
                          
            self.image.blit(text_render, (x, y))
                            
            y += word_height  # Start on new row.
        return
    
    def get_size(self,pos,  text, size, color=pg.Color('white')):
        font = pg.font.SysFont("Arial", size)
        
        words = [word for word in text.splitlines()]  # 2D array where each row is a list of words.
        self.words = words
        
        width, height = 0, 0
        
        for line in words:
            word_surface = font.render(line, 0, color)
            word_width, word_height = word_surface.get_size()
            
            if width < word_width:
                width = word_width
                
            height += word_height
        
        print (width, height)
        
        return width, height

#     def draw_text(self, text, font, color, surface, x, y, blit = True):
#         textobj = font.render(text, 1, color)
#         textrect = textobj.get_rect()
#         textrect.topleft = (x, y)
#         if blit:
#             surface.blit(textobj, textrect)
#         return textobj, textrect


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