from .constants import *
import pygame

class Pieces:
    PAD = 7
    OUT = 2

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.position()

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

    def position(self):
        self.x = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PAD
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUT)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
