import pygame

from utils import *
"""
TODO: scrivere tutte le classi

classes: button(), image(), display().
button():
    - image = pygame.image
    - coords = [int x, int y]
    - tolleranza = int
    - hit_box = {
        "destra": int, 
        "sinistra": int, 
        "su": int,
        "giu": int
    }
    
    + make(size = [int width, int height], colour = (int r, int g, int b), image = "path")
"""

pygame.init()
size = [720, 480]
display = display((40, 44, 52), size)

pygame.mixer.init()