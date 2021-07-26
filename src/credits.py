import utils
import __init__ as const

text =[
    "DEVELOPER: Marco Mazzeo",
    "GRAPHICS: Mia Masetti",
    "SOUNDS: Luca Pasqualetti & Cosimo Losurdo",
    "DOPPIAGGIO: Tiago Pisanti Vieira",
    "MAPPA ESPOLORAZIONE: Milo Binetti"
]

class credits():
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.text = text
        self.opened = False
        
        self.font = utils.pygame.font.SysFont("Arial", 11)
        self.height, self.width = self.make_Text(screen , self.font)
        
        return
    
    def make_Text(self, screen, font):
        x = self.x
        y = self.y
        h, w = 0, 0
        for i in range(len(text)):
            text_render = font.render(text[i], 1, (200, 242, 255))
            
            h += text_render.get_rect().height
            if w < text_render.get_rect().width:
                w = text_render.get_rect().width
                
        return h, w
        
    def open(self, screen):
        backstage = const.size
        x, y = self.x, self.y
        w, h = self.width, self.height       
        
        utils.pygame.draw.rect(screen, (33, 37, 43), (x, y, w, h))
        self.make_Text(screen, self.font, )

if __name__ == '__main__':
    screen = credits(const.display.screen, 20, 292)
    while True:
        for event in utils.pygame.event.get():
            if event.type == utils.pygame.QUIT:
                utils.pygame.quit()
            
        screen.open(const.display.screen)        
        const.display.update()