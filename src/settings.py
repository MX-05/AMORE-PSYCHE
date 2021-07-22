import utils.image as util
import pygame

class menu():
    def __init__(self):
        self.buttons = []
        self.play = {
            "playing": False,
            "button": util.button((20, 20))
        }
        self.play.make()
        self.buttons.append(self.play)
        
        self.audio = util.button((20, 30))
        self.audio.make()
        self.buttons.append(self.audio)
        
        self.credits = util.button((20, 40))
        self.credits.make()
        self.buttons.append(self.credits)
        
        self.skin = util.button((
            20 + self.credits.image.width + 20,     # X
            40                                      # Y
        ))
        self.skin.make()
        self.buttons.append(self.skin)
        
        return
    
    def open(self):
        screen = util.display((225, 225, 225), size)
        while True:
            for i in self.buttons:
                i.draw()
            
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    
                    if self.play["button"].on_click(x, y):
                        self.play["playing"] = True
                        return
                    
                    if self.audio.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe mixer 
                        print("\t [v] pulsante audio cliccato")
                    
                    if self.credits.on_click():
                        # TODO: aggiungere le opzioni della classe credits 
                        print("\t [v] pulsante crediti cliccato")
                    
                    if self.skin.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe skin 
                        print("\t [v] pulsante crediti cliccato")
        
        return