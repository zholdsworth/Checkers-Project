import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board


class Game:
    def __init__(self, win: pygame.Surface) -> None:
        """
        Initalize the game.
        Args: win (pygame.Surface): The Pygame display surface.
        """
        try:
            self._init()
            self.win = win
        except ValueError as e:
            print("Error initializing game: {e}")

    def update(self) -> None:
        """
        Update the game display.
        """
        try:
            self.board.draw(self.win)
            self.draw_valid_moves(self.valid)
            pygame.display.update()
        except pygame.error as e:
            print(f"Error updating game: {e}")

    def _init(self) -> None:
        try:
            self.selected = None
            self.board = Board()
            self.turn = RED
            self.valid = {}
        except ValueError as e:
            print(f"Error initializing game: {e}")

    def winner(self):
        try:
            return self.board.winner
        except ValueError as e:
            print(f"Error getting winner: {e}")

    def reset(self) -> None:
        """
        Reset the game to its initial state.
        """
        try:
            self._init()
        except ValueError as e:
            print(f"Error resetting game: {e}")

    def select(self, row: int, column: int) -> bool:
        """
        Select a piece on the game board.
        :param row: The row of the selected piece.
        :param column: The column of the selected piece.
        :return: bool: True if a piece was selected, False otherwise.
        """
        # If able to move there, piece will move. If not, piece will be unselected
        try:
            if self.selected:
                result = self._move(row, column)
                if not result:
                    self.selected = None
                    self.select(row, column)
            # If move is valid, return true. Else, return false.
            piece = self.board.get_piece(row, column)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid = self.board.get_valid_moves(piece)
                return True
            return False

        except ValueError as e:
            print(f"Error selecting piece: {e}")
            return False

    def _move(self, row: int, column: int) -> bool:
        """
        Move a piece on the game board.
        :param row: The row to move the piece to.
        :param column: The column to move the piece to.
        :return: bool: True if the piece was moved, False otherwise.
        """
        # Moving selected piece to spot selected if no other piece is already there
        try:
            piece = self.board.get_piece(row, column)
            if self.selected and piece == 0 and (row, column) in self.valid:
                self.board.move(self.selected, row, column)
                skipped = self.valid[(row, column)]
                if skipped:
                    self.board.remove(skipped)
                self.change_turn()
            else:
                return False

            return True

        except ValueError as e:
            print(f"Error moving piece: {e}")
            return False

    def draw_valid_moves(self, moves) -> None:
        """
        Draw the valid moves on the game board.
        :param: moves (dict): A dictionary containing the valid moves for the selected piece.
        """
        try:
            for move in moves:
                row, column = move
                pygame.draw.circle(self.win, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
        except pygame.error as e:
            print(f"Error drawing valid moves: {e}")

    def change_turn(self) -> None:
        # Changes moves back and forth
        try:
            self.valid = {}
            if self.turn == RED:
                self.turn = WHITE
            else:
                self.turn = RED
        except ValueError as e:
            print(f"Error changing turn: {e}")
