from ex12.display import *
from ex12.game import *
from ex12.ai import *

if __name__ == '__main__':
    """
    Main function, running a game "four in a row"
    """
    while True:  # Runs games until the user asks to leave
        game = Game()

        # Select users - computer or person-
        first_menu = FirstMenuDisplay()
        select_users = first_menu.get_choice()
        players = {1: None, 2: None}

        # Create computer players-
        if select_users[1] == 2:
            players[1] = AI(game, 1)
        if select_users[2] == 2:
            players[2] = AI(game, 2)

        # Select colors for users-
        sec_menu = SecondMenuDisplay()
        color_dirc = sec_menu.get_choice()

        main_game = MainDisplay(game, players, color_dirc)
