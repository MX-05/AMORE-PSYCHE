import __init__ as const

class mixer():
    
    def __init__(self, status):
        self.status = status
        
        return
    
    def change_status(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True
        
        return self.status
    
    def get_status(self):
        s = self.status
        if s:
            print ("\t AUDIO ON")
        else:
            print ("\t AUDIO OFF")
        
        return self.status
    
    def audio(self):
        return self.get_status()