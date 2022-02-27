import pygame 
import numpy as np 

pygame.init() 
window = pygame.display.set_mode((700,700))
pygame.display.set_caption("Sudoku") #changes window name
white = (255,255,255) #colors defined in RGB format
black = (0,0,0)
red = (255,0,0)
grey = (107,107,107)

class Board:
    def __init__(self, initial_values):
        """Initializes the board with the given initial values.
        INPUTS:
            initial_values - Not sure what Smita will use so will adjust accordingly - using just a list for now
            (list values from left to right top to bottom, leaving blanks as a space for now?)
        """
        
        self.initial_values = initial_values

    def create_board():
        '''
        creates the 9x9 sudoku board to play on based on the initial values of the initialized board
        '''
        #create a board using initial values in pygame

        square_size = 65
        list_of_positions = [] #list storing the positions of all of the rectangles to input numbers into later
        for i in range(1, 10): #since 9 boxes needed
            for j in range(1,10):
                pygame.draw.rect(window, grey, (i*square_size, j*square_size, square_size, square_size), 2)
                rectangle_position = [i*square_size, j*square_size]
                list_of_positions.append(rectangle_position)

        for i in range(0,3): #making larger squares to add the border effect
            i += 1/3 #gross way to make it match up
            for j in range(0,3): 
                j += 1/3
                pygame.draw.rect(window, white, (i*square_size*3, j*square_size*3, square_size*3, square_size*3), 2)
        pygame.display.update()
        return(list_of_positions)

    def update_board(): 
        #change board values for empty squares depending on user input 
        pass

    def solve_board():
        #run the final code solver function and take the output to populate this board
        pass

    def clear_board():
        #either this or delete board and create a new one? 
        pass
board1 = Board
board1.create_board()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()