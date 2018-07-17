import pygame

pygame.init()

display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('2048 Python')
clock = pygame.time.Clock()

pygame.quit()
quit()
