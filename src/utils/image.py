import pygame

class button():

    def __init__(self, coords, tolleranza = 0):
        
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.tolleranza = tolleranza
    
        return
    
    def make(self, screen, size ,colour = (241, 197, 49), image = ""):
        
        self.colour = colour
        
        if image != "": 
            self.image = sprite((self.x, self.y), width = size[0], height= sixe[1])
            self.hit_box = self.image.hit_box()
        else:
            self.image = sprite(self.coords, path= image)
            self.hit_box = self.image.hit_box(self.tolleranza)
        
        return self.image
    
    def upadte(self, screen):
        try:
            pygame.draw.rect(screen, self.colour, self.image)
        except:
            screen.blit(self.image, self.coords)
        screen.update()
                
        return
    
    def on_click(self, x, y):
        cl = self.hit_box
        if x <  cl["destra"] and x > cl["sinistra"]:
            if y > cl['su'] and y < cl['giu']:
                return True

class sprite():
    def __init__(self, coords, width = 50, height = 50, path = ""):
        self.x = coords[0]
        self.y = coords[1]
        
        if path != "":
            self.image = pygame.image.load(path)
        else:
            self.image = pygame.Rect(self.x, self.y, 50, 50)
            self.width = width
            self.height = height
        
        return
    
    def __str__(self):
        return "a subclasses of pygame.sprite"
    
    def hit_box(self, tolleranza =0):
        
        
        if type(self.image) == type(pygame.Rect()):
            return {
                "destra": self.x + self.width, 
                "sinistra": self.x, 
                "su": self.y, 
                "giu": self.y + self.height
            }
        dx = self.x +self.image.get_width() - tolleranza
        sx = self.x + tolleranza

        su = self.y + tolleranza + tolleranza
        giu = self.y + self.image.get_height() -tolleranza

        return {"destra": dx, "sinistra": sx, "su": su, "giu": giu}

class display():
    def __init__(self, background, size, FPS= -1):
        if FPS <0: 
            self.FPS = 50
        else:
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
        if type(self.background) == type(sprite()):
            self.screen.blit(self.background.image, (0, 0))
            
        pygame.display.update()
        pygame.time.Clock().tick(self.FPS)
        
        return