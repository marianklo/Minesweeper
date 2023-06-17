# Create a function that takes a grid of # and -, where each hash (#) represents a
# mine and each dash (-) represents a mine-free spot.
# Return a grid, where each dash is replaced by a digit, indicating the number of
# mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally).

grid = [["-", "-", "#", "-"],
        ["#", "#", "-", "-"],
        ["-", "-", "=", "#"],
        ["-", "#", "-", "#"]] 

def count_mine(grid):
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    # Create empty list to store output grid
    result = []
    
    # Loop through each row in the grid
    for row in range(rows):
        # Create a new list to represent new row
        new_row = []
        # Loop through each column in the row
        for col in range(cols):
            # If the cell is mine then add to the result
            if grid[row][col] == "#":
                new_row.append("#")
            # Otherwise count the adjacent mines
            else:
                count = 0
                # Check all 8 adjacent cels
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        # Make sure we do not go out of bounds
                        if 0 <= row+i < rows and 0 <= col+j < cols:
                            # If the adjacent cell is mine, increment count
                            if grid[row+i][col+j] == "#":
                                count +=1
                # Append the count as a string
                new_row.append(str(count))
        # Append the current roe to result
        result.append(new_row)
    # Return result
    return result

# Print output  
mine_sweeper = (count_mine(grid))
for row in mine_sweeper:
    print(row)




