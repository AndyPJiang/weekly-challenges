# week4
from collections import defaultdict


class LargestSumRectangle:
    def __init__(self, grid: list):
        self.grid = grid
        self.rows = len(grid)

    # pre-compute row sums starting at every index ( 0(n^2) size )
    def getRowSums(self) -> dict:
        grid = self.grid
        rows = self.rows
        sums = defaultdict(int)

        for i in range(rows):
            s = 0
            for j in range(len(grid[i])):
                try:
                    s += grid[i][j]
                    sums[(i,j)] = s
                except:
                    s = 0
        return sums

    # returns a tuple of pairs of indicies, the first pair representing the index of left top corner of the rectangle
    #  and the second pair representing the index of right bottom corner of the rectangle. 
    # algorithm runs in 0(n^3). 
    def findLargestRectangle(self) -> tuple:
        grid = self.grid
        if len(grid) == 0:
            return ()

        rowSums = self.getRowSums()
        largestRectSize = 0
        largestInds = ((0,0), (0,0))
        for i in range(self.rows):
            for j in range(len(grid[i])-1, -1, -1):
                size, rightBottom = self.getSize(rowSums, i, j)
                if largestRectSize < size:
                    largestRectSize = size
                    largestInds = ((i,0),rightBottom)

                # if already reached a rectange that spans every row, no need to keep looking at the current row
                if rightBottom[0] >= self.rows-1:
                    break
        
        return largestInds

    # given a starting row and a width that the rectange must be, cmopute the rectangle with the largest sum                
    def getSize(self, rowSums: dict, row: int, col: int) -> tuple:
        grid = self.grid
        rightBottom = ()
        size = 0
        while row < self.rows and len(grid[row]) > col :
            size += rowSums[(row,col)]
            row+=1

        rightBottom = (row-1,col)
        return (size, rightBottom)

