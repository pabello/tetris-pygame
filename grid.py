from constants import *
from blocks import Block
from colors import Colors
from position import Position
import pygame


class Grid:
    def __init__(self):
        self.width = GRID_WIDTH_HEIGHT
        self.height = GRID_WIDTH_HEIGHT

        self.row_number = GRID_SIZE_XY
        self.col_number = GRID_SIZE_XY

        self.grid = [[None for j in range(self.col_number)] for i in range(self.row_number)]

    def get_available_slots(self):
        empty_slots = []
        for i in range(self.row_number):
            for j in range(self.col_number):
                if self.grid[i][j] is None: empty_slots.append(Position(i, j))
        return empty_slots

    def update_cell(self, cell:Position, block:Block):
        self.grid[cell.row][cell.column] = block

    def place_block(self, block, cell):
        self.update_cell(cell, block)
    
    def draw(self, surface):
        for row in range(self.row_number):
            for col in range(self.col_number):
                cell_item = self.grid[row][col]
                # cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * CELL_SIZE +11, row * CELL_SIZE +11, CELL_SIZE-1, CELL_SIZE-1)
                # pygame.draw.rect(surface, Colors.get_colors()[cell_value], cell_rect)
                pygame.draw.rect(surface, Colors.get_colors()[0], cell_rect)
                if type(cell_item) is Block:
                    cell_item.draw(surface, row, col, GRID_OFFSET_X, GRID_OFFSET_Y)

    def reset(self):
        for row in range(self.row_number):
            for column in range(self.col_number):
                self.grid[row][column] = None


    def move_left(self) -> bool:
        made_a_move = False
        for i, row in enumerate(self.grid):
            blocks = [block for block in row if block is not None]
            merge_check_id = 1
            while len(blocks) > merge_check_id:
                if blocks[merge_check_id -1].block_value == blocks[merge_check_id].block_value:
                    blocks[merge_check_id -1].block_value *= 2
                    blocks[merge_check_id] = None
                    merge_check_id += 1
                merge_check_id += 1
            
            while None in blocks:
                blocks.remove(None)

            new_row = blocks + [None]*(self.col_number-len(blocks))
            if new_row != self.grid[i]:
                self.grid[i] = new_row
                made_a_move = True

        return made_a_move
            
    
    def move_right(self) -> bool:
        made_a_move = False
        for i, _ in enumerate(self.grid):
            blocks:list[Block] = [block for block in _ if block is not None]
            curr_block_id:int = len(blocks)-2  # starting with last but one block to see if can be merged with the last one
            while curr_block_id >= 0:
                curr_block_value:int = blocks[curr_block_id].block_value
                right_block_value:int = blocks[curr_block_id+1].block_value
                if curr_block_value == right_block_value:
                    # move the block to the right, then merge
                    blocks[curr_block_id+1].block_value *= 2
                    blocks[curr_block_id] = None
                    curr_block_id -= 1  # skip next block; can't merge with None
                curr_block_id -= 1

            while None in blocks:
                blocks.remove(None)

            new_row = [None]*(self.col_number-len(blocks)) + blocks
            if new_row != self.grid[i]:
                self.grid[i] = new_row
                made_a_move = True

        return made_a_move
    
    
    def move_up(self) -> bool:
        made_a_move = False
        for c in range(len(self.grid[0])):
            blocks:list[Block] = []
            for r in range(len(self.grid)):
                block:Block = self.grid[r][c]
                if block is not None:
                    blocks.append(block)
            curr_block_id = 1
            while curr_block_id < len(blocks):
                curr_block_value:int = blocks[curr_block_id].block_value
                prev_block_value:int = blocks[curr_block_id-1].block_value
                if curr_block_value == prev_block_value:
                    blocks[curr_block_id-1].block_value *= 2
                    blocks[curr_block_id] = None
                    curr_block_id += 1  # skip one block - can't merge with None
                curr_block_id += 1
            
            while None in blocks:
                blocks.remove(None)

            new_column = blocks + [None]*(self.row_number-len(blocks))
            for r in range(len(self.grid)):
                if new_column[r] != self.grid[r][c]:
                    self.grid[r][c] = new_column[r]
                    made_a_move = True

        return made_a_move
    
    def move_down(self) -> bool:
        made_a_move = False
        for c in range(len(self.grid[0])):
            blocks:list[Block] = []
            for r in range(len(self.grid)):
                block:Block = self.grid[r][c]
                if block is not None:
                    blocks.append(block)
            curr_block_id = len(blocks) - 2  # skip last one
            while curr_block_id >= 0:
                curr_block_value = blocks[curr_block_id].block_value
                next_block_value = blocks[curr_block_id+1].block_value
                if curr_block_value == next_block_value:
                    blocks[curr_block_id+1].block_value *= 2
                    blocks[curr_block_id] = None
                    curr_block_id -= 1
                curr_block_id -= 1
            
            while None in blocks:
                blocks.remove(None)
            
            new_column = [None]*(self.row_number-len(blocks)) + blocks
            for r in range(len(self.grid)):
                if new_column[r] != self.grid[r][c]:
                    self.grid[r][c] = new_column[r]
                    made_a_move = True                    

        return made_a_move
