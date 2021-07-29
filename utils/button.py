import pygame

class Button(pygame.sprite.Sprite):
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, pos, path = ""):
        super().__init__()
        self.pos = pos
        self.x, self.y = pos
        
        if path != "":
            self.image = pygame.image.load(path)
            self.rect = self.image.get_rect()
    
    # BUTTON WITH TEXT
        
    def B_text(self, text, font, bg= pygame.Color("white"), color = pygame.Color("black"), radius = 0):
        self.content = text
        self.font = pygame.font.SysFont(font[0], font[1])
        
        self.change_text(self.content, bg= bg, txt_color=color, radius=radius)
        return self
 
    def change_text(self, text, bg="white", txt_color = pygame.Color("black"), radius = 0):
        """Change the text whe you click"""
        self.content = text
        self.text = self.font.render(self.content, 1, txt_color)
        self.size = self.text.get_size()
        self.image = pygame.Surface(self.size)
        self.image.fill("white")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, bg, self.rect, border_radius=radius)
        self.rect.topleft = self.pos
        self.image.blit(self.text, (0, 0))
 
    # BUTTON REACTIONS
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True
                