from copy import deepcopy

EMPTY_CELL = 0
ERROR_MOVE_MSG = "Illegal move"
ERROR_LOC_MSG = "Illegal locarion"


class Game:
    """
    An object that is a "brain" of four in a row game.
    """

    NUM_OF_ROW = 6
    NUM_OF_COL = 7

    def __init__(self):
        """
        Constructor, creates a blank board for the game, and counts moves.
        """
        self.__board = [
            [EMPTY_CELL for _ in range(self.NUM_OF_COL)]
            for _ in range(self.NUM_OF_ROW)
        ]
        self.__moves_counter = 0
        self.__wins_cor = set()

    def make_move(self, column):
        """
        A function that do move a game - adds a disk in the given column.
        If you can not make the move, there is Exception.
        :param column: Integer, a column to add to it a disk.
        :return: None
        """
        for row in range(self.NUM_OF_ROW - 1, -1, -1):
            if self.__board[row][column] == EMPTY_CELL:
                self.__board[row][column] = (self.__moves_counter % 2) + 1
                self.__moves_counter += 1
                return
        raise Exception(ERROR_MOVE_MSG)

    def get_winner(self):
        """
        A function that checks the state of the game
        :return: User number, if it is won. 0 If a tie, None if not finished.
        """
        cols_res = self.__cols_scan()
        if cols_res:
            return cols_res

        rows_rus = self.__rows_scan()
        if rows_rus:
            return rows_rus

        # Checks diagonals from one direction
        diagonal_1 = self.__diagonal_scan(self.__board, 0)
        if diagonal_1:
            return diagonal_1

        # Checks diagonally on the other side (mirror the board)
        diagonal_2 = self.__diagonal_scan(self.__board_mirror(), 6)
        if diagonal_2:
            return diagonal_2

        # Checks that there is more where to put a disc
        for col in range(self.NUM_OF_COL):
            if self.__board[0][col] == EMPTY_CELL:
                return

        return 0

    def __cols_scan(self):
        """
        Checks if there is a win in the board columns
        :return: If someone won - his number. None if not.
        """
        for col in range(self.NUM_OF_COL):
            sequence = 0
            sequencer_player = 0
            self.__wins_cor = set()
            for row in range(self.NUM_OF_ROW - 1, -1, -1):
                if self.__board[row][col] == EMPTY_CELL:
                    break  # Finish checking the current column
                if self.__board[row][col] == sequencer_player:
                    sequence += 1
                    self.__wins_cor.add((row, col))
                    if sequence == 4:
                        return sequencer_player
                else:
                    sequence = 1
                    sequencer_player = self.__board[row][col]
                    self.__wins_cor = set()
                    self.__wins_cor.add((row, col))

    def __rows_scan(self):
        """
        Checks if there is a win in the board rows
        :return: If someone won - his number. None if not.
        """
        for row in range(len(self.__board)):
            sequence = 0
            sequencer_player = 0
            self.__wins_cor = set()
            for col in range(self.NUM_OF_COL):
                # An empty cell - resets the sequence.
                if self.__board[row][col] == EMPTY_CELL:
                    sequence = 0
                    sequencer_player = 0
                    self.__wins_cor = set()
                    continue
                if self.__board[row][col] == sequencer_player:
                    sequence += 1
                    self.__wins_cor.add((row, col))
                    if sequence == 4:
                        return sequencer_player
                else:
                    sequence = 1
                    sequencer_player = self.__board[row][col]
                    self.__wins_cor = set()
                    self.__wins_cor.add((row, col))

    def __diagonal_scan(self, board, dirc):
        """
        Checks if there is a win in the board diagonals
        :param board: List of lists, represents the board for review.
        :return: If someone won - his number. None if not.
        """
        # Scan from the first-row diagonal
        for col in range(len(board[0]) - 3):
            sequence = 0
            sequencer_player = 0
            self.__wins_cor = set()
            for row in range(len(board)):
                if col + row >= len(board[0]):
                    break
                if board[row][col + row] == EMPTY_CELL:
                    sequence = 0
                    sequencer_player = 0
                    self.__wins_cor = set()
                elif board[row][col + row] == sequencer_player:
                    sequence += 1
                    self.__wins_cor.add((row, abs(dirc - col - row)))
                    if sequence == 4:
                        return sequencer_player
                else:
                    sequence = 1
                    sequencer_player = board[row][col + row]
                    self.__wins_cor = set()
                    self.__wins_cor.add((row, abs(dirc - col - row)))

        # Scan the diagonal from the last column except the first
        for row in range(1, len(board) - 3):
            sequence = 0
            sequencer_player = 0
            self.__wins_cor = set()
            for col in range(len(board[0])):
                if col + row >= len(board):
                    break
                if board[col + row][col] == EMPTY_CELL:
                    sequence = 0
                    sequencer_player = 0
                    self.__wins_cor = set()
                elif board[col + row][col] == sequencer_player:
                    sequence += 1
                    self.__wins_cor.add((col + row, abs(dirc - col)))
                    if sequence == 4:
                        return sequencer_player
                else:
                    sequence = 1
                    sequencer_player = board[col + row][col]
                    self.__wins_cor = set()
                    self.__wins_cor.add((col + row, abs(dirc - col)))

    def __board_mirror(self):
        """
        Function reverses the order of the board rows
        :return: list containing lists, the new board
        """
        new_board = deepcopy(self.__board)
        for row in range(len(new_board)):
            new_board[row] = new_board[row][::-1]
        return new_board

    def get_player_at(self, row, col):
        """
        A function that returns the condition of a given cell
        :param row: An integer representing a row
        :param col: An integer representing a col
        If the request is invalid- Exception
        :return: None If the cell is empty, the user number if the cell is full
        """
        try:
            if self.__board[row][col] == EMPTY_CELL:
                return
        except:
            raise Exception(ERROR_LOC_MSG)
        else:
            return self.__board[row][col]

    def get_current_player(self):
        """
        :return: The number of the player whose turn to play
        """
        return (self.__moves_counter % 2) + 1

    def get_wins_cor(self):
        return self.__wins_cor
