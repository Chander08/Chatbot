import pygame 
import numpy as np 

pygame.init() 
window = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Sudoku") #changes window name


class Board:
    def __init__(self, initial_values):
        """Initializes the board with the given initial values.
        INPUTS:
            initial_values - Not sure what Smita will use so will adjust accordingly - using just a list for now
            (list values from left to right top to bottom, leaving blanks as a space for now?)
        """

        self.initial_values = initial_values

    def create_board():
        #create a board using initial values in pygame

    def update_board(): 
        #change board values for empty squares depending on user input 

    def solve_board():
        #run the final code solver function and take the output to populate this board

    def clear_board():
        #either this or delete board and create a new one? 
