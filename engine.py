import random
from settings import WIDTH, HEIGHT, GRID_SIZE

class SnakeEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        # Snake body is a list of coordinates. Index 0 is the head.
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = (GRID_SIZE, 0) # Moving Right initially
        self.food = self._place_food()
        self.score = 0
        self.is_running = True

    def _place_food(self):
        """Standard randomization within the grid constraints."""
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return (x, y)

    def update(self):
        if not self.is_running:
            return

        # Calculate new head position
        new_head = (self.snake[0][0] + self.direction[0], 
                    self.snake[0][1] + self.direction[1])

        # 1. Collision Check: Walls
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.is_running = False
            return

        # 2. Collision Check: Self
        if new_head in self.snake:
            self.is_running = False
            return

        self.snake.insert(0, new_head)

        # 3. Food Check
        if new_head == self.food:
            self.score += 1
            self.food = self._place_food()
        else:
            self.snake.pop() # Remove tail if no food eaten