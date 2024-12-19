import re
import random

class Cell:
    # a cell in the minesweeper grid. May contain a bomb.
    def __init__(self):
        self.visible = False
        #self.visible = False
        self.adjacentCells = []
        self.isBomb = False

        # for storing a refence to the pygame Rectangle (used to draw & detect mouse clicks)
        self.rect = None 
        self.colour = (255, 255, 255)

    def setRect(self, rect):
        self.rect = rect

    def setColour(self, colour):
        self.colour = colour

    def setBomb(self):
        self.isBomb = True

    def adjacentBombs(self):
        # returns the number of adjacent cells that are Bombs
        count = 0
        for cell in self.adjacentCells:
            if cell.isBomb:
                count += 1
        return count

    def getChar(self):
        if self.visible:
            if self.isBomb:
                self.colour = (225, 45, 45)
                return 'X'
                #return '💣'
            else:
                return chr(48+self.adjacentBombs())
        else:
            return '_'
            # return '■'
        
    def reveal(self, depth):
        self.visible = True
        if depth > 1:
            return
        if self.adjacentBombs() <=1:
            for cell in self.adjacentCells:
                if cell.adjacentBombs() <= 1 - depth:
                    if not cell.isBomb:
                        cell.reveal(1+depth)

class MinesweeperGrid:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.cells = [[Cell() for x in range(w)] for y in range(h)]
        self._linkCells()
        
        # true if the player has lost
        self.gameOver = False
        self.won = False

    def _linkCells(self):
        # loops through each cell in the grid & informs each cell of adjacent units
        for y in range(self.height):
            for x in range(self.width):

                currentCell = self.getCell(x, y)

                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        # if within bounds of the grid
                        if i >= 0 and j >= 0 and i < self.width and j < self.height:
                            
                            adjacentCell = self.getCell(i, j)

                            # if its the same cell, skip
                            if currentCell == adjacentCell:
                                continue
                            else:
                                currentCell.adjacentCells.append(adjacentCell)

    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width

    def getCells(self):
        return self.cells
    
    def revealBombs(self):
        # reveals all cells - used on game over
        for y in range(self.height):
            for x in range(self.width):
                currentCell = self.getCell(x, y)
                if currentCell.isBomb:
                    currentCell.visible = True

    def getCell(self, x, y):
        return self.cells[x][y]

    def addBomb(self, x, y):
        # adds a bomb at coordinate (x, y)
        self.getCell(x, y).setBomb()

    def click(self, x, y):
        # clicks at coordinates (x, y), revealing the tile
        # returns true if the player has won
        cell = self.getCell(x, y)
        cell.reveal(0)
        if cell.isBomb:
            self.gameOver = True
            self.winner = False
            self.revealBombs()
            return False

        for y in range(self.height):
            for x in range(self.width):
                # all non-bomb cells must be visible for the player to win
                if (not self.getCell(x, y).visible) and (not self.getCell(x,y).isBomb):
                    self.winner = False
                    return False
        # if we have reached here without returning, all non bomb cells are visible
        self.winner = True
        self.gameOver = True
        return True

    def stringOutput(self):
        toPrint = ""
        for y in range(self.height):
            for x in range(self.width):
                toPrint += str(self.getCell(x, y).getChar())
            toPrint += "\n"
        return toPrint

    def print(self):
        # prints the game grid
        print(self.stringOutput())

    def addRandomBomb(self, count):
        for i in range(count):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            self.addBomb(x, y)

if __name__ == "__main__":
    grid = MinesweeperGrid(5, 5)

    grid.addRandomBomb(7)

    grid.print()

    print("Enter co-ordinates to check in the format 'X, Y':")

    while grid.gameOver is False:
        playerSelection = input("enter co-ordinates: ('exit' to quit)\n")
        if playerSelection.lower() == 'exit':
            break

        # check that user input matches what we expect:
        if re.match("\s*\d+\s*[,]\s*\d+", playerSelection):
            x, y = playerSelection.split(',')
            x = int(x.strip())
            y = int(y.strip())

            if 0 <= x <= grid.width and 0 <= y <= grid.height:
                # (1, 1) of user input == (0, 0) of grid input
                # hence the -1
                won = grid.click(x-1, y-1)

                grid.print()

                if won:
                    print("You won!")

        else:
            print("Invalid input. Enter 2 numbers, seperated by a comma")
    
    print("game over")