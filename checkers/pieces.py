from .constants import *
import pygame


class Pieces:
    PAD = 15
    OUT = 2

    def __init__(self, row: int, column: int, color) -> None:
        """
        Initialize the piece object.
        :param: row (int): The row position of the piece.
        :param: column (int): The column position of the piece.
        :param color: The RGB value of the piece color.
        """
        self.row = row
        self.column = column
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.position()

    def position(self) -> None:
        """
        Calculate the x and y position of the piece based
        on its row and column positions.
        """
        self.x = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self) -> None:
        """
        Make the piece a king.
        """
        self.king = True

    def draw(self, win: pygame.Surface) -> None:
        """
        Draw the piece on the board.
        :param: win (pygame.Surface): The surface to draw the piece on.
        """
        radius = SQUARE_SIZE//2 - self.PAD
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUT)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        # Adds crown image and makes it centered on piece
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row: int, column: int) -> None:
        """
        Move the piece to the given row and column positions.
        :param: row (int): The row position to move the piece to.
        :param: column (int): The column position to move the piece to.
        """
        self.row = row
        self.column = column
        self.position()
