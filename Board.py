import pygame 
import numpy as np 

pygame.init() 
window = pygame.display.set_mode((700,700))
pygame.display.set_caption("Sudoku") #changes window name
font = pygame.font.SysFont('Arial', 50) #font and size
white = (255,255,255) #colors defined in RGB format
black = (0,0,0)
red = (255,0,0)
grey = (107,107,107)

class Board:
    def __init__(self, initial_values):
        """Initializes the board with the given initial values.
        INPUTS:
            initial_values - Not sure what Smita will use so will adjust accordingly - using just 9x9 array for now
        """
        
        self.initial_values = (initial_values)

    def create_board(self):
        '''
        creates the 9x9 sudoku board to play on based on the initial values of the initialized board
        '''
        #create a board using initial values in pygame

        square_size = 65
        list_of_positions = [] #list storing the positions of all of the rectangles to input numbers into later
        for i in range(1, 10): #since 9 boxes needed
            for j in range(1,10):
                x_pos = j*square_size
                y_pos = i*square_size
                pygame.draw.rect(window, grey, (x_pos, y_pos, square_size, square_size), 2)
                #rectangle positions stored as left, right, top, bottom of a square:
                rectangle_positions = [x_pos, x_pos + square_size, y_pos, y_pos + square_size] 
                list_of_positions.append(rectangle_positions)

        for i in range(0,3): #making larger squares to add the border effect
            i += 1/3 #gross way to make it match up
            for j in range(0,3): 
                j += 1/3
                pygame.draw.rect(window, white, (i*square_size*3, j*square_size*3, square_size*3, square_size*3), 2)
        pygame.display.update()
        pos_count = 0
        #the next part can probably be added to the first for loop but idk if its worth it
        for i in self.initial_values:
            for j in i:
                if j != 0: #if 0 dont input any number
                    display_text = font.render(str(j), True, white)
                    window.blit(display_text, (list_of_positions[pos_count][0]+20, list_of_positions[pos_count][2]+5))
                pos_count += 1
        pygame.display.update()

    def update_board(): 
        '''
        notes for next time ig
        Can use the list_of_positions from create_board to identify the regions of each square
        then add some sort of text add thing using pygame to let users input numbers
        cursor detector to see if its in that range and if it is clicked it becomes some sort of text box?
        also need some way of identifying if the square is already filled or not, since we dont want them to overwrite
        the initial board values
        '''
        #change board values for empty squares depending on user input 
        pass

    def solve_board():
        '''
        can just take the solved board array and create board using it
        '''
        #run the final code solver function and take the output to populate this board
        pass

    def check_board():
        #compares solution with user input values
        pass

    def new_game():
        #create new board
        pass

solvable_example_1 = np.array([[0,0,7,4,9,1,6,0,5], 
                                [2,0,0,0,6,0,3,0,9],
                                [0,0,0,0,0,7,0,1,0],
                                [0,5,8,6,0,0,0,0,4],
                                [0,0,3,0,0,0,0,9,0],
                                [0,0,6,2,0,0,1,8,7],
                                [9,0,4,0,7,0,0,0,2],
                                [6,7,0,8,3,0,0,0,0],
                                [8,1,0,0,4,5,0,0,0]])

board1 = Board(solvable_example_1)
board1.create_board()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #have to add user input stuff here
    pygame.display.update()
pygame.quit()