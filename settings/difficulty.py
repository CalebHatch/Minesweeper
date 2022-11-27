from easygui import *
class Difficulty():
    # Handles the difficulty selection for the game. Three difficulties are available: easy, normal, and hard. They are
    # implented in a way that will make it easy to add more in the future without major changes
    diff_choices = [ "Easy", "Normal", "Hard" ]
    diff_title = "Difficulty Select"

    difficulty_select = buttonbox ("Set difficulty", title = diff_title, choices = diff_choices )

    if difficulty_select == diff_choices[0]:
        diff_mode = "easy"
    elif difficulty_select == diff_choices[1]:
        diff_mode = "normal"
    elif difficulty_select == diff_choices[2]:
        diff_mode = "hard"

    msgbox (msg = "Difficulty set to: " + difficulty_select, title = diff_title)

    if diff_mode == "easy":
        player_lives = 2
        defusals = 3

        square_total_x = 4
        square_total_y = 4
        square_board_total = square_total_x * square_total_y

        mine_total = 2

    elif diff_mode == "normal":
        player_lives = 6
        defusals = 8

        square_total_x = 8
        square_total_y = 8
        square_board_total = square_total_x * square_total_y

        mine_total = 8

    elif diff_mode == "hard":
        player_lives = 8
        defusals = 12

        square_total_x = 12
        square_total_y = 12
        square_board_total = square_total_x * square_total_y

        mine_total = 12
