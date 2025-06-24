# Travelling Flame Simulation

This project simulates a "travelling flame" on a 5x5 grid using Pygame. The flame moves along a predefined path, burning green cells, turning them to ash, and then allowing them to recover back to green after a delay. The simulation demonstrates a simple cellular automaton with wrap-around fire propagation on a specific row.

---

## Main Concepts

- **Grid States:**
  - `0`: Empty (white)
  - `1`: Relaxed/Green (can burn)
  - `2`: Ash/Gray (recently burned, recovering)
  - `3`: Burning/Red (currently on fire)

- **Ash Recovery:**  
  Burned cells (ash) recover to green after a set number of steps.

- **Special Rule:**  
  On row 3, the fire wraps around from the last to the first column and vice versa, creating a continuous loop.

---

## Code Structure

### 1. Initialization

- **Grid Setup:**  
  Creates a 5x5 grid, initializing all cells to empty (`0`).  
  Sets up the initial "green" path and the ash timer grid.

- **Colors:**  
  Defines RGB color codes for each cell state.

- **Initial State:**  
  Sets up the green path and initializes the fire and ash on row 3.

### 2. Simulation Logic

#### `step_fire(grid, ash_timer)`

Handles one simulation step:
- Finds green cells adjacent to burning cells (including wrap-around on row 3).
- Updates burning cells to ash and starts their recovery timer.
- Turns eligible green cells to burning.
- Handles ash recovery to green after the timer expires.

### 3. Pygame Visualization

- **`draw_grid(grid, screen)`:**  
  Draws the grid on the Pygame window, coloring each cell according to its state.

- **Main Loop:**  
  Handles Pygame events, updates the simulation each second, and redraws the grid.

---

## How It Works

1. The simulation starts with a predefined green path and a burning cell at the start of row 3.
2. Each step:
   - The fire spreads to adjacent green cells (including wrap-around on row 3).
   - Burning cells become ash and start a recovery timer.
   - Ash cells recover to green after the timer.
3. The process repeats, creating a continuous travelling flame effect.

---

## Key Parameters

- `grid_size`: Size of the grid (5x5).
- `ASH_RECOVERY_DELAY`: Number of steps a cell remains ash before recovering.

---

## Usage

- Run the script:  
  ```
  python travelling_flame.py
  ```
- A Pygame window will display the grid and animate the travelling flame.
- Close the window to stop the simulation.

---

## Example Visualization

- **White:** Empty cell
- **Green:** Ready to burn
- **Red:** Burning
- **Gray:** Recently burned, recovering
