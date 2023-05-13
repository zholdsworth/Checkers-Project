from checkers.constants import *
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_pos_mouse(pos):
    """
    Returns the row and column of a square on the board based on the
    position of the mouse click.
    """
    x, y = pos
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column


def main() -> None:
    """
    The main function that runs the game loop.
    """
    try:
        run = True
        clock = pygame.time.Clock()
        game = Game(WIN)

        while run:
            clock.tick(FPS)

            #if game.winner() != None:
                #print(game.winner())
                #run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, column = get_pos_mouse(pos)

                    game.select(row, column)

            game.update()

        pygame.quit()

    except pygame.error as e:
        print(f"An error has occured: {e}")
        pygame.quit()


main()
