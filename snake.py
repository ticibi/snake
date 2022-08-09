from collections import deque
from tkinter.tix import CELL
import pygame
from config import CELL_SIZE
from random import randint


class Snake:
    '''snake class'''
    def __init__(self, pos):
        self.direction = 'up'
        self.head = pos
        self.body = deque([
            self.head,
            (pos[0], pos[1] + CELL_SIZE)
        ])

    def update(self, window):
        for i, b in enumerate(self.body):
            g_value = randint(1, 255)
            color = pygame.Color(0, g_value, 0)
            rect = pygame.Rect(
                b[0],
                b[1],
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(
                window,
                color,
                rect,
            )
        self.move()

    def move(self):
        x, y = self.head[0], self.head[1]
        match self.direction:
            case 'up':
                y -= CELL_SIZE
            case 'down':
                y += CELL_SIZE
            case 'left':
                x -= CELL_SIZE
            case 'right':
                x += CELL_SIZE
        self.body[0] = (x, y)
        self.head = self.body[0]
        self.body.rotate(1)
        
    def grow_body(self):
        self.body.append(self.body[-1])
