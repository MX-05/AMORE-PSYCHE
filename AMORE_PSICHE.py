# IMPORT LIBRARIES
import pygame as pg
import sys

from ignore.button_2 import Button

class sprite_font(pg.sprite.Sprite):
    def __init__(self, screen, text, pos, size, bg = pg.Color("white")):
        super().__init__()
        
        self.max_size = screen.get_size()
        
        self.width, self.height = self.get_size(pos, text, size)
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(bg)
        
        self.blit_text(screen, text, pos, size)        
                
        self.rect = self.image.get_rect()
        return
        
    def blit_text(self, surface, text, pos, size, color=pg.Color('black')):
        font = pg.font.SysFont("Arial", size)
                
        words = self.words
        space = self.space
                
        max_width, max_height = self.max_size
        x, y = pos
                
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                    
                self.image.blit(word_surface, (x, y))
                
                x += word_width + space
                            
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        return
    
    def get_size(self,pos,  text, size, color=pg.Color('white')):
        font = pg.font.SysFont("Arial", size)
        
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        self.words, self.space = words, space
        
        max_width, max_height = self.max_size
        width, height = 0, 0
        x, y = pos
        
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                
                if x + word_width >= max_width:
                    height += word_height  # Start on new row.
                
                width = width + word_width + space
            height += word_height
        
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
    "color": "black"
}
pg.display.set_caption(display['caption'])
surface = pg.display.set_mode((display['width'], display['height']))

font = pg.font.SysFont("Arial", 20)

# ------------------------------------- MENU ------------------------------------- #

# BUTTON SETUP
play = Button("Play", (300, 210), 50, bg=(225, 0, 0))
audio = Button("Audio ON",(295, 280), 25, bg = "blue")

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

credits = sprite_font(surface, text_credits, (20, 330), 20)

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
                audio.change_text("Audio off ")
            else:
                audio.change_text("Audio ON", bg="blue")
    
    # pg.draw.rect(surface, (40, 44, 52), (0, 330, surface.get_width(), surface.get_height()-330))
    
    menu.draw(surface)
    clock.tick(60)
    pg.display.update()