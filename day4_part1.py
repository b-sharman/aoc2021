#!/usr/bin/python

class Tile(object):
    """
    Object representing a number on a Board.

    Stores whether it has been triggered by a number.
    """

    def __init__(self, value):
        self.value = value
        self.triggered = False # whether the value has come up yet

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def trigger(self):
        """ Call when this tile's number has been revealed. """
        self.triggered = True

    def update(self, num):
        """ Call this every time a number is revealed. """
        if num == self.value:
            self.trigger()


class Board(object):
    """ Object representing a Bingo board. """

    def __init__(self, board):
        # list of lists
        self.board = board
        # most recently triggered number
        self.most_recent_num = None

    def __str__(self):
        s = ""
        for row in self.board:
            s += "\t".join([str(tile) for tile in row]) + "\n"
        return(s)

    def update(self, num):
        """ Update each tile with the number. """
        for row in self.board:
            for tile in row:
                tile.update(num)
        self.most_recent_num = num

    def get_won(self):
        """ Return true if any row or column of Tiles is entirely triggered. """
        # check rows
        for row in self.board:
            if all([tile.triggered for tile in row]):
                print("won on this row:", row)
                return True

        # check columns
        for col in range(len(self.board[0])):
            if all([self.board[row][col].triggered for row in range(len(self.board))]):
                print("won on column", col)
                return True

        # if true has not yet been returned, the board is not winning
        return False

    def get_untriggered_sum(self):
        """ Return the sum of the values of the untriggered tiles. """

        # dirty but it works
        ret = 0
        for row in self.board:
            for tile in row:
                if not tile.triggered:
                    ret += tile.value

        return ret

    def get_score(self):
        """
        Return the score calculated like this:

        sum of uncalled numbers (i.e. sum of values of untriggered tiles)
        multiply that sum by the most recent called number
        """

        if self.most_recent_num is None:
            return 0
        else:
            return self.get_untriggered_sum() * self.most_recent_num

    @staticmethod
    def parse(s):
        """ Parse a string s which is in turn parsed from the input file. """

        # list comprehension would get too messy here
        board = []
        for row in s.split("\n"):
            board.append([Tile(int(x)) for x in row.split()])

        return Board(board)


class Game(object):
    """ Object representing a game of Bingo. """

    def __init__(self, boards, bingo_subsystem):
        self.boards = boards
        self.bs = bingo_subsystem

    def play_round(self, num):
        """ Update each Bingo board according to num, which has been revealed. """
        for board in self.boards:
            board.update(num)

    def play(self):
        for num in self.bs:
            # if any board has a winning configuration
            if any([board.get_won() for board in self.boards]):
                break
            self.play_round(num)

        # show winning board(s)
        for board in self.boards:
            if board.get_won():
                print("\nThis board won with a score of " + str(board.get_score()) + ":")
                print(board)

        # I assume the data is engineered so that this never happens,
        # but it might be good to check:
        if not any([board.get_won() for board in self.boards]):
            print("No board won after going through all the numbers.")


def main():
    with open("day4_input.txt") as f:
        content = f.read().strip()
        f.close()
        # remove pesky alignment spaces
        while "  " in content:
            content = content.replace("  ", " ")
        content = content.split("\n\n")

        bingo_subsystem = [int(x) for x in content.pop(0).split(",")]
        board_strings = content.copy()
        boards = [Board.parse(s) for s in board_strings]
        
        # print(bingo_subsystem)
        # print()
        # for board in boards[:3]: # first three boards
        #     print(board)

        game = Game(boards, bingo_subsystem)
        game.play()

main()
