# http://pygametutorials.wikidot.com/tutorials-basic

import pygame
from pygame.locals import *

from grid import MinesweeperGrid

# TODO: display the number of remaining clear cells left

# pixel width/height for draing to the game screen
CELL_WIDTH = 25
CELL_HEIGHT = 25

GRID_OFFSET_X = 25
GRID_OFFSET_Y = 50
 
class App:

    def __init__(self):
        self._running = True
        self._display = None
        self.size = self.width, self.height = 640, 400
        self._grid = None
        self._exit_on_click = False
        self.won = False
 
    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        # if quitting
        if event.type == pygame.QUIT:
            self._running = False
        
        # if clicking
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self._exit_on_click:
                self._running = False

            ## if mouse is pressed get position of cursor
            pos = pygame.mouse.get_pos()

            ## check if cursor is on any of our grid rectangles
            for x in range(self._grid.width):
                for y in range(self._grid.height):
                    cell = self._grid.getCell(x, y)
                    if cell.rect.collidepoint(pos):
                        cell.setColour((144, 245, 66))
                        self._grid.click(x, y)
            
    def on_loop(self):
        pass

    def on_render(self):
        self.draw_grid()
        pygame.display.flip()
        pass

    def draw_grid(self):
        # draws the minesweeper grid to the screen
        font = pygame.font.Font(None, 36)

        # if the game is over, print "game over" at the top
        if self._grid.gameOver:
            # TODO: different message if victory
            if self._grid.winner:
                text_surface = font.render("YOU WON!", True, (144, 245, 66))
            else:
                text_surface = font.render("GAME OVER", True, (225, 45, 45))
            text_rect = text_surface.get_rect(center = (GRID_OFFSET_X + (self._grid.width * CELL_WIDTH // 2), GRID_OFFSET_Y // 2))
            self._display.blit(text_surface, text_rect)
            self._exit_on_click = True

        # loop through each cell in the minsweeper grid
        for y in range(self._grid.getHeight()):
            for x in range(self._grid.getWidth()):
                cell = self._grid.getCell(x, y)
                # draw a single cell
                surface = font.render(cell.getChar(), True, cell.colour)
                cell_rect = surface.get_rect(topleft = (x * CELL_WIDTH + GRID_OFFSET_X, y * CELL_HEIGHT + GRID_OFFSET_Y))
                cell.setRect(cell_rect)
                self._display.blit(surface, cell_rect)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    
    def add_grid(self, grid):
        # add the minesweeper grid
        self._grid = grid
 
if __name__ == "__main__" :
    theApp = App()
    minesweeperGrid = MinesweeperGrid(8, 8)
    minesweeperGrid.addRandomBomb(10)
    theApp.add_grid(minesweeperGrid)

    theApp.on_execute()
