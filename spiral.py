def print_spiral(size):
    """Prints a spiral of a given size"""

    grid = []

    # Build Grid
    for i in range(size):
        grid.append(list(' ' * size))

    # Top row of xs
    for i in range(size):
        grid[0][i] = "x"

    # Bottom row of xs
    for i in range(1, size):
        grid[i][size - 1] = "x"
        grid[size - 1][i] = "x"

    # First column up
    for i in range(2, size):
        grid[i][1] = "x"

    # Second row to right
    for i in range(2, size - 2):
        grid[2][i] = "x"

    # Last column down
    for i in range(3, size - 2):
        grid[i][size-3] = "x"

    # Second row to right
    for i in range(3, size - 2):
        grid[2][i] = "x"

    # Last column down
    for i in range(3, size - 2):
        grid[i][size-3] = "x"

    for i in range(size):
        print grid[i]
    print len(grid)

print_spiral(12)
print_spiral(7)
print_spiral(8)





    # for i in range(len(grid)):
    #     for j in range(len(grid)):
    #         if i == 0:
    #             grid[i][j] = 'x'
    #         if i == (size - 1):
    #             grid[i][j] = 'x'
    #         if j == (size - 1):
    #             grid[i][j] = 'x'


    # def create_xs(size, start_index=0):
    #     for i in range(size):
    #         grid[start_index][i] = "x"

    #     start_index += 1
    #     # Bottom row of xs
    #     for i in range(start_index, size):
    #         grid[i][size - 1] = "x"
    #         grid[size - 1][i] = "x"

    #     start_index += 1
    #     # First column up
    #     for i in range(start_index, size):
    #         grid[i][start_index - 1] = "x"

     # create_xs(size - 2, start_index=2)


# start at (0, 0)
# go right size # of spaces
# go down size -2 number of spaces
# go left size -3 number of spaces
# go up size -4 number of spaces
# go right size - 5 number of spaces

# current = grid[x][y]
# for i in range(size):

# def add_xs_across(x, y):
#     for i in range(size):
#         grid[x][y+i] = 'x'

# def add_xs_down(x, y):
#     for i in range(size-1)
#         grid[]

