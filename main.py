import pygame
from time import sleep
from food import Food
from snake import Snake
from score import Score
from config import WIDTH, HEIGHT, CELL_SIZE, Colors


pygame.init()
pygame.display.set_caption("Python Snake ML")
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
fps = 10


class SnakeML:
    def __init__(self):
        self.running = True
        self.snake = Snake(pos=(WIDTH // 2, HEIGHT // 2))
        self.food = Food(color=Colors.RED)
        self.score = Score(color=Colors.WHITE, font='Arial', size=20)
        self.hiscore = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameover()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameover()

                if event.key == pygame.K_UP or \
                    event.key == pygame.K_w:
                    self.snake.direction = 'up'

                elif event.key == pygame.K_DOWN or \
                    event.key == pygame.K_s:
                    self.snake.direction = 'down'

                elif event.key == pygame.K_LEFT or \
                    event.key == pygame.K_a:
                    self.snake.direction = 'left'

                elif event.key == pygame.K_RIGHT or \
                    event.key == pygame.K_d:
                    self.snake.direction = 'right'

                if event.key == pygame.K_e:
                    self.food.reposition()

                if event.key == pygame.K_r:
                    self.reset()

    def update(self, window):
        self.snake.update(window)
        self.food.update(window)
        self.score.update(window)

    def process(self):
        # snake runs into food
        if self.snake.head == self.food.pos:
            self.score.add_score(1)
            self.food.reposition()
            self.snake.grow_body()
        # snake runs into x bounds
        if self.snake.head[0] < 0 or self.snake.head[0] > WIDTH - CELL_SIZE:
            self.gameover()
        # snake runs into y bounds
        if self.snake.head[1] < 0 or self.snake.head[1] > HEIGHT - CELL_SIZE:
            self.gameover()
        # snake runs into itself
        #if self.snake.head in list(self.snake.body)[2:]:
        #    self.gameover()

    def run(self, window):
        while self.running:
            window.fill(Colors.BLACK)
            self.process()
            self.handle_events()
            self.update(window)
            pygame.display.update()
            clock.tick(fps)
            
    def gameover(self):
        self.reset()
        return
        self.running = False
        sleep(5)
        pygame.quit()
        quit()

    def reset(self):
        self.hiscore = self.score.hiscore
        self.running = True
        self.snake = Snake(pos=(WIDTH // 2, HEIGHT // 2))
        self.food = Food(color=Colors.RED)
        self.score = Score(color=Colors.WHITE, hiscore=self.hiscore)


if __name__ == '__main__':
    app = SnakeML()
    app.run(window)
