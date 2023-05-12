import pygame
from checkers.constants import *
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_pos_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, column = get_pos_mouse(pos)
                piece = board.get_piece(row, column)
                board.move(piece, 4, 3)

        game.update()

    pygame.quit()


main()
