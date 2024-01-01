import os
from grid import game_grid
import time
import sys


def clear_screen():
    os.system("clear") 

# Print menu
def upper_menu():
    print(" _____________________________")
    print("|                             |")
    print("|         PEEK-A-BOO          |")
    print("|_____________________________|")
    print()
    
def main_menu():
    print("1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New game")
    print("5. Exit\n")

# To get the coordinates of the matrix
def indices(inp):
    m = ord(inp[0])-ord('A')
    l = int(inp[1:])
    return l, m

# to check if the input entered is valid input or not
def valid_input(inp):
    # if len(inp) != 2:
    #     return False
    if not inp[0].isalpha() or not inp[1:].isdigit():
        return False
    return True

# To check if the coordinate entered belongs to the grid or not
def v_c(grid_size, grid, l, m):
    if m < 0 or m >= int(grid_size):
        print("Input error: column entry is out of range for this grid. Please try again.")
        print()
        return False
    elif l < 0 or l >= int(grid_size):
        print("Input error: row entry is out of range for this grid. Please try again.")
        print()
        return False
    return True

def get_input(grid, grid_size):
    while True:
        element = input("Enter cell coordinates (e.g., a0): ").upper()

        if valid_input(element):
            l, m = indices(element)
            break
        else:
            print("\nEnter coordinate correctly\n")

    while not v_c(grid_size, grid, l, m):
        element = get_input(grid, grid_size)
        l, m = indices(element)
    return element

# To uncover two elements        
def select_elements(grid, grid_size):
    while True:
        element1 = get_input(grid, grid_size)
        element2 = get_input(grid, grid_size)
        l1, m1 = indices(element1)
        l2, m2 = indices(element2)
        
        while l1 == l2 and m1 == m2:
            print("\nYou entered same coordinates twice.Enter coordinates for 2nd element again\n")
            element2 = get_input(grid, grid_size)
            l2, m2 = indices(element2)


        if v_c(grid_size, grid, l1, m1) and v_c(grid_size, grid, l2, m2):
            break


    num1 = grid.get_value(l1, m1)
    num2 = grid.get_value(l2, m2)
        
    if num1 == num2:
        grid.reveal(l1, m1)
        grid.reveal(l2, m2)
    else:
        value1 = grid.get_grid_value(l1,m1)
        value2 = grid.get_grid_value(l2, m2)
        clear_screen()
        grid.reveal(l1, m1)
        grid.reveal(l2, m2)
        upper_menu()
        grid.view()
        main_menu()
        print("\nSelect: ")
        time.sleep(2)
        if value1 == "X":
            grid.unreveal(l1, m1)
        if value2 == "X":
            grid.unreveal(l2, m2)
    grid.add_guesses()

# To permanently uncover two elements
def uncover_element(grid, grid_size):
    
    while True:

        element = get_input(grid,grid_size)
        l, m = indices(element)

        if v_c(grid_size, grid, l, m):
            l, m = indices(element)
            break

    grid.reveal(l, m)
    grid.add_guesses()
    grid.add_guesses()
    grid.uncover_element_guesses(l, m)


# Game was completed
def game_completed():
    print()
    input("Grid has been completely revealed you can only enter option 4 or 5. Press enter to continue")

# Function to play game
def play_game(grid_size):
    
    grid = game_grid(grid_size)
    grid.fill_matrix()
    reveal_all = False
    while True:
        clear_screen()
        upper_menu()
        grid.view()
        if grid.x_counter() == 0 and reveal_all == False:
            score = grid.calculate_score()
            print(score)
            print()
        main_menu()
        selection = input("Select: ")

        if selection == "1":
            if grid.x_counter() != 0:
                select_elements(grid, grid_size)
            else:
                game_completed()

        elif selection == "2":
            if grid.x_counter() != 0:
                uncover_element(grid, grid_size)
            else:
                game_completed()

        elif selection == "3":
            if grid.x_counter() != 0:
                grid.uncover_all()
                reveal_all = True
            else:
                game_completed()

        elif selection == "4":
            play_game(grid_size)
        
        elif selection == "5":
            exit()
        
        else:
            input("You have selected an invalid option. Press Enter to continue and then enter the option again.")
        clear_screen()

# To check if the grid size entered is valid or not
def valid_grid_size(grid_size):
    if grid_size == 2 or grid_size == 4 or grid_size == 6:
        return True
    return False

# Exit if the grid size is invalid
def input_grid_size(grid_size):
    if not valid_grid_size(grid_size):
        print("You entered an invalid grid size. The size of grid can only be 2 or 4 or 6.")
        exit()

def main():
    grid_size = int(sys.argv[1])
    input_grid_size(grid_size)
    play_game(grid_size)

if __name__ == "__main__":
    main()
