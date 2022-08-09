import pygame
from config import CELL_SIZE


class Score:
    def __init__(self, color, font='arial', size=20, hiscore=0):
        self.font = pygame.font.SysFont(font, size)
        self.color = color
        self.score = 0
        self.hiscore = hiscore
        self.is_visible = True
        self._update_surface()

    def _update_surface(self):
        self.surface = self.font.render(f'Score: {self.score}', True, self.color)
        self.rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
        self.surface2 = self.font.render(f'Hiscore: {self.hiscore}', True, self.color)
        self.rect2 = pygame.Rect(0, 20, CELL_SIZE, CELL_SIZE)

    def update(self, window:pygame.Surface):
        if not self.is_visible:
            return
        window.blit(self.surface, self.rect)
        window.blit(self.surface2, self.rect2)

    def add_score(self, score:int):
        self.score += score
        if self.score > self.hiscore:
            self.hiscore = self.score
        self._update_surface()
