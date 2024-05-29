import pygame, sys
from perlin import *

class Main:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2D Perlin Noise")
        self.screen = pygame.display.get_surface()
        self.scale = 100

        self.perlin = Perlin2D(self.width / self.scale, self.height / self.scale)
    
    def update(self):
        self.screen.fill((255, 255, 255))
        self.render(3)
        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    def render(self, res):
        for x in range(0, self.width, res):
            for y in range(0, self.height, res):
                color = self.perlin.get(x / self.scale, y / self.scale)
                color = self.map(color, -1, 1, 0, 255)
                pygame.draw.rect(self.screen, (color, color, color), (x, y, res, res))
    
    def map(self, n, min1, max1, min2, max2):
        return ((n - min1) / (max1 - min1)) * (max2 - min2) + min2
                

if __name__ == '__main__':
    main = Main()
    main.update()