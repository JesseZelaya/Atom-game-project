# Author: Jesse Zelaya
# Date: 8/7/2020
# Description: Black box game creates in python and played in console through interaction.
# In this version, the guessing player will start with 25 points. As stated on the Wikipedia
# https://en.wikipedia.org/wiki/Black_Box_%28game%29
# page, "Each entry and exit location counts as a point" that is deducted from the current score.
# If any entry/exit location of the current ray is shared with any entry/exit of a previous ray,
# then it should not be deducted from the score again. Each incorrect guess of an atom position
# will cost 5 points, but repeat guesses should not be deducted from the score again.


class BlackBoxGame:
    """
    Creates black box game object that can be interacted with by user to play the Black box game.
    This class takes rows, and columns as two separate list parameters and
    takes a tuple for the coordinates of the atoms used in the game.
    This will act as a 'gameboard' or game object and will use the methods
    in the class to play and update the player on their status of the game.
    """

    def __init__(self, location_tuple):
        """initializes parameters passed in to start game"""
        self._location_tuple = location_tuple
        self._player_points = 25
        self._location_tuple = location_tuple
        self._atom_count = len(location_tuple)
        self._guess_list = []
        self._entry_exit_list = []
        self._entry_coord = ''

        # initialize board

        row0 = ['l', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r']
        row1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row5 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row6 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row7 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row8 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        row9 = ['L', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R']

        self._board_list = [row9, row8, row7, row6, row5, row4, row3, row2, row1, row0]
        # add atoms example [(3,2),(1,7),(4,6),(8,8)]
        # adding atoms works
        for ball in self._location_tuple:
            self._board_list[ball[0] ][ball[1]] = 'X'

    def print_board(self):
        """
            Prints out current board with values marked for entry
            and exit points.
        :return: No return; only prints to console.
        """
        #  print board works for printing and showing initialization
        for nn in range(len(self._board_list) - 1, -1, -1):
            print(self._board_list[nn])

    def shoot_ray(self, row, col):
        """
            This lets the user pick a row and column for an entry point
            score should be adjusted accordingly.
        :param row: coordinate for entry
        :param col: coordinate for entry
        :return: tuple of exit or return non if there is a hit
                if chosen row and column in corner return false
        """
        self._entry_coord = (row, col) # keeps track of entry

        if (row, col) == (0, 9) or (row, col) == (0, 0) or (row, col) == (9, 0) or (row, col) == (9, 9):
            return False
        # self._entry_exit_list.append((row, col))
        if row == 0:  # shooting upward
            shot_result = self.shoot_upward(row, col)
            self.handle_shot_points(shot_result)
            return shot_result
        elif col == 9:  # shooting left
            shot_result = self.shoot_left(row, col)
            self.handle_shot_points(shot_result)
            return shot_result
        elif col == 0:  # shoot right
            shot_result = self.shoot_right(row, col)
            self.handle_shot_points(shot_result)
            return shot_result
        elif row == 9:  # shoot down
            shot_result = self.shoot_down(row, col)
            self.handle_shot_points(shot_result)
            return shot_result

    def handle_shot_points(self, shot_result):
        """handles points for result of each shot according to entry and exit
            """
        # check entry coordinates and exit coordinates against given list and variables
        # if exit or entry already in list do not subtract from score
        # if they are not then subtract for the one not in list or any not None
        if self._entry_coord == shot_result and self._entry_coord not in self._entry_exit_list:
            self._entry_exit_list.append(self._entry_coord)
            self._player_points -= 1
            return None
        if self._entry_coord not in self._entry_exit_list:
            self._player_points -= 1
            self._entry_exit_list.append(self._entry_coord)
        if shot_result not in self._entry_exit_list and shot_result is not None:
            self._entry_exit_list.append(shot_result)
            self._player_points -= 1
        if shot_result is None and self._entry_coord not in self._entry_exit_list:
            self._entry_exit_list.append(self._entry_coord)
            self._player_points -= 1


    def shoot_upward(self, row, col):
        """
        shoots in the upward direction until it reaches end of board or encounters an
        atom
        :return: position of exit or none
        """
        # base case
        #self.shoot_right(1,1)
        if row == 9:
            return row, col # exit_point
        if self._board_list[row + 1][col] == 'X': # atom in front
            return None
        if (self._board_list[row + 1][col - 1] == 'X' and row == 0): # atom diagonal edge
            end_point = self.shoot_right(row + 2, col)
        elif self._board_list[row + 1][col + 1] == 'X' and row == 0:
            end_point = self.shoot_left(row + 2, col)
        elif self._board_list[row + 1][col - 1] == 'X': # atom on either side
            return self.shoot_right(row, col)
        elif self._board_list[row + 1][col + 1] == 'X':
            return self.shoot_left(row, col)
        else:
            end_point = self.shoot_upward(row + 1, col)
        return end_point

    def shoot_down(self, row, col):
        """
        shoots in the upward direction until it reaches end of board or encounters an
        atom
        :return: position of exit or none
        """
        in_out_points = 1
        # base case
        if row == 0:
            return row, col # exit_point
        if self._board_list[row - 1][col] == 'X':
            return None
        if self._board_list[row - 1][col - 1] == 'X' and row == 9:
            end_point = self.shoot_right(row - 2, col)
        elif self._board_list[row - 1][col + 1] == 'X' and row == 9:
            end_point = self.shoot_left(row - 2, col)
        elif self._board_list[row - 1][col - 1] == 'X': # atom on left
            end_point = self.shoot_right(row, col)
        elif self._board_list[row - 1][col +1] == 'X':
            end_point = self.shoot_left(row, col)
        else:
            end_point = self.shoot_down(row - 1, col)
        return end_point

    def shoot_left(self, row, col):
        """
        shoots in the left direction until it reaches end of board or encounters atom
        :return: exit coordinates or None
        """
        if col == 0:
            return row, col
        if self._board_list[row][col - 1] == 'X':
            return None
        if self._board_list[row + 1][col - 1] == 'X' and col == 9:
            return self.shoot_down(row, col - 2)
        elif self._board_list[row - 1][col - 1] == 'X' and col == 9:
            return self.shoot_upward(row, col - 2)
        elif self._board_list[row + 1][col - 1] == 'X': # atom above
            end_point = self.shoot_down(row, col)
        elif self._board_list[row - 1][col - 1] == 'X':
            end_point = self.shoot_upward(row, col)
        else:
            end_point = self.shoot_left(row, col - 1)
        return end_point

    def shoot_right(self, row, col):
        """
        shoots in the left direction until it reaches end of board or encounters atom
        :return: exit coordinates or None
        """
        if col == 9:
            return row, col
        if self._board_list[row][col + 1] == 'X': # see if x in front
            return None
        if self._board_list[row + 1][col + 1] == 'X' and col == 0: # check for x's left and right at edge
            return self.shoot_down(row, col + 2)
        elif self._board_list[row - 1][col + 1] == 'X' and col == 0:
            return self.shoot_upward(row, col + 2)
        elif self._board_list[row + 1][col + 1] == 'X': # check for x's left and right for corner
            return self.shoot_down(row, col)
        elif self._board_list[row -1][col+1] == 'X':
            return self.shoot_upward(row, col)
        else:
            end_point = self.shoot_right(row, col + 1)
        return end_point

    def guess_atom(self, row, col):
        """
            Coordinates guess if atom is at chosen site. adjusts players
            score accordingly.
        :param row:
        :param col:
        :return: if atom at chosen coordinate return true, else return false
        """
        # checked and works well
        # choose coordinate check if atom, return accordingly
        if self._board_list[len(self._board_list)-1 - row][col] == 'X':
            self._atom_count -= 1
            return True
        else:
            if (row,col) not in self._guess_list:
                self._player_points = self._player_points - 5
            if (row, col) not in self._guess_list:
                self._guess_list.append((row, col))
            return False

    def get_score(self):
        """
            Returns the current score of a player.
            No parameters.
        :return: Player score
        """
        return self._player_points

    def atoms_left(self):
        """
            No parameters.
        :return: Returns the number of atoms not guessed by player.
        """
        return self._atom_count





