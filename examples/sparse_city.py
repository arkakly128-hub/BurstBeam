import random

class SparseCity:
    def __init__(self, seed=42):
        random.seed(seed)
        self.X, self.Y, self.Z = 100, 100, 30

        # Initialize empty grid
        self.grid = [[[0 for z in range(self.Z)] for y in range(self.Y)] for x in range(self.X)]

        # Random buildings
        for _ in range(1200):
            x, y, z = random.randint(0, self.X - 1), random.randint(0, self.Y - 1), random.randint(0, self.Z - 1)
            self.grid[x][y][z] = 1

        # Dynamic obstacles (e.g., birds)
        self.dynamic = set()
        for _ in range(8000):
            x, y, z = random.randint(0, self.X - 1), random.randint(0, self.Y - 1), random.randint(0, self.Z - 1)
            self.dynamic.add((x, y, z))

        self.start = (0, 0, 0)
        self.goal = (99, 99, 29)
