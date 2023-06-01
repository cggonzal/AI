from queue import PriorityQueue

class Node:
    def __init__(self, row, col, prevNode, costSoFar):
        self.row = row
        self.col = col
        self.costSoFar = costSoFar
        self.prevNode = prevNode
    
    def __lt__(self, other):
        return self.costSoFar < other.costSoFar

def getPath(node):
    path = []
    iterNode = node
    while iterNode != None:
        row = iterNode.row
        col = iterNode.col
        path.append((row, col))
        iterNode = iterNode.prevNode

    path.reverse()
    return path

def isValid(row, col, numRows, numCols, visited):
    return 0 <= row and row < numRows and \
           0 <= col and col < numCols and \
           (row, col) not in visited


def heuristic(row, col, targetRow, targetCol):
    return abs(targetRow - row) + abs(targetCol - col)

numRows = 5
numCols = 5

board = [[0] * numCols for _ in range(numRows)]

startRow, startCol = 0, 0  # top left
targetRow, targetCol = numRows - 1, numCols - 1  # bottom right

pq = PriorityQueue()
pq.put(Node(startRow, startCol, None, 0))

visited = set()

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while not pq.empty():
    currentNode = pq.get()
    visited.add((currentNode.row, currentNode.col))
    
    if currentNode.row == targetRow and currentNode.col == targetCol:  # solution found
        print("Path found: ")
        print(getPath(currentNode))
        break
    
    for d in directions:
        nextRow = d[0] + currentNode.row
        nextCol = d[1] + currentNode.col
        if isValid(nextRow, nextCol, numRows, numCols, visited):
            cost = currentNode.costSoFar + heuristic(nextRow, nextCol, targetRow, targetCol)
            pq.put(Node(nextRow, nextCol, currentNode, cost))
