import pygame
import sys
from settings import *
from engine import SnakeEngine

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Engine v1.0")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)
    
    game = SnakeEngine()

    while True:
        # 1. Event Handling (Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.direction != (0, GRID_SIZE):
                    game.direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and game.direction != (0, -GRID_SIZE):
                    game.direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and game.direction != (GRID_SIZE, 0):
                    game.direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and game.direction != (-GRID_SIZE, 0):
                    game.direction = (GRID_SIZE, 0)

        # 2. Update Engine
        game.update()

        # 3. Rendering (Drawing)
        screen.fill(COLOR_BG)
        
        # Draw Food
        pygame.draw.rect(screen, COLOR_FOOD, (game.food[0], game.food[1], GRID_SIZE-2, GRID_SIZE-2))
        
        # Draw Snake
        for segment in game.snake:
            pygame.draw.rect(screen, COLOR_SNAKE, (segment[0], segment[1], GRID_SIZE-2, GRID_SIZE-2))

        # Draw Score
        score_surface = font.render(f"Score: {game.score}", True, COLOR_TEXT)
        screen.blit(score_surface, (10, 10))

        if not game.is_running:
            # Simple Game Over overlay
            msg = font.render("GAME OVER - Press R to Restart", True, COLOR_FOOD)
            screen.blit(msg, (WIDTH//4, HEIGHT//2))
            
            # Check for restart
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game.reset()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()