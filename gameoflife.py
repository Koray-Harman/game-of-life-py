import random

## generate new grid with specified dimensions
def grid_maker(grid_cells, grid_rows):
    grid = []
    cell_value = False
    for _x in range(grid_rows):
        row = []
        for _y in range(grid_cells):
            row.append(cell_value)
        grid.append(row)
    return grid


class Gameoflife:

    def __init__(self, cells_x, rows_y):
        self.grid = grid_maker(cells_x, rows_y)
        self.new_grid = []
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    # check if cells_x value is within grid boundary
    def is_valid_x(self, cells_x):
        return (cells_x >= 0) and (cells_x < self.width)

    # check if rows_y value is within grid boundary
    def is_valid_y(self, rows_y):
        return (rows_y >= 0) and (rows_y < self.height)

    # check if given cell is alive
    def is_alive(self, cells_x, rows_y):
        if (self.is_valid_x(cells_x)) and (self.is_valid_y(rows_y)):
            return self.grid[rows_y][cells_x]
        #else:
        #    return False

    # count living neighbours for cell
    def count_live_neighbours(self, cells_x, rows_y):
        current_y = rows_y - 1
        end_x = cells_x + 1
        end_y = rows_y + 1
        livecount = 0
        while current_y <= end_y:
            current_x = cells_x - 1
            while current_x <= end_x:
                if not(current_y == rows_y and current_x == cells_x):
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
    def set_cell(self, cells_x, rows_y, value=True):
        self.grid[rows_y][cells_x] = value

    # overide all cell values with specific value within grid
    def set_all_values(self, value=True):
        for row_index in range(len(self.grid)):
            row = self.grid[row_index]
            row_length = len(row)
            for cell_index in range(row_length):
                cells_x = cell_index
                rows_y = row_index
                self.set_cell(cells_x, rows_y, value)

    # overide all cell values with random True/False value
    def randomise_all_values(self):
        for row_index in range(len(self.grid)):
            row = self.grid[row_index]
            row_length = len(row)
            for cell_index in range(row_length):
                value = random.choice([True, False])
                cells_x = cell_index
                rows_y = row_index
                self.set_cell(cells_x, rows_y, value)

#    OLD VERSION OF COUNT count living neighbour cells
#    def count_alive_neighbours(self, cells_x, rows_y):
#        livingCells = 0
#        gridheight = len(self.grid)
#        gridwidth = len(self.grid[rows_y])
#        #neighbours above selected cell
#        if rows_y - 1 >= 0:
#            if cells_x - 1 >= 0:
#                if self.grid[rows_y - 1][cells_x - 1] == True:
#                    livingCells += 1
#            if self.grid[rows_y - 1][cells_x] == True:
#                livingCells += 1
#            if cells_x + 1 < gridwidth:
#                if self.grid[rows_y - 1][cells_x + 1] == True:
#                    livingCells += 1
#        #neighbours either side of selected cell
#        if cells_x - 1 >= 0:
#            if self.grid[rows_y][cells_x - 1] == True:
#                    livingCells += 1
#        if cells_x + 1 < gridwidth:
#            if self.grid[rows_y][cells_x + 1] == True:
#                    livingCells += 1
#        #neighbours underneath selected cell
#        if rows_y + 1 < gridheight:
#            if cells_x - 1 >= 0:
#                if self.grid[rows_y + 1][cells_x - 1] == True:
#                    livingCells += 1
#            if self.grid[rows_y + 1][cells_x] == True:
#                livingCells += 1
#            if cells_x + 1 < gridwidth:
#                if self.grid[rows_y + 1][cells_x + 1] == True:
#                    livingCells += 1
#        return(livingCells)

    # convert grid to array of living neighbour count
    def iterate_living_neighbours(self):
        next_grid = []
        for row_index in range(len(self.grid)):
            row = self.grid[row_index]
            next_row = []
            for cell_index in range(len(row)):
                cells_x = cell_index
                rows_y = row_index
                next_row.append(self.count_live_neighbours(cells_x, rows_y))
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
                cells_x = cell_index
                rows_y = row_index
                live_neighbour = self.count_live_neighbours(cells_x, rows_y)
                if self.grid[rows_y][cells_x] is True:
                    if live_neighbour < 2:
                        next_row.append(False)
                    elif live_neighbour >= 2 and live_neighbour <= 3:
                        next_row.append(True)
                    elif live_neighbour > 3:
                        next_row.append(False)
                    else:
                        next_row.append(True)
                if self.grid[rows_y][cells_x] is False:
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
