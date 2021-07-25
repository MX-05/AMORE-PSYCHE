import pygame
from utils.image import sprite

class button():

    def __init__(
        self, 
        coords, 
        font = "Arial", 
        font_size = 25, 
        font_color = (225, 225, 225),
        text_distance = 5,
        tolleranza = 0
    ):
        
        pygame.font.init()
        
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.tolleranza = tolleranza
        
        self.text_setting = {
            "font": pygame.font.SysFont(font, font_size),
            "font color": font_color,
            "distance": text_distance,
            "content": "",
            "coords": []
        }
        for i in coords:
            self.text_setting["coords"].append(i + text_distance)
    
        return
    
    def make(self, size = [], content= "button", colour = (241, 197, 49), image = ""):
        self.colour = colour
        if size == []:
            width = self.text_setting["font"].get_linesize() + self.text_setting["distance"]
            height = self.text_setting["font"].get_height() + self.text_setting["distance"]
            size.append(width)
            size.append(height)
        
        if image == "" or image.lower() =="rect": # RECTANGLE
            self.image = sprite((self.x, self.y), width = size[0], height= size[1])
            self.hit_box = self.image.hit_box()
            self.text_setting["content"] = content 
        else:
            self.image = sprite(self.coords, path= image)
            self.hit_box = self.image.hit_box(self.tolleranza)
        
        return self.image
    
    def draw(self, screen):
        if type(self.image.image) == type(pygame.Rect(3, 3, 3, 3)):
            pygame.draw.rect(screen, self.colour, self.image.image)
            screen.blit(
                self.text_setting["font"].render(
                    self.text_setting["content"], 
                    True, 
                    self.text_setting["font color"]
                ), 
                self.text_setting["coords"]
            )
        else:
            screen.blit(self.image, self.coords)
                
        return
    
    def on_click(self, x, y):
        cl = self.hit_box
        if x <  cl["destra"] and x > cl["sinistra"]:
            if y > cl['su'] and y < cl['giu']:
                return True
    
    def get_coords(self):
        XcoordT = self.text_setting["coords"][0]
        YcoordT = self.text_setting["coords"][1]
        
        if len(str(self.x)) <=6 or len(str(self.y))<=6:
            print( "\tASSE | button | text")
            print(f"\t  X  | {self.x}{(6-len(str(self.x)))*' '}| {XcoordT}")
            print(f"\t  Y  | {self.y}{(6-len(str(self.y)))*' '}| {YcoordT}")