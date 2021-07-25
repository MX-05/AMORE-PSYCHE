import __init__ as const

class mixer():
    
    def __init__(self, status):
        self.status = status
        
        return
    
    def get_status():
        s = self.status
        if s:
            print ("AUDIO ON")
        else:
            print ("AUDIO OFF")
        
        return self.status