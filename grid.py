from constants import *
from colors import Colors
from position import Position
import pygame


class Grid:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT

        self.row_number = GRID_HEIGHT // CELL_SIZE
        self.col_number = GRID_WIDTH // CELL_SIZE

        self.grid = [[0 for i in range(self.col_number)] for i in range(self.row_number)]

    def update_cell(self, tile:Position, value):
        self.grid[tile.row][tile.column] = value

    def is_inside(self, row, column):
        if row >=0 and row < self.row_number and column >= 0 and column < self.col_number:
            return True
        return False
    
    def collides_with_other(self, tile:Position):
        if self.grid[tile.row][tile.column] != 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.col_number):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.col_number):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for column in range(self.col_number):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.row_number-1, 0, -1):
            if self.is_row_full(row):
                completed += 1
                self.clear_row(row)
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def draw(self, surface):
        for row in range(self.row_number):
            for col in range(self.col_number):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * CELL_SIZE +11, row * CELL_SIZE +11, CELL_SIZE-1, CELL_SIZE-1)
                pygame.draw.rect(surface, Colors.get_colors()[cell_value], cell_rect)

    def reset(self):
        for row in range(self.row_number):
            for column in range(self.col_number):
                self.grid[row][column] = 0 