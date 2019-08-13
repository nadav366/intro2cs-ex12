import tkinter as tk


SIZE = "700x700+250+0"
FONT = "Algerian"

MAIN_TITLE_SIZE = 50
SECOND_TITLE_SIZE = 30
SMALL_TITLE = 20

TITLE = "Four in a Row"
MAIN_TITLE = "choose player-"
SECOND_TITLE = "Click on the image to select"
TURN_MSG = "The turn of player "
WIN_MSG = {1: "player 1 won!!",
           2: "player 2 won!!",
           0: "Tie, the game is over"}
MORE = "Another game?"
DONE = "Done?"


class FirstMenuDisplay:
    """
    Object that is the graphics of the selection screen -
    to select the type of users
    """

    def __init__(self):
        """
        constructor.
        Initializes all variables of the object And runs the screen
        """
        self.__root = tk.Tk()
        self.__dict_player = {}  # Variable to save user selection

        # Set the screen properties
        self.__root.title(TITLE)
        self.__root.geometry(SIZE)
        self.__root.protocol("WM_DELETE_WINDOW", exit)

        # Create image files for graphics
        comp = tk.PhotoImage(file="ex12//comp.png")
        man = tk.PhotoImage(file="ex12//man.png")

        # creating headlines-
        lanel_1 = tk.Label(self.__root, text=MAIN_TITLE,
                           font=(FONT, MAIN_TITLE_SIZE))
        lanel_1.pack(side=tk.TOP)
        lanel_2 = tk.Label(self.__root, text=SECOND_TITLE,
                           font=(FONT, SECOND_TITLE_SIZE))
        lanel_2.pack(side=tk.TOP)

        # Creating the Options grid-
        lanel_3 = tk.Frame(self.__root)
        lanel_3.pack()

        ply1 = tk.Label(lanel_3, text="player 1:", font=(FONT, SMALL_TITLE))
        ply1.grid(row=0, column=1)
        ply2 = tk.Label(lanel_3, text="player 2:", font=(FONT, SMALL_TITLE))
        ply2.grid(row=0, column=2)

        # Placing the photos-
        man_1 = tk.Button(lanel_3, image=man, overrelief=tk.SUNKEN,
                          command=self.__choose_player(lanel_3, 1, 1),)
        man_1.grid(row=1, column=1)

        man_2 = tk.Button(lanel_3, image=man, overrelief=tk.SUNKEN,
                          command=self.__choose_player(lanel_3, 2, 1, ))
        man_2.grid(row=1, column=2)

        comp_1 = tk.Button(lanel_3, image=comp,  overrelief=tk.SUNKEN,
                           command=self.__choose_player(lanel_3, 1, 2))
        comp_1.grid(row=2, column=1)

        comp_2 = tk.Button(lanel_3, image=comp, overrelief=tk.SUNKEN,
                           command=self.__choose_player(lanel_3, 2, 2))
        comp_2.grid(row=2, column=2)

        self.__root.mainloop()

    def __choose_player(self, lanel, player, choose):
        """
        A function that creates a function to perform when you  Select Player-
        :param lanel: A lanel object on which the images are located.
        :param player: Which player is chosen? (1 or 2)
        :param choose: What was chosen? (1 person, 2 computer)
        :return: Function to perform at the time of the click
        """

        def clicking():
            """
            Function that occurs when you press Select.
            Coverage of the image is more relevant, and updating of the
            dictionary is under review.
            If you have already selected two - close the window.
            """
            self.__dict_player[player] = choose

            white = tk.PhotoImage(file="ex12//white.png")
            caver = tk.Button(lanel, image=white)
            caver.grid(row=(choose % 2) + 1, column=player)

            if len(self.__dict_player) == 2:
                self.__root.after(1000, self.__root.destroy)

        return clicking

    def get_choice(self):
        """
        :return: A dictionary that preserves users' selection.
        """
        return self.__dict_player


SELECT_ORDER = "Select color for player "


class SecondMenuDisplay:
    """
    Object that is the graphics of the color selection screen -
    to select the color of the users discs
    """

    def __init__(self):
        """
        constructor.
        Initializes all variables of the object And runs the screen
        """
        self.__root = tk.Tk()
        self.__dict_color = {}  # Variable to save user selection
        # to keep the buttons that the garbage collector will not destroy them-
        self.__saver = {}

        # Set the screen properties
        self.__root.title(TITLE)
        self.__root.geometry(SIZE)
        self.__root.protocol("WM_DELETE_WINDOW", exit)

        # Create a title-
        self.__lanel_1 = tk.Label(self.__root, text=SELECT_ORDER + "1-",
                                  font=(FONT, SECOND_TITLE_SIZE))
        self.__lanel_1.pack(side=tk.TOP)

        # Create buttons to choose from -
        lanel_2 = tk.Frame(self.__root)
        lanel_2.pack()
        self.__draw_colors(lanel_2)

        self.__root.mainloop()

    def __draw_color(self, lanel, filename, row, col):
        """
        A function that produces a button for one color
        :param lanel: Label object Place the button on it.
        :param filename: Name the image file to the button
        :param row: row to position the button
        :param col: Column to position the button
        """
        button_i = tk.PhotoImage(file=filename + ".png")
        button = tk.Button(lanel)
        button.config(image=button_i, overrelief=tk.SUNKEN, borderwidth=0,
                      command=self.__choose_color(filename, button))
        button.grid(row=row, column=col)
        self.__saver[button_i] = button

    def __draw_colors(self, lanel):
        """
        A function that produces a buttons for all colors
        :param lanel: Label object Place the button on it.
        """
        self.__draw_color(lanel, "ex12//blue", 0, 0)
        self.__draw_color(lanel, "ex12//black", 0, 1)
        self.__draw_color(lanel, "ex12//gray", 0, 2)
        self.__draw_color(lanel, "ex12//ornge", 1, 0)
        self.__draw_color(lanel, "ex12//grin", 1, 1)
        self.__draw_color(lanel, "ex12//pink", 1, 2)
        self.__draw_color(lanel, "ex12//yellow", 2, 0)
        self.__draw_color(lanel, "ex12//azure", 2, 1)
        self.__draw_color(lanel, "ex12//purple", 2, 2)

    def __choose_color(self, filename, button):
        """
        A function that creates a function to perform when you Select color-
        :param filename: The image file name of the button clicked
        :param button: Button object pressed
        :return: Function to execute when the button is pressed
        """

        def clicking():
            """
            A function performed when a button is pressed, updates the
            dictionary, covers the button and
            if two are already selected, closes the window.
            """
            self.__dict_color[len(self.__dict_color) + 1] = filename

            caver = tk.PhotoImage(file="ex12//black_caver.png")
            button.config(image=caver, command=lambda: 1)
            self.__lanel_1.config(text=SELECT_ORDER + "2-")

            if len(self.__dict_color) == 2:
                self.__root.after(1000, self.__root.destroy)

        return clicking

    def get_choice(self):
        """
        A function that returns the selection
        :return: Dictionary with color selection
        """
        return self.__dict_color


class MainDisplay:
    """
    An object that is the main window of a four-row game.
    """

    def __init__(self, game, players, color_dirc):
        """
        constructor.
        Initializes all variables of the object And runs the screen
        :param game:
        :param players:
        :param color_dirc:
        """
        self.__root = tk.Tk()

        self.__game = game
        self.__buttom_dict = {}
        self.__next_game = True
        self.__players = players
        self.__color_dirc = color_dirc
        self.__wins_image_saver = dict()

        # Set the screen properties
        self.__root.title(TITLE)
        self.__root.geometry(SIZE)
        self.__root.configure(bg="white")
        self.__root.protocol("WM_DELETE_WINDOW", exit)

        # Create image objects to disks and save in dictionary.
        first_color = tk.PhotoImage(file=color_dirc[1] + ".png")
        sec_color = tk.PhotoImage(file=color_dirc[2] + ".png")
        self.__player_color = {1: first_color, 2: sec_color}

        # Create a title-
        self.__lanel_1 = tk.Label(self.__root, text=(
                TURN_MSG + str(self.__game.get_current_player())),
                                  font=(FONT, SECOND_TITLE_SIZE), bg="white")
        self.__lanel_1.pack(side=tk.TOP)

        # Create a grid of buttons to the clipboard
        lanel_2 = tk.Frame(self.__root)
        lanel_2.pack()

        filename = tk.PhotoImage(file="ex12//empty.png")
        for col in range(7):
            for row in range(6):
                button = tk.Button(lanel_2)
                button.config(bg="black", image=filename, overrelief=tk.SUNKEN,
                              command=self.__choose_disc(col), borderwidth=0)
                button.grid(row=row, column=col)
                self.__buttom_dict[(row, col)] = button

        self.__root.after(600, self.__check_for_ai)
        self.__root.mainloop()

    def get_finish(self):
        """
        A function that returns whether the user is interested in another game
        """
        return self.__next_game

    def __check_for_ai(self):
        """
        A function that checks whether the AI ​​queue is playing,
        and if so does a move.
        """
        if self.__players[self.__game.get_current_player()] is not None and\
                self.__game.get_winner() is None:
            self.__choose_disc(self.__players[
                                   self.__game.get_current_player()].
                               find_legal_move(), ai=True)()

    def __check_for_finish(self):
        """
        Check whether the game is over.
        If so, perform actions to end the game.
        :return: True if the game not over, None if is over
        """
        result = self.__game.get_winner()

        # If the game is not over, update the title-
        if result is None:
            self.__lanel_1.config(font=(FONT, SECOND_TITLE_SIZE),
                                  text=(TURN_MSG + str(
                                      self.__game.get_current_player())))
            return True

        # Update all buttons, following the end of the game-
        wins_cor = self.__game.get_wins_cor()
        for cor, button in self.__buttom_dict.items():
            button.config(command=lambda: 1)
            if cor in wins_cor:
                win_image = tk.PhotoImage(
                    file=self.__color_dirc[result] + "_win.png")
                button.config(image=win_image)
                self.__wins_image_saver[cor] = win_image

        self.__lanel_1.config(text=WIN_MSG[result],
                              font=(FONT, SECOND_TITLE_SIZE))

        # Create buttons to check the game's continuation
        lanel_3 = tk.Frame(self.__root)
        lanel_3.pack()

        but = tk.Button(lanel_3, bg="white",
                        activebackground="white",
                        text=MORE,
                        command=lambda: self.__root.destroy(),
                        borderwidth=5,
                        overrelief=tk.SUNKEN,
                        font=(FONT, SMALL_TITLE))
        but.grid(row=0, column=0)

        but = tk.Button(lanel_3, bg="white",
                        activebackground="white",
                        text=DONE,
                        command=exit,
                        borderwidth=5,
                        overrelief=tk.SUNKEN,
                        font=(FONT, SMALL_TITLE))
        but.grid(row=0, column=1)

    def __choose_disc(self, col, ai=False):
        """
        Create a function to perform when you press the button
        :param col: The button column
        :return: Function to perform when clicking on one of the columns
        """

        def clicking():
            """
            A function performed when a button is pressed and updates the
            screen and game object by clicking.
            """
            if self.__players[self.__game.get_current_player()] is None or ai:
                for row in range(5, -1, -1):
                    if self.__game.get_player_at(row, col) is None:
                        self.__buttom_dict[(row, col)].config(
                            image=self.__player_color[
                                self.__game.get_current_player()],
                            overrelief=tk.FLAT,
                            command=lambda: 1)

                        self.__game.make_move(col)
                        if self.__check_for_finish():
                            self.__root.after(700, self.__check_for_ai)
                        return

        return clicking
