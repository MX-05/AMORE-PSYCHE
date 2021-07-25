import pygame
from utils.image import sprite

init_font_setting = {
    "content": "button",
    "name": "Arial",
    "size": 25,
    "color": (243, 195, 44)
}

class button():

    def __init__(self, coords, text, path = "", color = (100, 100, 100), font = init_font_setting, tolleranza = 0):
        
        pygame.font.init()
        
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.tolleranza = tolleranza
        
        font["content"] = text
        self.font_settings = font
        self.font = pygame.font.SysFont(font["name"], font["size"])
        self.text_render = self.font.render(font["content"], 1, font["color"])
        
        self.make(image = path)
        self.color = color
    
        return
    
    def make(self, image = ""):
        
        if image == "" or image.lower() =="rect": # RECTANGLE
            x, y, w, h = self.text_render.get_rect()
            x, y = self.coords
            
            self.image = pygame.Rect(x, y, w, h)
            self.hit_box = {
                "destra": x+ w,
                "sinistra": x, 
                "su": y, 
                "giu": y+h
            }
            
        else:
            self.image = sprite(self.coords, path= image)
            self.hit_box = self.image.hit_box(self.tolleranza)
        
        return self.image
    
    def draw(self, screen):
        if type(self.image) == type(pygame.Rect(3, 3, 3, 3)):
            pygame.draw.rect(screen, self.color, self.image)
            screen.blit(self.text_render, (self.x, self.y))
        else:
            screen.blit(self.image, self.coords)
                
        return
    
    def on_click(self, x, y):
        cl = self.hit_box
        if x <  cl["destra"] and x > cl["sinistra"]:
            if y > cl['su'] and y < cl['giu']:
                return True
    
    def get_coords(self):
        XcoordT = self.hit_box["sinistra"]
        YcoordT = self.hit_box["su"]
        
        if len(str(self.x)) <=6 or len(str(self.y))<=6:
            print( "\tASSE | button | text")
            print(f"\t  X  | {self.x}{(6-len(str(self.x)))*' '}| {XcoordT}")
            print(f"\t  Y  | {self.y}{(6-len(str(self.y)))*' '}| {YcoordT}")