import random

PLAYER_ERROR = "Wrong player"
MOVES_ERROR = "No possible AI moves"
NUM_OF_ROW = 6
NUM_OF_COL = 7
EMPTY_CELL = 0



class AI:
    """
    An object that is a "player" artificial intelligence in four in a row game
    """

    def __init__(self, game, player):
        """
        constructor
        :param game: four in a row, game Object
        :param player: Integer number, player number
        """
        self.__game = game
        self.__player = player

    def find_legal_move(self, timeout=None):
        """
        A function that selects a move for the computer user.
        :param timeout:
        :return:
        """
        if self.__game.get_current_player() != self.__player:
            raise Exception(PLAYER_ERROR)
        if self.__game.get_winner() is not None:
            raise Exception(MOVES_ERROR)

        optionals = []
        for col in range(NUM_OF_COL):
            if not self.__game.get_player_at(0, col):
                optionals.append(col)

        return random.choice(optionals)


    def get_last_found_move(self):
        pass


