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
        
        if image == "": 
            self.image = pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, size[0], size[1]))
            self.hit_box = {"destra": size[0], "sinistra": self.x, "su": self.y, "giu": size[1]}
        else:
            self.image = image
            self.hit_box = sprite.hit_box(self.image, self.x, self.y, self.tolleranza)
        
        return self.image
    
    def on_click(self, x, y):
        cl = self.hit_box
        if x <  cl["destra"] and x > cl["sinistra"]:
            if y > cl['su'] and y < cl['giu']:
                return True

class sprite():
    def __init__(self, coords, path = ""):
        self.x = coords[0]
        self.y = coords[1]
        
        if path != "":
            self.image = pygame.image.load(path)
        else:
            self.image = pygame.Rect(self.x, self.y, 50, 50)
            self.width = 50
            self.height = 50
        
        return
    
    def __str__(self):
        return "a subclasses of pygame.sprite"
    
    def hit_box(self, img, x, y, tolleranza =0):
        dx = x +img.get_width() - tolleranza
        sx = x + tolleranza

        su = y + tolleranza + tolleranza
        giu = y + img.get_height() -tolleranza

        return {"destra": dx, "sinistra": sx, "su": su, "giu": giu}

class display():
    def __init__(self, background, size, FPS= -1):
        if FPS <0: 
            self.FPS = 50
        else:
            self.FPS = FPS
    
        self.screen= pygame.display.set_mode(size)
        if type(background) == type(""):
            self.background = sprite([0, 0], path=background)
        if type(background) == type(('r', 'g', 'b')):
            self.background = sprite([0, 0], path = background)
        return
        
    def update(self):
        pygame.display.update()
        pygame.time.Clock().tick(self.FPS)
        
        return