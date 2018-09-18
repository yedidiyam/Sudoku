# the cell class
class Cell:
    def __init__(self, row, col, value=0):
        self.value=value
        self.row=row
        self.col=col
        if self.row <= 2 and self.col <= 2:
            grid = 0
        elif (self.row > 2 and self.row <= 5) and self.col <= 2:
            grid = 1
        elif (self.row > 5 and self.row <= 8) and self.col <= 2:
            grid = 2
        elif (self.row <= 2) and self.col > 2 and (self.col <= 5):
            grid = 3
        elif (self.row > 2 and self.row <= 5) and (self.col > 2 and self.col <= 5):
            grid = 4
        elif (self.row > 5 and self.row <= 8) and (self.col > 2 and self.col <= 5):
            grid = 5
        elif (self.row <= 2) and self.col > 5 and (self.col <= 8):
            grid = 6
        elif (self.row > 2 and self.row <= 5) and (self.col > 5 and self.col <= 8):
            grid = 7
        elif (self.row > 5 and self.row <= 8) and (self.col > 5 and self.col <= 8):
            grid = 8
        self.grid=grid
    #gotta be a more efficient way to do this lol^^^
    #returns value of row, column, and grid attributes in that order
    def get_position(self):
        return self.row, self.col, self.grid
    #sets the value of the sudoku cell
    def enter_value(self,value):
        self.value=value


# the board class
class Board():
## init(9x9 list of lists)

    # initial setup
    def create_puzzle(self, number_dict):
        # accepts a dictionary with row,column as keys and the value for that cell as value
        # eg. {'0,0': 4, '1,5': 9}
        for key, value in number_dict.items():
            row = int(key.split(',')[0])
            column = int(key.split(',')[1])

            self.board[row][column].enter_value(value)

    ## print_board()
    def print_board(self):
        print('\n')
        print('\n  -----------------------------------')
        # used self.board to refer to list of list that represents the grid
        for row in self.board:
            print(' |', end=' ')
            for column in row:
                print(str(column), end=' | ')
            print('\n  -----------------------------------')
        print('\n')
        return ''

    ## is_full()
    def is_full(board):
        for x in range(9):
            for y in range (9):
                if board[x][y] == 0:
                    return False
                return True

## get_value() # return a specific value based on row and column indices
## enter_value(row, column, value) # enter a value into a specific cell by calling the enter_value() method on the cell object
## find_possibilities()
    ## solve()
    def solve(self):
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
                self.enter_value(row, column, possible_entries[i])

                # recursive call and backtracking
                # enables the computer to try out the possible solutions
                # until the correct solution is found
                self.solve(self)
        # backtrack
        # if no solution is found, the cell is emptied and
        # other possibilities are explored
        self.enter_value(row, column, 0)

b = Board()
b.print_board()
