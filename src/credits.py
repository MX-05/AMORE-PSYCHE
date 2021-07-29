import utils, sys
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
            screen.blit(text_render, (self.x, self.y+ h))
            
            h += text_render.get_rect().height
            if w < text_render.get_rect().width:
                w = text_render.get_rect().width
        
        line = const.pygame.Rect(self.x, self.y + h, w, 2)
        draw_line = const.pygame.draw.rect(screen, (255,255,255), line)
        line.move(self.x, self.y+ h)
                
        return h, w
        
    def open(self, screen):
        backstage = const.size
        x, y = self.x, self.y
        w, h = self.width, self.height       
        
        utils.pygame.draw.rect(screen, (33, 37, 43), (x, y, w, h))
        
        self.make_Text(screen, self.font, )
        

if __name__ == '__main__':
    screen = credits(const.display.screen, 0, const.size[1])
    animation = True
    while True:
        
        if screen.y >= 292:
            screen.y -=1
            print(screen.y)
            
            screen.open(const.display.screen)
            const.display.update()        
                
            
        for event in utils.pygame.event.get():
            if event.type == utils.pygame.QUIT:
                utils.pygame.quit()
                sys.exit()
        
        const.display.update()