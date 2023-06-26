# Mine Sweeper

This is a Python function that takes a grid of `#` and `-`, where each hash (`#`) represents a mine and each dash (`-`) represents a mine-free spot. The function returns a new grid, where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).

## Getting Started

To use this function, you need to have Python installed on your system. The code provided is compatible with Python 3.

1. Copy the code from the code block or download the code file.
2. Open your preferred Python editor or IDE.
3. Create a new Python file or open an existing one.
4. Paste the code into the Python file.

## Usage

The function `count_mine` takes a grid as input and returns a new grid with the counts of adjacent mines. Here's an example of how to use the function:

```python
grid = [["-", "-", "#", "-"],
        ["#", "#", "-", "-"],
        ["-", "-", "=", "#"],
        ["-", "#", "-", "#"]] 

mine_sweeper = count_mine(grid)

for row in mine_sweeper:
    print(row)
```
Running the above code will output the grid with the counts of adjacent mines:

```

[['1', '2', '#', '3'],
 ['#', '#', '3', '4'],
 ['1', '2', '=', '#'],
 ['2', '#', '4', '#']]
```
The output grid contains digits indicating the number of mines adjacent to each spot. The original mine positions (#) remain unchanged.

# How It Works
The count_mine function iterates over each cell in the input grid and counts the number of adjacent mines. It uses nested loops to check the eight adjacent cells around each spot. The function avoids going out of bounds by checking the boundaries of the grid. The adjacent mine counts are then added to a new grid, which is returned as the output.

Contributing
Contributions are welcome! If you find any issues with the code or have suggestions for improvements, please feel free to open an issue or submit a pull request.

Acknowledgments
The code was developed to solve a classic problem, Minesweeper, by counting adjacent mines. The algorithm used in the function is a common approach to solving this problem.
