import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 3
NUM_BOMBS = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

# Function to place bombs randomly
def place_bombs():
    bombs = []
    for _ in range(NUM_BOMBS):
        bomb_x = random.randint(0, GRID_SIZE - 1)
        bomb_y = random.randint(0, GRID_SIZE - 1)
        bombs.append((bomb_x, bomb_y))
    return bombs

# Main game loop
def main():
    bombs = place_bombs()
    print("Bombs:", bombs)

    running = True
    while running:
        screen.fill(WHITE)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse click
                x, y = pygame.mouse.get_pos()
                cell_x = x // CELL_SIZE
                cell_y = y // CELL_SIZE
                print("Clicked cell:", cell_x, cell_y)

                # Check if the clicked cell contains a bomb
                if (cell_x, cell_y) in bombs:
                    print("Game over!")
                    running = False

        pygame.display.flip()

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
