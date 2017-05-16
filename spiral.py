def print_spiral(size):
    """Print a spiral on a matrix that is the given size across, decreases
    in size as it loops around and includes a column or row or empty spaces
    in between each spiral.
    """

    # Build Grid
    grid = []

    for i in range(size):
        grid.append(list(' ' * size))
    original_size = size
    coord = (0, 0)

    while size:
        # Create rows of x's to the right
        for i in range(size):
            grid[coord[0]][coord[1] + i] = 'x'
        coord = (coord[0] + 1, coord[1] + size - 1)
        size = size - 1

        # Create column of x's down
        if size > 0:
            for i in range(size):
                grid[coord[0] + i][coord[1]] = 'x'
            size = size - 1
            coord = (coord[0] + size, coord[1]-1)

        # Create row of x's to the left
        if size > 0:
            for i in range(size):
                grid[coord[0]][coord[1] - i] = 'x'
            size = size - 1
            coord = (coord[0] - 1, coord[1] - size)

        # Create column of x's up
        if size > 0:
            for i in range(size):
                grid[coord[0] - i][coord[1]] = 'x'
            size = size - 1
            coord = (coord[0] - size, coord[1] + 1)

    # Print grid with spiral
    for i in range(original_size):
        print grid[i]


print_spiral(6)
print_spiral(7)
print_spiral(10)
print_spiral(12)
