from .constants import *
import pygame


class Pieces:
    PAD = 15
    OUT = 2

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        self.x = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PAD
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUT)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        # Adds crown image and makes it centered on piece
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, column):
        self.row = row
        self.column = column
        self.position()
