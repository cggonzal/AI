from typing import List, Tuple
class Board:
    def __init__(self, numRows: int, numCols: int, obstacles: List[Tuple[int, int]] = None):
        '''
        Internally the class stores the board as a 2d list called data where data[row][col] == 1 if there is an obstacle
        and 0 if the space is free.
        obstacles is a list where each element is a tuple (row, col) denoting that there is an obstacle at (row, col).
        '''
        self.numRows = numRows
        self.numCols = numCols
        self.data = [[0] * numCols for _ in range(numRows)]

        if obstacles is not None:
            for row, col in obstacles:
                self.data[row][col] = 1


    def hasObstacle(self, row: int, col: int) -> bool:
        return self.data[row][col] == 1


    def __str__(self):
        return str(self.data)
