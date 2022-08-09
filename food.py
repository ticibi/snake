import pygame
import random
from config import WIDTH, HEIGHT, CELL_SIZE


class Food:
    '''food class'''
    def __init__(self, color):
        self.color = color
        self.pos = self.reposition()

    def reposition(self):
        x = random.randrange(0, (WIDTH - CELL_SIZE), CELL_SIZE)
        y = random.randrange(0, (HEIGHT - CELL_SIZE), CELL_SIZE)
        self.pos = (x, y)
        return (x, y)

    def update(self, window):
        rect = pygame.Rect(
            self.pos[0],
            self.pos[1],
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(
           window,
            self.color,
            rect,
        )
