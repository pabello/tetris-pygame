from grid import Grid
from blocks import *
from copy import deepcopy
from os import path
import random
import pygame

class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), TBlock(), OBlock(), IBlock(), SBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

        base_dir = path.dirname(__file__)
        self.block_place_sound = pygame.mixer.Sound(path.join(base_dir, "roblox_oof.mp3"))
        self.clear_rows_sound = pygame.mixer.Sound(path.join(base_dir, "anime_wow.mp3"))
        self.game_over_sound = pygame.mixer.Sound(path.join(base_dir, "you_lost.mp3"))

        self.clear_rows_sound.set_volume(.3)
        self.block_place_sound.set_volume(.35)
        self.game_over_sound.set_volume(.9)

    def get_random_block(self) -> Block:
        return deepcopy(random.choice(self.blocks))
    
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or self.collides_with_other():
            self.current_block.move(0, 1)
    
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or self.collides_with_other():
            self.current_block.move(0, -1)
    
    def move_down(self) -> bool:
        self.current_block.move(1, 0)
        if not self.block_inside() or self.collides_with_other():
            self.current_block.move(-1, 0)
            self.lock_block()
            return False
        return True

    def collides_with_other(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.collides_with_other(tile):
                return True
        return False

    def lock_block(self):
        self.block_place_sound.play()
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            self.grid.update_cell(tile, self.current_block.block_type)
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_rows_sound.play()
            self.update_score(rows_cleared)
        if self.collides_with_other():
            self.game_over = True
            self.game_over_sound.play()

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside():
            self.current_block.undo_rotation()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True
    
    def update_score(self, lines_cleared):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 600
        elif lines_cleared == 4:
            self.score += 1000

    def add_point(self):
        self.score += 1
    
    def draw(self, screen:pygame.Surface):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.block_type == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.block_type == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

    def reset(self):
        self.grid.reset()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0