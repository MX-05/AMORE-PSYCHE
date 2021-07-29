import utils as util
import __init__ as const

import pygame

size = const.size
screen = const.display

class menu():
    def __init__(self):
        
        # ----------- PLAY BTN --------
        
        self.play = {
            "playing": False,
            "button": util.button((20, 20), "  Play  ")
        }
        
        # ----------- AUDIO BTN --------
        
        self.audio = {
            "status": const.mixer(True),
            "button": util.button((20, 80), "  Audio  "),
        }
        self.audio["status coords"] = ( 
                20 + self.audio["button"].image.width + 20,
                80
            )
        
        # ----------- AUDIO STATUS --------
        
        if self.audio["status"]:
            self.status = util.button(self.audio["status coords"], " on ")
        else:
            self.status = util.button(self.audio["status coords"], " off ")
        
        # ----------- CREDITS BTN --------
        
        self.credits = {
            "button": util.button((5, size[1] - 30), "  Credits  "),
            "clicked": False
        }
        
        # ----------- SKIN BTN --------
        
        self.skin = util.button((455, 282),  "  Skin  ")
        
        return
    
    def main_menu(self):
        while True:
            
            # ---------- DRAW BTN ------    ------
            
            for i in self.__dict__.items():
                try:
                    i[1]["button"].draw(screen.screen)
                except:
                    i[1].draw(screen.screen)
            
            # ---------- EVENTS --------------
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    
                    # ----------- PLAY ------------
                    
                    if self.play["button"].on_click(x, y):
                        self.play["playing"] = True
                        # TODO: mettere la funzione play per avviare i dialoghi 
                        print("\t [v] PUlsanre Play cliccato")
                        return
                    
                    # ----------- PLAY ------------
                    
                    if self.audio["button"].on_click(x, y):
                        
                        if self.audio["status"].change_status() == True:
                            self.status = util.button(self.audio["status coords"], " on ")
                        else:
                            self.status = util.button(self.audio["status coords"], " off ")
                    
                    if self.credits["button"].on_click(x, y):
                        if self.credits["clicked"] == True:
                            
                            self.credits["button"].y = size[1] - 30
                            self.credits["clicked"] = False
                            
                            print(self.credits["button"].y)
                        
                        else:
                            self.credits["button"].y = size[1] - 200
                            self.credits["clicked"] = True
                            
                        print("\t [v] pulsante crediti cliccato")
                    
                    if self.skin.on_click(x, y):
                        # TODO: aggiungere le opzioni della classe skin 
                        print("\t [v] pulsante skin cliccato")
            screen.update()
        
        return
    
if __name__ == "__main__":
    setting = menu()
    setting.main_menu()