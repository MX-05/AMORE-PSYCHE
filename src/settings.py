import utils.image as util
import pygame

# FIXME: sistemare lo scambio di variabili nell'__init__.py
size = [720, 480]

class menu():
    def __init__(self):
        
        self.play = {
            "playing": False,
            "button": util.button((20, 20))
        }
        self.play["button"].make(content="Play")        
        
        self.audio = util.button((20, 80))
        self.audio.make(content="Audio")      
        
        self.credits = util.button((20, 140))
        self.credits.make(content="Credits")
        
        self.skin = util.button((
            20 + self.credits.image.width + 20,     # X
            140                                     # Y
        ))
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