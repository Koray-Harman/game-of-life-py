import random

## generate new grid with specified dimensions
def grid_maker(grid_cells, grid_row):
    grid = []
    cell_value = False
    for _x in range(grid_row):
        row = []
        for _y in range(grid_cells):
            row.append(cell_value)
        grid.append(row)
    return grid


class Gameoflife:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = grid_maker(x, y)
        self.new_grid = []
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    # check if x value is within grid boundary
    def is_valid_x(self, n):
        return (n >= 0) and (n < self.width)

    # check if y value is within grid boundary
    def is_valid_y(self, n):
        return (n >= 0) and (n < self.height)

    # check if given cell is alive
    def is_alive(self, x, y):
        if (self.is_valid_x(x)) and (self.is_valid_y(y)):
            return self.grid[y][x]
        #else:
        #    return False

    # count living neighbours for cell
    def count_live_neighbours(self, x, y):
        current_y = y - 1
        end_x = x + 1
        end_y = y + 1
        livecount = 0
        while current_y <= end_y:
            current_x = x - 1
            while current_x <= end_x:
                if not(current_y == y and current_x == x):
                    if self.is_alive(current_x, current_y):
                        livecount += 1
                current_x += 1
            current_y += 1
        return livecount


    # define next generation grid
    def next_generation(self):
        self.grid = self.new_grid

    # print grid array with borders
    def glossy_grid(self):
        width = len(self.grid[0])
        if width == 0:
            print('error')
            return
        print('+', ('-' * width), '+', sep='')
        for row in self.grid:
            print('|', end="")
            for cell in row:
                if cell is False:
                    print('X', end="")
                elif cell is True:
                    print('O', end="")
            print('|')
        print('+', ('-' * width), '+', sep='')

    # overide specific cell value within grid
    def set_cell(self, x, y, value=True):
        self.grid[y][x] = value

    # overide all cell values with specific value within grid
    def set_all_values(self, value=True):
        for row_index in range(len(self.grid)):
            row = self.grid[row_index]
            row_length = len(row)
            for cell_index in range(row_length):
                x = cell_index
                y = row_index
                self.set_cell(x, y, value)

    # overide all cell values with random True/False value
    def randomise_all_values(self):
        for row_index in range(len(self.grid)):
            row = self.grid[row_index]
            row_length = len(row)
            for cell_index in range(row_length):
                value = random.choice([True, False])
                x = cell_index
                y = row_index
                self.set_cell(x, y, value)

#    OLD VERSION OF COUNT count living neighbour cells
#    def count_alive_neighbours(self, x, y):
#        livingCells = 0
#        gridheight = len(self.grid)
#        gridwidth = len(self.grid[y])
#        #neighbours above selected cell
#        if y - 1 >= 0:
#            if x - 1 >= 0:
#                if self.grid[y - 1][x - 1] == True:
#                    livingCells += 1
#            if self.grid[y - 1][x] == True:
#                livingCells += 1
#            if x + 1 < gridwidth:
#                if self.grid[y - 1][x + 1] == True:
#                    livingCells += 1
#        #neighbours either side of selected cell
#        if x - 1 >= 0:
#            if self.grid[y][x - 1] == True:
#                    livingCells += 1
#        if x + 1 < gridwidth:
#            if self.grid[y][x + 1] == True:
#                    livingCells += 1
#        #neighbours underneath selected cell
#        if y + 1 < gridheight:
#            if x - 1 >= 0:
#                if self.grid[y + 1][x - 1] == True:
#                    livingCells += 1
#            if self.grid[y + 1][x] == True:
#                livingCells += 1
#            if x + 1 < gridwidth:
#                if self.grid[y + 1][x + 1] == True:
#                    livingCells += 1
#        return(livingCells)

    # convert grid to array of living neighbour count
    def iterate_living_neighbours(self):
        next_grid = []
        for row_index in range(len(self.grid)):
            row = self.grid[row_index]
            next_row = []
            for cell_index in range(len(row)):
                x = cell_index
                y = row_index
                next_row.append(self.count_live_neighbours(x, y))
            next_grid.append(next_row)
        print(next_grid)
        return next_grid

    # generate new grid state based on GoL rules
    def gol_next_grid(self):
        next_grid = []
        #for iteration in range(iterations):
        for row_index in range(len(self.grid)):
            row = self.grid[row_index]
            next_row = []
            for cell_index in range(len(row)):
                x = cell_index
                y = row_index
                live_neighbour = self.count_live_neighbours(x, y)
                if self.grid[y][x] is True:
                    if live_neighbour < 2:
                        next_row.append(False)
                    elif live_neighbour >= 2 and live_neighbour <= 3:
                        next_row.append(True)
                    elif live_neighbour > 3:
                        next_row.append(False)
                    else:
                        next_row.append(True)
                if self.grid[y][x] is False:
                    if live_neighbour == 3:
                        next_row.append(True)
                    else:
                        next_row.append(False)
            next_grid.append(next_row)
        self.new_grid = next_grid
        return next_grid

    # iteraite the generation of next grid state
    def new_grid_iterations(self, iterations):
        self.grid = self.gol_next_grid()
        self.glossy_grid()
        for _iteration in range(iterations):
            self.grid = self.gol_next_grid()
            self.glossy_grid()
            final_grid = self.grid
        return final_grid


    # generate next grid and replace default grid - runs gol_next_grid() and next_generation()
    def gol_transition_grid(self):
        self.gol_next_grid()
        self.next_generation()



#TESTGAME = Gameoflife(20, 20)
#TESTGAME.set_cell(3, 5, false)
#TESTGAME.set_all_values(True)
#TESTGAME.glossy_grid()
#TESTGAME.count_alive_neighbours(2, 2)
#TESTGAME.glossy_grid()
#TESTGAME.randomise_all_values()
#TESTGAME.glossy_grid()
#TESTGAME.gol_next_grid()
#TESTGAME.next_generation()
#TESTGAME.glossy_grid()
