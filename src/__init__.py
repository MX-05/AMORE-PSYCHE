import pygame

from src.utils.image import *
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
display = pygame.display.set_mode([720, 480])

pygame.mixer.init()