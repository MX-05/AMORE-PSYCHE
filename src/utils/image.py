import pygame

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
            print( "\tASSE | button | text\n")
            print(f"\t  X  | {self.x}{(6-len(str(self.x)))*' '}| {XcoordT}\n")
            print(f"\t  Y  | {self.y}{(6-len(str(self.y)))*' '}| {YcoordT}\n")

class sprite():
    def __init__(self, coords, width = 50, height = 50, path = ""):
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        
        if path != "":
            self.image = pygame.image.load(path)
        else:
            self.image = pygame.Rect(self.x, self.y, 50, 50)
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