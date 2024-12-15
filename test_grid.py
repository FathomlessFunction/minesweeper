import pytest

from grid import MinesweeperGrid

@pytest.fixture(scope='session')  # one server to rule'em all
def grid():
    grid = MinesweeperGrid(5, 5)
    grid.addBomb(1, 1)
    return grid

@pytest.fixture(scope='session')  # one server to rule'em all
def emptyGrid():
    emptyGrid = MinesweeperGrid(5, 5)
    return emptyGrid

# game logic tests
def test_if_player_clicks_on_a_bomb_game_should_end(grid):
    grid.click(1, 1)
    assert grid.gameOver is True

def test_if_player_does_not_click_on_bomb_game_should_continue(emptyGrid):
    emptyGrid.click(1, 1)
    assert grid.gameOver is False

# cell logic tests
def test_if_player_clicks_on_clear_space_should_be_revealed(emptyGrid):
    emptyGrid.click(1, 1)
    cell = emptyGrid.getCell(1, 1)
    assert cell.visible is True

def test_if_player_clicks_on_cell_should_show_number_of_adjacent_bombs(grid):
    grid.click(2, 1)
    cell = grid.getCell(2, 1)
    assert cell.adjacent == 1

def test_cell_should_show_diagonally_adjacent_bombs(grid):
    cell = grid.getCell(2, 2)
    assert cell.adjacent == 1
