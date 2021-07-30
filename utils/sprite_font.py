import pygame as pg
import pygame.gfxdraw

class sprite_font(pg.sprite.Sprite):
    def __init__(self, screen, text, pos, size, font = "Arial", bg = pg.Color("white"), txt_color = pg.Color("black")):
        super().__init__()
        
        self.max_size = screen.get_size()
        self.screen = screen
        
        # SET FONT
        if font in pg.font.get_fonts():
            self.font = pg.font.SysFont(font, size)
        else:
            self.font = pg.font.Font(font, size)
        
        # SET SPRITE SIZE
        self.width, self.height = self.get_size(pos, text, size, self.font)
        self.image = pg.Surface((self.width, self.height))
        self.color = bg
        self.image = self.image.convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        
        # SET RECTANGLE
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, bg, self.rect, border_radius=10)
        self.rect.topleft = pos
        
        self.blit_text(self.image, text, (0, 0), self.font, color = txt_color)        
        return
        
    def blit_text(self, surface, text, pos, font, color=pg.Color('black')):
                
        words = self.words
                
        max_width, max_height = self.max_size
        x, y = pos
                
        for line in words:
            text_render = font.render(line, 1, color)
            word_width, word_height = text_render.get_size()
                          
            surface.blit(text_render, (x, y))
                            
            y += word_height  # Start on new row.
        return
    
    def get_size(self,pos,  text, size, font, color=pg.Color('white')):
        
        words = [word for word in text.splitlines()]  # 2D array where each row is a list of words.
        self.words = words
        
        width, height = 0, 0
        
        for line in words:
            word_surface = font.render(line, 0, color)
            word_width, word_height = word_surface.get_size()
            
            if width < word_width:
                width = word_width
                
            height += word_height
                
        return width, height
    
    
#     def draw_text(self, text, font, color, surface, x, y, blit = True):
#         textobj = font.render(text, 1, color)
#         textrect = textobj.get_rect()
#         textrect.topleft = (x, y)
#         if blit:
#             surface.blit(textobj, textrect)
#         return textobj, textrect
