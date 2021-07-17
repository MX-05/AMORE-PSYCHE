
class button():
    def __str__(self):
        return "a subclasses of pygame.image"

    def __init__(self, coords, image, tolleranza = 0):
        self.image = image
        
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.tolleranza = tolleranza
    
        self.hit_box = self.hit_box(self.image, self.x, self.y, self.tolleranza)
    
    def on_click(self, x, y):
        cl = self.hit_box
        if x <  cl["destra"] and x > cl["sinistra"]:
            if y > cl['su'] and y < cl['giu']:
                return True
            
    def hit_box(self, img, x, y, tolleranza =0):
        dx = x +img.get_width() - tolleranza
        sx = x + tolleranza

        su = y + tolleranza + tolleranza
        giu = y + img.get_height() -tolleranza

        return {"destra": dx, "sinistra": sx, "su": su, "giu": giu}
