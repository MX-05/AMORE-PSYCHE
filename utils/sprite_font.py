import pygame as pg
import pygame.gfxdraw

class sprite_font(pg.sprite.Sprite):
    def __init__(self, screen, text, pos, size, bg = pg.Color("white"), txt_color = pg.Color("black")):
        super().__init__()
        
        self.max_size = screen.get_size()
        self.screen = screen
        
        self.width, self.height = self.get_size(pos, text, size)
        self.image = pg.Surface((self.width, self.height))
        self.color = bg
        self.image.fill(bg)
        
        self.rect = self.image.get_rect()
                
        self.rect.topleft = pos
        self.draw_rounded_rect(5)
        self.blit_text(screen, text, pos, size, color = txt_color)        
        return
        
    def blit_text(self, surface, text, pos, size, color=pg.Color('black')):
        font = pg.font.SysFont("Arial", size)
                
        words = self.words
                
        max_width, max_height = self.max_size
        x, y = pos
                
        for line in words:
            text_render = font.render(line, 1, color)
            word_width, word_height = text_render.get_size()
                          
            surface.blit(text_render, (x, y))
                            
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
    
    def draw_rounded_rect(self, corner_radius, surface ="",rect = "", color=""):
        ''' Draw a rectangle with rounded corners.
        Would prefer this: 
            pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
        but this option is not yet supported in my version of pygame so do it ourselves.

        We use anti-aliased circles to make the corners smoother
        '''#  (16, 152, 104)
        if surface == "":
            surface = self.screen
        if rect == "":
            rect = self.rect
        if color == "":
            color = self.color
        if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
            raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

        # need to use anti aliasing circle drawing routines to smooth the corners
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        rect_tmp = pygame.Rect(rect)

        rect_tmp.width -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)

        rect_tmp.width = rect.width
        rect_tmp.height -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)
    
#     def draw_text(self, text, font, color, surface, x, y, blit = True):
#         textobj = font.render(text, 1, color)
#         textrect = textobj.get_rect()
#         textrect.topleft = (x, y)
#         if blit:
#             surface.blit(textobj, textrect)
#         return textobj, textrect
