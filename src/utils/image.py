import pygame

class sprite():
    def __init__(self, coords, width = 50, height = 50, path = ""):
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        
        if path != "":
            self.image = pygame.image.load(path)
        if path == "":
            self.image = pygame.Rect(self.x, self.y, width, height)
            self.width = width
            self.height = height
            
            self.color = (241, 197, 49)
        
        return
    
    def __str__(self):
        return "a subclasses of pygame.sprite"
    
    def draw(self, screen):
        if type(self.image) != type(pygame.Rect):
            screen.blit(self.image, self.coords)
        else:
            pygame.draw.rect(screen, self.color, self.image)
            
        return
    
    def hit_box(self, tolleranza =0):
        
        
        if type(self.image) == type(pygame.Rect(self.x, self.y, 50, 50)):
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

