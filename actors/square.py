from tkinter import *
from settings.difficulty import Difficulty
import random
import ctypes
import sys
from actors.player import Player


class Square:
    # These are the squares that can either contain a number giving a clue to how many mines are near or are a mine
    # themselves.
    square_defused = False
    square_amount = (Difficulty.square_board_total - Difficulty.mine_total)  # Amount of squares minus mines

    all = []

    def __init__(self, x, y, is_a_mine=False):
        # Initializes properties for squares
        self.is_a_mine = is_a_mine
        self.square_button = None
        self.square_opened = False
        self.x = x
        self.y = y

        # Adds squares to a list
        Square.all.append(self)

    def make_button(self, location):  # Creates button for squares
        button = Button(
            location,
            bg='#C0C0C0',
            fg='#191970',
            width=4,
            height=1,
        )

        button.bind('<Button-1>', self.left_click)  # Takes left click input for button
        button.bind('<Button-3>', self.right_click)  # Takes right click input for button

        self.square_button = button

    def right_click(self, event):
        # Handles what happens when player right clicks. Player right clicks to defuse mines
        if not self.square_opened:
            Player.update_defusals()
        if self.is_a_mine and Player.right_clicks > 0:
            self.square_button.configure(text='X', fg='black')
            self.square_defused = True
            self.square_opened = True
            if not self.square_opened:
                self.square_amount -= 1
        else:
            pass

    def left_click(self, event):
        # Handles what happens when player left clicks. Player left clicks to select squares/mines
        if self.is_a_mine and self.square_defused is False:
            Player.update_lives()
            self.reveal_mine()
        else:
            self.reveal_hint()
        if Square.square_amount == 0:
            ctypes.windll.user32.MessageBoxW(0, 'You selected all of the squares! You win!', 'Winner!', 0)
            sys.exit
            quit()

    def rng_mines():
        # Selects 16 random squares to be mines
        mines = random.sample(
            Square.all, Difficulty.mine_total
        )

        for mine in mines:
            mine.is_a_mine = True

    def get_square_with_coords(self, x, y):
        # Gets square based on its coordinates
        for square in Square.all:
            if square.x == x and square.y == y:
                return square

    @property
    def bordering_squares(self):
        # Finds bordering squares
        borders = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        squares = [self.get_square_with_coords(self.x + dx, self.y + dy) for dx, dy in borders]
        return [square for square in squares if square is not None]

    @property
    def find_mines(self):
        # Determines how many mines are bordering the square 
        mine_count = 0
        for square in self.bordering_squares:
            if square.is_a_mine:
                mine_count += 1

        return mine_count

    def reveal_hint(self):
        if self.square_opened == False and self.is_a_mine == False:
            Square.square_amount -= 1
            # Reveals how many mines are bordering the square
            if self.square_defused is False:
                self.square_button.configure(text=self.find_mines)
            elif self.square_defused is True:
                pass

            self.square_button.configure(bg='#a9a9a9')  # Changes square background color when opened

            self.square_opened = True
        elif self.square_opened == True:
            pass

    def reveal_mine(self):
        # Reveals mines and takes a life away from player
        if self.square_opened == False:
            self.square_button.configure(bg='red')
            self.square_opened = True
        elif self.square_opened == True:  # Won't do anything if square is already opened
            pass
