# min conflicts solver for NQueens problems
from nqueens import *
n = 8
NQ = NQueens(n)
timer = 0
while(not NQ.allQueensSafe()):
    minAttacks = n + 1 # n + 1 is greater than any possibility of attacks so this is guaranteed to get minimized
    pickedQueen = NQ.pickRandomQueen() 

    positions = NQ.availablePositions(pickedQueen)
    minConflictPosition = (-1,-1)
    for pos in positions: # iterate through all positions of pickedQueen and move to position of minimum conflict
        NQ.moveQueen(pickedQueen,pos)
        newNumberOfConflicts = NQ.specificQueenConflicts(pos)
        if(newNumberOfConflicts < minAttacks ):
            minConflictPosition = pos
            minAttacks = newNumberOfConflicts
        NQ.moveQueen(pos,pickedQueen) # move queen back

    NQ.moveQueen(pickedQueen,minConflictPosition)# move queen to least conflict spot

print(NQ.printBoard())
