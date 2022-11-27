from tkinter import *
import settings.settings
import ctypes
import sys

class Player:
    # Controls all of the aspects of the player, like lives and defusals remaining
    lives = settings.settings.PLAYER_LIVES
    right_clicks = settings.settings.DEFUSALS
    defusals_label = None
    player_lives_label = None

    def make_player_lives_label(location):
        # Makes label for how many player lives are remaining
        label = Label(
            location,
            bg = '#C4A484',
            fg = 'black',
            text = f"Lives Remaining: {Player.lives}",
            font=('', 24)
        )

        Player.player_lives_label = label

    def make_defusals_label(location):
        # Makes label for how many player defusals are remaining
            defusals_label = Label(
                location,
                bg = '#C4A484',
                fg = 'black',
                text = f"Defusals Remaining: {Player.right_clicks}",
                font=('', 24)
            )

            Player.defusals_label = defusals_label

    def update_lives():
        # Updates how many lives the player has left
        Player.lives -= 1
        if Player.lives >= 0:
            Player.player_lives_label.configure(text=f"Lives Remaining: {Player.lives}")
        elif Player.lives < 0:  # Makes sure lives don't go negative
            pass

        if Player.lives <= 0:
            ctypes.windll.user32.MessageBoxW(0, 'Out of Lives. Better luck next time!', 'Game over', 0)
            sys.exit
            quit()

    def update_defusals():
        # Updates how many defusals the player has left
        Player.right_clicks -= 1
        if Player.right_clicks >= 0:
            Player.defusals_label.configure(text=f'Defusals Remaining: {Player.right_clicks}')
        elif Player.right_clicks < 0:  # Makes sure defusals don't go negative
            pass

        if Player.right_clicks <= 0:
            ctypes.windll.user32.MessageBoxW(0, 'Out of defusals', 'Can Not Defuse', 0)





