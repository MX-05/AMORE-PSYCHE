import utils.image as util
import pygame

# FIXME: sistemare lo scambio di variabili nell'__init__.py
size = [720, 480]

class menu():
    def __init__(self):
        self.buttons = []
        
        self.play = {
            "playing": False,
            "button": util.button((20, 20))
        }
        self.play["button"].make()
        self.play["button"].text_setting["content"] = "Play"
        
        self.buttons.append(self.play["button"])
        
        self.audio = util.button((20, 80))
        self.audio.make()
        self.audio.text_setting["content"] = "Audio"
        
        self.buttons.append(self.audio)
        
        self.credits = util.button((20, 140))
        self.credits.make()
        self.credits.text_setting["content"] = "Credits"
        
        self.buttons.append(self.credits)
        
        self.skin = util.button((
            20 + self.credits.image.width + 20,     # X
            140                                      # Y
        ))
        self.skin.make()
        self.skin.text_setting["content"] = "Skin"
        
        self.buttons.append(self.skin)
        
        return
    
    def open(self):
        screen = util.display((225, 225, 225), size)
        while True:
            for i in self.buttons:
                i.draw(screen.screen)
            
            for event in pygame.event.get():
                # FIXME: fare chiudere il processo quando clicco la x della finestra 
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
                        print("\t [v] pulsante crediti cliccato")
            screen.update()
        
        return
    
setting = menu()
setting.open()