# Number Connect Game

This is a simple Number Connect Game built using Python and Pygame. The objective is to connect cells with the same value to merge them into a single cell with a doubled value.

## Features

- 5x6 grid of cells
- Randomly initialized cell values (2, 4, 8, 16, 32, 64)
- Merge cells by connecting them with a mouse drag
- New values are added to the top of the grid after a merge
- Custom colors for different cell values

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository or download the script file.

    ```bash
    git clone https://github.com/your-username/number-connect-game.git
    ```

2. Install Pygame if you haven't already.

    ```bash
    pip install pygame
    ```

## Usage

1. Navigate to the directory containing the script.

    ```bash
    cd number-connect-game
    ```

2. Run the script.

    ```bash
    python number_connect_game.py
    ```

3. The game window will open. Connect cells with the same value by clicking and dragging the mouse. Release the mouse button to merge the cells.

## Code Overview

### Constants

- `GRID_SIZE`: The number of rows and columns in the grid.
- `CELL_SIZE`: The size of each cell.
- `WINDOW_SIZE`: The size of the game window.
- `BACKGROUND_COLOR`: The background color of the game window.
- `TEXT_COLOR`: The color of the text in the cells.
- `FONT_SIZE`: The font size of the text in the cells.
- `LINE_COLOR`: The color of the line connecting cells.
- `LINE_WIDTH`: The width of the connecting line.

### Functions

- `get_cell_color(value)`: Returns the color corresponding to the cell value.
- `draw_grid(grid, path=None)`: Draws the grid and the path (if any) on the screen.
- `initialize_grid()`: Initializes the grid with random values.
- `merge_path(grid, path)`: Merges the cells along the given path.
- `get_path(start_pos, end_pos)`: Returns a list of positions from the start to the end position.

### Main Game Loop

- Initializes the grid.
- Handles user input for merging cells.
- Updates and redraws the grid after each merge.


## Feel free to customize this PYGAME to better suit your project's needs.
