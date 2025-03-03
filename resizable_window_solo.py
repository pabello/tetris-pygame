import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Resizable Pygame Window")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update the screen size when the window is resized
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # Fill the screen with a color
    screen.fill((0, 0, 0))  # Fill with black

    # Draw something (e.g., a rectangle)
    pygame.draw.rect(screen, (255, 0, 0), (width // 4, height // 4, width // 2, height // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()