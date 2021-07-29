import pygame

class Button(pygame.sprite.Sprite):
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, pos, path = ""):
        super().__init__()
        self.x, self.y = pos
        
        if path != "":
            self.image = pygame.image.load(path)
            self.rect = self.image.get_rect()
    
    # BUTTON WITH TEXT
        
    def text(self, text, font, bg= pygame.Color("white"), color = pygame.Color("black")):
        self.content = text
        self.font = pygame.font.SysFont(font[0], font[1])
        
        self.change_text(self.content, bg= bg, txt_color=color)
        return
 
    def change_text(self, text, bg="white", txt_color = pygame.Color("black")):
        """Change the text whe you click"""
        self.content = text
        self.text = self.font.render(self.content, 1, txt_color)
        self.size = self.text.get_size()
        self.image = pygame.Surface(self.size)
        self.image.fill(bg)
        self.image.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    # BUTTON REACTIONS
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True