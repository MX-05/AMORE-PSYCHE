import pygame as pg

class sprite_font(pg.sprite.Sprite):
    def __init__(self, screen, text, pos, size, bg = pg.Color("white"), txt_color = pg.Color("black")):
        super().__init__()
        
        self.max_size = screen.get_size()
        
        self.width, self.height = self.get_size(pos, text, size)
        self.image = pg.Surface((self.width, self.height))
        self.bg = bg
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
