import utils as util
import __init__ as const

import pygame

size = const.size
screen = const.display

class menu():
    def __init__(self):
        
        self.play = {
            "playing": False,
            "button": util.button((20, 20), " Play ")
        }
        
        self.audio = util.button((20, 80), " Audio ")
        
        self.credits = util.button((20, 140), " Credits ")
        
        self.skin = util.button((
            20 + self.credits.image.width + 20,     # X
            140                                    # Y
        ),  " Skin ")
        
        return
    
    def open(self):
        while True:
            for i in self.__dict__.items():
                try:
                    i[1]["button"].draw(screen.screen)
                except:
                    i[1].draw(screen.screen)
            
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    
                    if self.play["button"].on_click(x, y):
                        self.play["playing"] = True
                        print("\t [v] PUlsanre Play cliccato")
                        return
                    
                    if self.audio.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe mixer 
                        print("\t [v] pulsante audio cliccato")
                    
                    if self.credits.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe credits 
                        print("\t [v] pulsante crediti cliccato")
                    
                    if self.skin.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe skin 
                        print("\t [v] pulsante skin cliccato")
            screen.update()
        
        return
    
setting = menu()
setting.open()