import utils
import __init__ as const

text = """
    DEVELOPER: Marco Mazzeo
    GRAPHICS: Mia Masetti
    SOUNDS: Luca Pasqualetti & Cosimo Losurdo
    DOPPIAGGIO: Tiago Pisanti Vieira
    MAPPA ESPOLORAZIONE: Milo Binetti
"""

class credits():
    def __init__(self):
        self.text = text
        self.opened = False
        
    def open(self, screen, x, y):
        backstage = const.size
        
        window = utils.button((x, backstage[1]), text)
        self.window = window
        for i in range(backstage[1], y):
            window.y = i
            window.draw(screen)
