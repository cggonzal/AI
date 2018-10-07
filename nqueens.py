import random
class NQueens:
    def __init__(self,n):
        self.board, self.queenPositions  = self.getNewBoard(n)
        self.n = n

    def getNewBoard(self,n):
    # queens are represented as ones in 2d list of all zeros
    # Since it's a 2d list, each element is a row of zeros except for the queen
        board = []
        queensPos = []
        for x in range(n): # makes n x n board of zeros
            board.append([0]*n)

        for x in range(n): # sets a random value of each row to be 1, denoting the queen
            randomIndex = random.randint(0,n-1)
            board[x][randomIndex] = 1
            queensPos.append( (x,randomIndex) )

        return (board,queensPos)

    def allQueensSafe(self): # returns true if problem is solved and all queens safe, false otherwise
        for pos in self.queenPositions:
            if(self.UnderAttack(pos)):
                return False
        return True

    def attackViaCol(self,pos):
        for queen in self.queenPositions:
            if(pos[1] == queen[1] and queen != pos): # last inqueality checks to make sure you arent comparing the same queen
                return True
        return False

    def attackViaRow(self,pos):
        for queen in self.queenPositions:
            if(pos[0] == queen[0] and queen != pos):
                return True
        return False

    def attackViaDiagonal(self,pos):
        for queen in self.queenPositions:
            if (abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos):
                return True
        return False

    def UnderAttack(self,position):
        if(self.attackViaDiagonal(position)):
            return True

        if(self.attackViaRow(position)):
            return True

        if(self.attackViaCol(position)):
            return True

        return False

    def specificQueenConflicts(self,pos): # returns number of pieces attacking queen at position pos
        assert pos in self.queenPositions # checks to make sure given position is a queen
        count = 0
        for queen in self.queenPositions:
            if (abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos):
                count += 1

            if (pos[0] == queen[0] and queen != pos):
                count += 1

            if (pos[1] == queen[1] and queen != pos):
                count += 1

        return count

    def pickRandomQueen(self): # returns position of random queen
        newIndex = random.randint(0,self.n - 1)
        return self.queenPositions[newIndex]

    def printBoard(self): # prints out all positions of queens
        for queen in self.queenPositions:
            print(queen)


    def moveQueen(self,startPos,endPos): # moves queen from startpos to endpos
        assert self.board[startPos[0]][startPos[1]] == 1
        # above assert will fail if the start position does not have a queen
        self.board[startPos[0]][startPos[1]] = 0
        self.board[endPos[0]][endPos[1]] = 1
        self.queenPositions.remove(startPos)
        self.queenPositions.append(endPos)

    def availablePositions(self,pos):
        # returns list of tuples with all positions queen can go
        availablePos = []
        for x in range(self.n):
            availablePos.append( (pos[0],x) )

        return availablePos
