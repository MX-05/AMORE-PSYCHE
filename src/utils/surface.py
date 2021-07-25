import pygame
from utils.image import sprite

class display():
    def __init__(self, background, size, FPS= 50):
        self.FPS = FPS
    
        # SCREEN
    
        self.screen= pygame.display.set_mode(size)
        
        if type(background) == type(""):        # image as background
            self.background = sprite([0, 0], path=background)
            
        if type(background) == type(('r', 'g', 'b')):   # color as background
            self.background = background
            self.screen.fill((background))
        return
        
    def update(self):
        if type(self.background) == type(sprite([0,0])):
            self.screen.blit(self.background.image, (0, 0))
            
        pygame.display.update()
        pygame.time.Clock().tick(self.FPS)
        
        return
    
    def debug(self, x=0, y=0, mode = ["mouse"]):
        if mode[0].lower() == "mouse":
            print(f"\t X: {x} | Y: {y};")
            
        if mode[0].lower() == "hit-box":
            hit_box = pygame.Rect(mode[1].x, mode[1].y, mode[1].width, mode[1].height)
            pygame.draw.rect(self.screen, (231, 18, 15, 225), hit_box)
        return