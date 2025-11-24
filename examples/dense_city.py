import random

class DenseCity:
    def __init__(self, seed=42):
        random.seed(seed)
        self.X, self.Y, self.Z = 50, 50, 20
        self.grid = [[[0 for z in range(self.Z)] for y in range(self.Y)] for x in range(self.X)]
        for x in range(self.X):
            for y in range(self.Y):
                for z in range(self.Z):
                    if random.random() < 0.38:
                        self.grid[x][y][z] = 1
        self.start = (0, 0, 0)
        self.goal = (49, 49, 19)
