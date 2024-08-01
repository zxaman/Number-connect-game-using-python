import pygame
import random
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = (5, 6)  # 5 rows x 6 columns
CELL_SIZE = 60  # Size of each cell (make sure it's a square)
WINDOW_SIZE = (CELL_SIZE * GRID_SIZE[1], CELL_SIZE * GRID_SIZE[0])
BACKGROUND_COLOR = (187, 173, 160)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 20
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 5

# Custom colors for each number
def get_cell_color(value):
    colors = {
        2: (238, 228, 218), 4: (237, 224, 200), 8: (242, 177, 121),
        16: (245, 149, 99), 32: (246, 124, 95), 64: (246, 94, 59),
        128: (237, 207, 114), 256: (237, 204, 97), 512: (237, 200, 80),
        1024: (237, 197, 63), 2048: (237, 194, 46)
    }
    return colors.get(value, (205, 193, 180))

# Set up display
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Number Connect Game')

# Font
font = pygame.font.SysFont(None, FONT_SIZE)

def draw_grid(grid, path=None):
    screen.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE[0]):
        for col in range(GRID_SIZE[1]):
            value = grid[row][col]
            color = get_cell_color(value)
            pygame.draw.rect(screen, color,
                             pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if value:
                text = font.render(f"{value:,}", True, TEXT_COLOR)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)
    
    # Draw path if exists
    if path:
        for start, end in zip(path, path[1:]):
            pygame.draw.line(screen, LINE_COLOR, 
                             (start[1] * CELL_SIZE + CELL_SIZE // 2, start[0] * CELL_SIZE + CELL_SIZE // 2),
                             (end[1] * CELL_SIZE + CELL_SIZE // 2, end[0] * CELL_SIZE + CELL_SIZE // 2),
                             LINE_WIDTH)
    
    pygame.display.update()

def initialize_grid():
    grid = [[random.choice([2, 4, 8, 16, 32, 64]) for _ in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]
    return grid

def merge_path(grid, path):
    if len(path) < 2:
        return
    
    value = grid[path[0][0]][path[0][1]]
    for pos in path:
        if grid[pos[0]][pos[1]] != value:
            return  # Path contains different values, so no merge
    
    for pos in path[:-1]:
        grid[pos[0]][pos[1]] = 0
    grid[path[-1][0]][path[-1][1]] = value * 2

    # Apply gravity
    for col in range(GRID_SIZE[1]):
        new_col = [grid[row][col] for row in range(GRID_SIZE[0]) if grid[row][col] != 0]
        new_col = [0] * (GRID_SIZE[0] - len(new_col)) + new_col
        for row in range(GRID_SIZE[0]):
            grid[row][col] = new_col[row]

    # Add new numbers at the top
    for row in range(GRID_SIZE[0]):
        for col in range(GRID_SIZE[1]):
            if grid[row][col] == 0:
                grid[row][col] = random.choice([2, 4, 8, 16, 32, 64])

def get_path(start_pos, end_pos):
    path = []
    r, c = start_pos
    end_r, end_c = end_pos
    while (r, c) != (end_r, end_c):
        path.append((r, c))
        if end_r < r:
            r -= 1
        elif end_r > r:
            r += 1
        if end_c < c:
            c -= 1
        elif end_c > c:
            c += 1
    path.append((end_r, end_c))
    return path

def main():
    grid = initialize_grid()
    draw_grid(grid)
    dragging = False
    start_pos = None
    path = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    start_pos = (event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE)
                    dragging = True
                    path = [start_pos]
                    
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    if start_pos:
                        end_pos = (event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE)
                        path = get_path(start_pos, end_pos)
                        merge_path(grid, path)
                        draw_grid(grid)
                        dragging = False
                        start_pos = None
                        path = []
            
            elif event.type == MOUSEMOTION:
                if dragging:
                    end_pos = (event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE)
                    path = get_path(start_pos, end_pos)
                    draw_grid(grid, path)
        
        pygame.display.update()

if __name__ == "__main__":
    main()
