import random

class game_grid:

    # Constructor
    def __init__(self, grid_size):
        self.grid_size = int(grid_size)
        self.matrix = []
        for r in range(self.grid_size):
            rs = ["X"] * self.grid_size
            self.matrix.append(rs)
        self.matrix_pairs = []
        for i in range(self.grid_size):
            ro = [0] * self.grid_size
            self.matrix_pairs.append(ro)
        self.uncover_matrix = []
        for j in range(self.grid_size):
            row = [False] * self.grid_size
            self.uncover_matrix.append(row)
        self.num_guesses = 0
        self.cheated = False
    
    # Get value at the l, m coordinate from the grid
    def get_value(self, l, m):
        return self.matrix_pairs[l][m]

    # Get value from the revealed grid
    def get_grid_value(self, l, m):
        return self.matrix[l][m]
    
    # Fill matrix with random numbers
    def fill_matrix(self):
        num = (self.grid_size ** 2)//2
        numbers_list = list(range(num))*2
        random.shuffle(numbers_list)
        
        for l in range(self.grid_size):
            for m in range(self.grid_size):
                ind = l * self.grid_size + m
                self.matrix_pairs[l][m] = numbers_list[ind]

    # Reveal element at l, m coordinates
    def reveal(self, l, m):
        self.matrix[l][m] = self.matrix_pairs[l][m]

    # Print the grid
    def view(self):
        print("\t", end = '')
        for i in range(self.grid_size):
            print("[", chr(i + 65),']\t', end='')
        print('\n\n')
        for l in range(self.grid_size):
            print("[", l, ']\t', end = '')
            for m in range (self.grid_size):
                print(" ",self.matrix[l][m], end = ' \t')            
            print('\n\n')
    
    # Unreveal a particular element
    def unreveal(self, l, m):
        self.matrix[l][m] = "X"
        
    # Count the number of "X"s in the revealed grid
    def x_counter(self):
        counter = 0
        for l in range(self.grid_size):
            for m in range(self.grid_size):
                if self.matrix[l][m] == "X":
                    counter += 1
        return counter

    # Uncover the grid completely
    def uncover_all(self):
        for l in range(self.grid_size):
            for m in range(self.grid_size):
                self.reveal(l,m)

   # Increment the number of guesses
    def add_guesses(self):
        self.num_guesses += 1

    # Modify the value of the uncover matrix for a particular matrix if uncovered by option 2
    def uncover_element_guesses(self, l, m):
        self.uncover_matrix[l] [m] = True

    # Calculate score
    def calculate_score(self):
        counter = 0
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.uncover_matrix[i][j] == True:
                    counter += 1
        if counter == self.grid_size ** 2 :
            return "You cheated - Loser!. Your score is 0!"           
        else:
            minimum_possible_guesses = (self.grid_size ** 2) // 2
            return "Oh Happy Day. You've won!! Your score is: " + str(((minimum_possible_guesses) / self.num_guesses) * 100)
