from grid import Grid
from blocks import Block
import constants
import random
import pygame

class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = [2]
        self.game_over = False
        self.score = 0


        base_dir = path.dirname(__file__)
        sounds_dir = path.join(base_dir, "assets", "sounds")
        self.block_place_sound = pygame.mixer.Sound(path.join(sounds_dir, "roblox_oof.mp3"))
        self.clear_rows_sound = pygame.mixer.Sound(path.join(sounds_dir, "anime_wow.mp3"))
        self.game_over_sound = pygame.mixer.Sound(path.join(sounds_dir, "you_lost.mp3"))

        self.clear_rows_sound.set_volume(.3)
        self.block_place_sound.set_volume(.35)
        self.game_over_sound.set_volume(.9)

    def get_random_block(self) -> Block:
        return Block(random.choice(self.blocks))
    
    def place_block_at_random(self, block:Block):
        available_slots = self.grid.get_available_slots()
        slot = random.choice(available_slots)
        self.grid.update_cell(slot, block)
    
    def move_left(self):
        if self.grid.move_left():
            self.add_block()
    
    def move_right(self):
        if self.grid.move_right():
            self.add_block()
    
    def move_up(self):
        if self.grid.move_up():
            self.add_block()

    def move_down(self):
        if self.grid.move_down():
            self.add_block()

    # def collides_with_other(self):
    #     tiles = self.current_block.get_cell_positions()
    #     for tile in tiles:
    #         if self.grid.collides_with_other(tile):
    #             return True
    #     return False

    def add_point(self):
        self.score += 1
    
    def draw(self, screen:pygame.Surface):
        self.grid.draw(screen)

    def add_block(self):
        self.place_block_at_random(self.get_random_block())

    def reset(self):
        self.score = 0
        self.grid.reset()
        self.start()
