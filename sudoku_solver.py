# the cell class
## value (initialize with value as 0)
## enter_value()


# the board class
class Board():
## init(9x9 list of lists)
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
                    if self.get_value(x, y) == 0:
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
