import pygame

class Button(pygame.sprite.Sprite):
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font, bg="white", feedback="", txt_color = pygame.Color("black")):
        super().__init__()
        self.content = text
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg, txt_color)
 
    def change_text(self, text, bg="white", txt_color = pygame.Color("black")):
        """Change the text whe you click"""
        self.content = text
        self.text = self.font.render(self.content, 1, txt_color)
        self.size = self.text.get_size()
        self.image = pygame.Surface(self.size)
        self.image.fill(bg)
        self.image.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self):
        # screen.blit(self.image, (self.x, self.y))
        self.rect.center = [self.x, self.y]
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True