class Cell:
    def __init__(self):
        pass

class MinesweeperGrid:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.grid = [[0 for x in range(w)] for y in range(h)] 
        
        # true if the player has lost
        self.gameOver = False

    def addBomb(self, x, y):
        # adds a bomb at coordinate (x, y)
        pass

    def click(self, x, y):
        # clicks at coordinates (x, y), revealing the tile
        # returns true if the player has lost
        pass

    def GameOver(self):
        return self.gameOver

    def stringOutput(self):
        toPrint = ""
        for y in range(self.height):
            for x in range(self.width):
                toPrint += str(self.grid[x][y])
            toPrint += "\n"
        return toPrint

    def print(self):
        # prints the game grid
        print(self.stringOutput())

if __name__ == "__main__":
    print("Hello world!")

    grid = Grid(5, 5)
    grid.print()
