import pygame

# Size of the grid (5x5)
grid_size = 5

# Main grid: stores the state of each cell
# 0 = empty, 1 = green (relaxed), 2 = ash (recovering), 3 = burning
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Timer grid: tracks how long each cell should remain as ash
ash_timer = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # Timer for ash recovery

# Color mapping for each state
colors = {
    0: (255, 255, 255),  # Empty (white)
    1: (0, 255, 0),      # Green/relaxed (green)
    2: (128, 128, 128),  # Ash (gray)
    3: (255, 0, 0)       # Burning (red)
}

# Set up the initial green (relaxed) path on the grid
grid[3][0] = 1
grid[3][1] = 1
grid[3][2] = 1
grid[3][3] = 1
grid[3][4] = 1

grid[0][1] = 1
grid[1][1] = 1
grid[2][1] = 1

grid[0][3] = 1
grid[1][3] = 1
grid[2][3] = 1

# Number of steps a cell remains as ash before recovering to green
ASH_RECOVERY_DELAY = 2  # steps to stay as ash

def step_fire(grid, ash_timer):
    """
    Advances the simulation by one step:
    - Finds green cells adjacent to burning cells and marks them to burn.
    - Updates burning cells to ash and starts their recovery timer.
    - Recovers ash cells to green after their timer expires.
    """
    to_burn = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                burning_neighbor = False
                # Check standard neighbors (up, down, left, right)
                if (row > 0 and grid[row-1][col] == 3) or \
                   (row < len(grid)-1 and grid[row+1][col] == 3) or \
                   (col > 0 and grid[row][col-1] == 3) or \
                   (col < len(grid[row])-1 and grid[row][col+1] == 3):
                    burning_neighbor = True
                # Special wrap-around for row 3 (fire loops horizontally)
                if row == 3:
                    if col == 0 and grid[3][4] == 3:
                        burning_neighbor = True
                    if col == 4 and grid[3][0] == 3:
                        burning_neighbor = True
                if burning_neighbor:
                    to_burn.append((row, col))
    # Update grid: burning -> ash, green to be burned -> burning
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 3:
                grid[row][col] = 2  # burning -> ash
                ash_timer[row][col] = ASH_RECOVERY_DELAY  # set timer
    for row, col in to_burn:
        grid[row][col] = 3  # green -> burning

    # Ash recovers to green after timer runs out
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 2 and ash_timer[row][col] > 0:
                ash_timer[row][col] -= 1
                if ash_timer[row][col] == 0:
                    grid[row][col] = 1  # ash -> green

# --- Pygame setup and visualization ---

pygame.init()
window_size = 650
screen = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()

def draw_grid(grid, screen):
    """
    Draws the current state of the grid to the Pygame window.
    Each cell is colored according to its state.
    """
    cell_size = window_size // len(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            pygame.draw.rect(screen, colors[grid[row][col]], 
                             (col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)

running = True

# Set up infinite fire loop on row 3
for col in range(grid_size):
    grid[3][col] = 1  # green (relaxed)

grid[3][0] = 3  # fire (burning)
grid[3][1] = 2  # ash (grey)
ash_timer[3][1] = ASH_RECOVERY_DELAY  # set ash timer for the ash cell

# --- Main simulation loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    step_fire(grid, ash_timer)  # Advance the simulation by one step

    screen.fill((0, 0, 0))
    draw_grid(grid, screen)
    pygame.display.flip()
    clock.tick(1)  # 1 step per second

pygame.quit()