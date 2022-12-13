from tkinter import *
from settings.difficulty import Difficulty
from actors.square import Square
from actors.player import Player
import ctypes

window = Tk()
# Creates title and resolution of game
window.title("Minesweeper")
window.geometry('800x600')
window.configure(bg="#C4A484")  # Light brown background color

# Frame where all the squares are
center_frame = Frame(
    window,
    bg='#C4A484',
    width=40,
    height=24
)

# Places center frame in the center
center_frame.place(
    x=160,
    y=150,
)

# Top frame where player info will go
top_left_frame = Frame(
    window,
    bg='#C4A484',
    width=800,
    height=120
)

# Place top frame in top left corner
top_left_frame.place(
    x=0,
    y=0
)

# Generates all squares
for x in range(Difficulty.square_total_x):
    for y in range(
            Difficulty.square_total_y):  # Multiplies the x and y for the square amounts defined in the difficulty class
        square = Square(x, y)
        square.make_button(center_frame)
        square.square_button.grid(
            column=y, row=x
        )

# Displays player lives label
Player.make_player_lives_label(top_left_frame)
Player.player_lives_label.place(
    x=0,
    y=0
)

# Displays player defusals label
Player.make_defusals_label(top_left_frame)
Player.defusals_label.place(
    x=0,
    y=40
)

Square.rng_mines()

window.mainloop()  # Runs the window
