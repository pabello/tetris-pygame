from __future__ import annotations

from constants import CELL_SIZE

import pygame

pygame.init()

number_font = pygame.font.Font(None, 30)
class Block:
    def __init__(self, block_value) -> None:
        self.block_value = block_value
        self.cell_size = CELL_SIZE

    def draw(self, screen:pygame.Surface, row, column, offset_x, offset_y):
        left = column*CELL_SIZE + offset_x
        top = row*CELL_SIZE + offset_y
        tile_rect = pygame.Rect(left, top, CELL_SIZE-1, CELL_SIZE-1)
        pygame.draw.rect(screen, colors[self.block_value], tile_rect)
        screen.blit(number_font.render(str(self.block_value), True, (255, 255, 255)), (left, top))


colors = {
    2: "#0C93FA",
    4: "#5A9CAB",
    8: "#A9A45C",
    16: "#F7AD0D",
    32: "#E4775C",
    64: "#D242AB",
    128: "#BF0CFA",
    256: "#D20CAB",
    512: "#E40C5B",
    1024: "#B50D68",
    2048: "#850E75",
}
