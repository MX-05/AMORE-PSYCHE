import utils.image as util

def menu():
    def __init__(self):
        self.play = {
            playing: False,
            button: util.button((20, 20))
        }
        self.play.make()
        
        self.audio = util.button((20, 30))
        self.audio.make()
        
        self.credits = util.button((20, 40))
        self.credits.make()
        
        self.skin = util.button((
            20 + self.credits.image.width + 20,     # X
            40                                      # Y
        ))
        self.skin.make()
        
        return