from __future__ import annotations

from constants import CELL_SIZE
from colors import Colors
from position import Position
from grid import Grid
from copy import deepcopy

import pygame

class Block:
    def __init__(self, block_type) -> None:
        self.block_type = block_type
        self.cells = {}
        self.cell_size = CELL_SIZE
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.rotation_states_count = 4 if block_type != 4 else 1
        self.color = Colors.get_colors()[block_type]

    def draw(self, screen:pygame.Surface, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column*CELL_SIZE + offset_x, tile.row*CELL_SIZE + offset_y, CELL_SIZE-1, CELL_SIZE-1)
            pygame.draw.rect(screen, Colors.get_colors()[self.block_type], tile_rect)

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def rotate(self):
        self.rotation_state = (self.rotation_state + 1) % self.rotation_states_count

    def undo_rotation(self):
        self.rotation_state = (self.rotation_state - 1) % self.rotation_states_count

    def get_cell_positions(self) -> list[Position]:
        tiles = self.cells[0][self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles 
    
    def __deepcopy__(self, memo:Block):
        new_instance = Block(
            deepcopy(self.block_type, memo),
        )
        new_instance.cells = deepcopy(self.cells, memo),
        new_instance.row_offset = self.row_offset
        new_instance.column_offset = self.column_offset
        return new_instance


class LBlock(Block):
    def __init__(self) -> None:
        super().__init__(block_type = 1)
        self.cells = {
            0: (Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)),
            1: (Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)),
            2: (Position(2, 0), Position(1, 0), Position(1, 1), Position(1, 2)),
            3: (Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)),
        }
        self.move(0, 3)

class JBlock(Block):
    def __init__(self):
        super().__init__(block_type = 2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)

class IBlock(Block):
    def __init__(self):
        super().__init__(block_type = 3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)

class OBlock(Block):
    def __init__(self):
        super().__init__(block_type = 4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)

class SBlock(Block):
    def __init__(self):
        super().__init__(block_type = 5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class TBlock(Block):
    def __init__(self):
        super().__init__(block_type = 6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(block_type = 7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)