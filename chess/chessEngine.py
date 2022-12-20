# Stores information about the game - keep a log of the moves played

class GameState():
    def __init__(self):
        # Represent the chess board with a list of lists (8x8) with each list representing a row
        # We have used "xx" to represent empty squares - no pieces on that square
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
            ["xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
            ["xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
            ["xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        # Determine whose turn it is
        self.whiteToPlay = True
        # Keep a record of the moves played
        self.moveLog = []

    def makeMove(self, move):
        # When we move a piece from (a,b) to (c,d), the piece disappears from initial (a,b)
        self.board[move.startRow][move.startCol] = "xx"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        # Append this move to the log and switch the player
        self.moveLog.append(move)
        self.whiteToPlay = not self.whiteToPlay


class Move():
    # In chess, horizontal rows are called ranks - 6th rank, 3rd rank, etc.
    # Vertical columns are called files - d file, a file
    # toRanks = {"0": 8, "1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1}
    # toFiles = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h"}
    # Get corresponding array row number from rank
    toRows = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}
    # Get corresponding array column number from file
    toCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    # Get corresponding chess rank notation from array
    toRanks = {values: keys for keys, values in toRows.items()}
    # Get corresponding chess file notation from array
    toFiles = {values: keys for keys, values in toCols.items()}

    def __init__(self, initial_pos, final_pos, board):
        # Grab the 4 positions in play
        self.startRow = initial_pos[0]
        self.startCol = initial_pos[1]
        self.endRow = final_pos[0]
        self.endCol = final_pos[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        # Modify this to real chess notation
        return self.getRankAndFile(self.startRow, self.startCol) + self.getRankAndFile(self.endRow, self.endCol)

    def getRankAndFile(self, row, col):
        return self.toFiles[col] + self.toRanks[row]