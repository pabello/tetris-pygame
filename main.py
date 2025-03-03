import pygame, sys
from constants import *
from colors import Colors
from game import Game

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white.value)
next_surface = title_font.render("Next", True, Colors.white.value)
game_over_surface = title_font.render("Game over!", True, Colors.white.value)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

game = Game()
game.add_block()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)
pygame.display.set_caption("Pygame 2048")
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not game.game_over:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    game.move_left()
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    game.move_right()
                if event.key in [pygame.K_UP, pygame.K_w]:
                    game.move_up()
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    game.move_down()
            elif event.key in [pygame.K_RETURN, pygame.K_r, pygame.K_SPACE]:
                game.game_over = False
                game.reset()

    score_value_surface = title_font.render(str(game.score), True, Colors.white.value)

    screen.fill(Colors.dark_blue.value)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue.value, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue.value, next_rect, 0, 10)

    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                                                                  centery = score_rect.centery))
    
    if game.game_over:
        screen.blit(game_over_surface, (328, 450, 50, 50))
    
    game.draw(screen)

    pygame.display.update()
    clock.tick(FRAME_RATE)
