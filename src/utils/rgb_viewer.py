import pygame

def get_color(color):
    rgb = color.split(',')
    rgb[0] = rgb[0].replace('(', '')
    rgb[1] = rgb[1].strip()
    rgb[2] = rgb[2].strip().replace(')', '')
    
    return rgb
        
    
def get_rgb(rgb):
    red = int(rgb[0])
    green = int(rgb[1])
    blue = int(rgb[2])
    
    return red, green, blue

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        pygame.display.update()
        
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode([100, 100])
    rgb = get_color(str(input("Insert color in rgb: ")))
    screen.fill((get_rgb(rgb)))
    
    main()