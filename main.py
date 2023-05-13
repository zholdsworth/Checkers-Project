from checkers.constants import *
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_pos_mouse(pos: tuple[int, int]) -> tuple[int, int]:
    """
    Returns the row and columns of a square on the board on the
    position of the mouse click.
    :param: pos (tuple[int, int]): The position of the mouse click.
    :return: tuple[int, int]: The row and column of the square on the board.
    """
    x, y = pos
    row: int = -1
    column: int = -1
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column


def main() -> None:
    """
    The main function that runs the game loop.
    """
    try:
        run: bool = True
        clock: pygame.time.Clock = pygame.time.Clock()
        game: Game = Game(WIN)

        while run:
            clock.tick(FPS)
        # Broke everything
        # if game.winner() != None:
            # print(game.winner())
            # run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos: tuple[int, int] = pygame.mouse.get_pos()
                    row: int
                    column: int
                    row, column = get_pos_mouse(pos)
                    game.select(row, column)

            game.update()
    except pygame.error as e:
        print(f"A Pygame error occurred: {e}")
    except ValueError as e:
        print(f"A ValueError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
