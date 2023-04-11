import pygame
import numpy as np

#pygame設定環節
pygame.init()
width, height = 500, 500
WINDOW_SIZE = (width, height)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("簡易細胞動態模擬程式 v1.0 alpha")

# 可以色色與設網格
BLACK = (0,38, 111)
WHITE = (255, 255, 255)
size = 5
gw, gh = width // size, height // size

# 細胞狀態隨機初始化
grid = np.random.randint(2, size=(gw, gh))

#細胞規則
def evolve(state, neighbors):
    alive_neighbors = np.sum(neighbors)
    if state == 1:
        if alive_neighbors < 2 or alive_neighbors > 3:
            return 0
        else:
            return 1
    else:
        if alive_neighbors == 3:
            return 1
        else:
            return 0

#動作函數
def evolve_grid(grid):
    new_grid = np.zeros_like(grid)
    for i in range(gw):
        for j in range(gh):
            neighbors = grid[(i-1):(i+2), (j-1):(j+2)]
            neighbors_sum = np.sum(neighbors) - grid[i, j]
            new_grid[i, j] = evolve(grid[i, j], neighbors_sum)
    return new_grid

#純顯示
def draw_grid(grid):
    screen.fill(BLACK)
    for i in range(gw):
        for j in range(gh):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (i*size, j*size, size, size))

while True:
    #開搞
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           # sys.exit()

    # Evolve the grid and redraw it
    grid = evolve_grid(grid)
    draw_grid(grid)
    pygame.display.flip()
