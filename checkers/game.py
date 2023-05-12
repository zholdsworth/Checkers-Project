import pygame
from .constants import *
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid = {}

    def reset(self):
        self._init()

    def select(self, row, column):
        if self.selected:
            result = self._move(row, column)
            if not result:
                self.selected = None
                self.select(row, column)

    def _move(self, row, column):