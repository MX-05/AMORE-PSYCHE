import utils as util
import __init__ as const

import pygame

size = const.size

class menu():
    def __init__(self):
        
        self.play = {
            "playing": False,
            "button": util.button((20, 20), font_color=(40, 44, 52))
        }
        self.play["button"].make(content="Play")        
        
        self.audio = util.button((20, 80), font_color=(40, 44, 52))
        self.audio.make(content="Audio")      
        
        self.credits = util.button((20, 140), font_color=(40, 44, 52))
        self.credits.make(content="Credits")
        
        self.skin = util.button((
            20 + self.credits.image.width + 20,     # X
            140                                    # Y
        ),  font_color=(40, 44, 52)
        )
        self.skin.make(content="Skin")      
        
        
        return
    
    def open(self):
        screen = util.display((225, 225, 225), size)
        while True:
            for i in self.__dict__.items():
                try:
                    i[1]["button"].draw(screen.screen)
                except:
                    i[1].draw(screen.screen)
            
            screen.debug(mode=["hit-box", self.audio.image])
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # FIXME: fixare la hit_box dei pulsanti 
                    screen.debug(x, y)
                    
                    if self.play["button"].on_click(x, y):
                        self.play["playing"] = True
                        print("\t [v] PUlsanre Play cliccato")
                        return
                    
                    if self.audio.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe mixer 
                        print(self.audio.get_coords())
                        print("\t [v] pulsante audio cliccato")
                    
                    if self.credits.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe credits 
                        print("\t [v] pulsante crediti cliccato")
                    
                    if self.skin.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe skin 
                        print("\t [v] pulsante crediti cliccato")
            screen.update()
        
        return
    
setting = menu()
setting.open()