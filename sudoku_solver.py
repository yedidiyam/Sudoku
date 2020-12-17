# the cell class
class Cell:

    def cross (A,B):
        '''nifty string comprehension that combines two elements and
        i'm not entirely sure this ever actually gets used,
        but i wanted to contribute because im bored'''
        return [a+b for a in A for b in B]

    def __init__(self, row, col, value=0):
        '''Creates a cell object, containing information on the row, column,
        and value. Calculates the grid based on row and column.'''
        self.value=value
        self.row=row
        self.col=col
        # if self.row <= 2 and self.col <= 2:
        #     grid = 0
        # elif (self.row > 2 and self.row <= 5) and self.col <= 2:
        #     grid = 1
        # elif (self.row > 5 and self.row <= 8) and self.col <= 2:
        #     grid = 2
        # elif (self.row <= 2) and self.col > 2 and (self.col <= 5):
        #     grid = 3
        # elif (self.row > 2 and self.row <= 5) and (self.col > 2 and self.col <= 5):
        #     grid = 4
        # elif (self.row > 5 and self.row <= 8) and (self.col > 2 and self.col <= 5):
        #     grid = 5
        # elif (self.row <= 2) and self.col > 5 and (self.col <= 8):
        #     grid = 6
        # elif (self.row > 2 and self.row <= 5) and (self.col > 5 and self.col <= 8):
        #     grid = 7
        # elif (self.row > 5 and self.row <= 8) and (self.col > 5 and self.col <= 8):
        #     grid = 8
        # self.grid=grid

    #returns value of row, column, and grid attributes in that order
    def __str__(self):
        '''Returns the value of the cell object as a string.'''
        return str(self.value)

    def get_position(self):
        '''Returns row, column, and grid position of the Cell object.'''
        return self.row, self.col, self.grid

    def enter_value(self,value):
        '''Sets value of sudoku cell. Does not return anything.'''
        self.value=value

# the board class
class Board():

    def __init__(self):
        self.board = [[Cell(i, j) for j in range(9)] for i in range(9)]

    #initial setup of puzzle
    def create_puzzle(self, number_dict):
        ''' Accepts a dictionary with 'row, column' as keys and the value for the specific
        cell as value. eg. {'0,0': 4, '1,5': 9} '''
        for key, value in number_dict.items():
            row = int(key.split(',')[0])
            column = int(key.split(',')[1])

            self.board[row][column].enter_value(value)

    ## print_board()
    def print_board(self):
        '''Prints the values of all 81 cells in a pretty, visually pleasing and
        comprehensible format. '''
        print('\n')
        print('\n  -----------------------------------')
        # uses self.board to refer to list of list that represents the grid
        for row in self.board:
            print(' |', end=' ')
            for column in row:
                print(str(column), end=' | ')
            print('\n  -----------------------------------')
        print('\n')
        return ''

    ## is_full()
    def is_full(self):
        '''Checks if the board is full or not. Returns true if it is full and
        false if it is not full.'''
        for x in range(9):
            for y in range (9):
                if self.board[x][y].value == 0:
                    return False
        # if there is atleast one zero in the board it returns false
        return True

## find_possibilities()
    def find_row(self, row, possibilities):
        '''Checks the board and identifies set entities in each row to see which
        box in each row is already filled.'''
        for i in range(9):
            if self.board[row][i].value != 0:
                possibilities[self.board[row][i].value] = 1

    def find_column(self, column, possibilities):
        '''Checks board and identifies set entities in each column to see which
        box in each column is already filled. '''
        for i in range(9):
            if self.board[i][column].value != 0:
                possibilities[self.board[i][column].value] = 1

    def get_grid_value(self, val):
        '''Returns which grid the position of the value is in.'''
        if val < 3:
            return 0
        elif val >= 3 and val < 6:
            return 3
        else:
            return 6

    def find_grid(self, row, column, possibilities):
        '''Checks the board and identifies set entities in each grid to see which grid has already been completed. '''
        g_row = self.get_grid_value(row)
        g_column = self.get_grid_value(column)

        for i in range(g_row, g_row + 3):
            for j in range(g_column, g_column + 3):
                if self.board[i][j].value != 0:
                    possibilities[self.board[i][j].value] = 1

    def find_possibilities(self, row, column):
        ''' '''
        possibilities = {}
        for i in range(1, 10):
            possibilities[i] = 0

        self.find_row(row, possibilities)
        self.find_column(column, possibilities)
        self.find_grid(row, column, possibilities)

        for i in range(1, 10):
            if possibilities[i] == 0:
                possibilities[i] = i
            else:
                possibilities[i] = 0

        return possibilities


    def solve(self):
        '''Solves the puzzle. If the board is full, it prints the board and quits.
        Finds possible values for a given cell based on its position - employs
        backtracking and shit - somebody else write this pls'''
        # initialize variables to be used to identify empty cell
        row = 0
        column = 0

        # check if grid is full
        # if it is, print the board and exit
        if self.is_full():
            print('The puzzle has been solved successfully!')
            # print the board if solved completely
            self.print_board()
            # returning nothing exits the program
            return
        else:
            for x in range(9):
                for y in range(9):
                    if self.board[x][y].value == 0:
                        row = x
                        column = y
                        break

        # find the possible entries for the specific cell
        possible_entries = self.find_possibilities(row, column)

        # main controller
        for i in range(1, 10):
            if possible_entries[i] != 0:
                self.board[row][column].value = possible_entries[i]

                # recursive call and backtracking
                # enables the computer to try out the possible solutions
                # until the correct solution is found
                self.solve()
        # backtrack
        # if no solution is found, the cell is emptied and
        # other possibilities are explored
        self.board[row][column].value = 0

b = Board()
b.create_puzzle({'0,0':7, '0,1':9, '0,6':3,
                '1,5':6, '1,6':9,
                '2,0':8, '2,4':3, '2,7':7, '2,8':6,
                '3,5':5, '3,8':2,
                '4,2':5, '4,3':4, '4,4':1, '4,5':8, '4,6':7,
                '5,0':4, '5,3':7,
                '6,0':6, '6,1':1, '6,4': 9, '6,8':8,
                '7,2':2, '7,3':3,
                '8,2':9, '8,7':5, '8,8':4})
b.print_board()
b.solve()
