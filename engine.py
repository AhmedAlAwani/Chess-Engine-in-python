# storing the of the game and valid moves in the current state also move logs

class GameState():
    def __init__(self):
        # board 8*8 2d list
        # R,N,Q,K,p for piecs
        # b for black
        # w for white
        # -- for empty
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.whiteToMove=True
        self.moveLog=[]

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)#so we can undo it
        self.whiteToMove= not self.whiteToMove  #swap players


class Move():

    # Maps chess ranks (1-8) to row indexes (7-0)
    ranksToRows = {
        "1": 7, "2": 6, "3": 5, "4": 4,
        "5": 3, "6": 2, "7": 1, "8": 0
    }

    # Reverse mapping: row indexes back to ranks
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    # Maps chess files (a-h) to column indexes (0-7)
    filesToCols = {
        "a": 0, "b": 1, "c": 2, "d": 3,
        "e": 4, "f": 5, "g": 6, "h": 7
    }

    # Reverse mapping: column indexes back to files
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq,endSq, board ):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved=board[self.startRow][self.startCol]
        self.pieceCaptured=board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
