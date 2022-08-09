from collections import deque

MAX_MEMORY = 100_000
BATCH_SIZE = 1_000
LR = 0.001

class Agent:
    def __init__(self):
        self.n_games = 0
        self.e = 0
        self.g = 0.88
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = None
        self.trainer = None

    def get_state(self, snake, food):
        pass

    def add_to_memory(self, state, action, reward, next, done):
        pass

    def train_long(self):
        pass

    def train_short(self):
        pass

    def get_actions(self, state):
        self.e = 80 - self.n_games
