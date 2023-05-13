from .constants import *
from .pieces import Pieces


class Board:
    def __init__(self) -> None:
        """
        Initializes the Board class with the board state and player information.
        """
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def squares(self, win: pygame.Surface) -> None:
        """
        Draws the red and black checkerboard squares on the screen.
        :param: win (pygame.Surface): The surface to draw on.
        """
        try:
            win.fill(BLACK)
            for row in range(ROWS):
                for col in range(row % 2, ROWS, 2):
                    pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        except ValueError as e:
            print(f"Error occurred in squares(): {e}")

    def move(self, piece, row: int, column: int) -> None:
        """
        Moves a checker piece on the board.
        :param: piece (Pieces): The checker piece to move.
        :param: row (int): The row to move the piece to.
        :param: column (int): The column to move the piece to.
        :return:
        """
        # Swamps values by reversing
        try:
            self.board[piece.row][piece.column], self.board[row][column] = \
                self.board[row][column], self.board[piece.row][piece.column]
            piece.move(row, column)

            if row == ROWS - 1 or row == 0:
                piece.make_king()
                if piece.color == WHITE:
                    self.white_kings += 1
                else:
                    self.red_kings += 1
        except ValueError as e:
            print(f"Error occurred in move(): {e}")

    def get_piece(self, row: int, column: int):
        return self.board[row][column]

    def create_board(self) -> None:
        """
        Creates the initial state of the checkerboard.
        """
        try:
            for row in range(ROWS):
                self.board.append([])
                for col in range(COLUMNS):
                    # Determines where to place checker pieces
                    if col % 2 == ((row + 1) % 2):
                        if row < 3:
                            self.board[row].append(Pieces(row, col, WHITE))
                        elif row > 4:
                            self.board[row].append(Pieces(row, col, RED))
                        else:
                            self.board[row].append(0)
                    else:
                        self.board[row].append(0)
        except ValueError as e:
            print(f"Error occurred in draw(): {e}")

    def draw(self, win: pygame.Surface) -> None:
        """
        Draws the checkerboard and pieces on the screen.
        :param: win (pygame.Surface): The surface to draw on.
        """
        try:
            self.squares(win)
            for row in range(ROWS):
                for col in range(COLUMNS):
                    pieces = self.board[row][col]
                    if pieces != 0:
                        pieces.draw(win)
        except ValueError as e:
            print(f"Error occurred in draw(): {e}")

    def remove(self, pieces) -> None:
        """
        Removes the checker pieces from the board
        """
        try:
            for piece in pieces:
                self.board[piece.row][piece.column] = 0
                if piece != 0:
                    if piece.color == RED:
                        self.red_left -= 1
                    else:
                        self.white_left -= 1
        except ValueError as e:
            print(f"Error occurred in remove(): {e}")

    def winner(self) -> None:
        """
        Returns the color of the winner player.
        """

        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED

        return None

    def get_valid_moves(self, piece):
        """
        Returns a dictionary of all valid moves for the given piece, with the keys being the coordinates of the
        destination squares and the values being lists of the pieces that were skipped over to get there.
        """
        moves = {}
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._move_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._move_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._move_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._move_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _move_left(self, start: int, stop: int, step: int, color: str, left: int, skipped=[]):
        """
        Returns a dictionary of all valid moves that can be made by moving a piece to the left, with the keys being the
        coordinates of the destination squares and the values being lists of the pieces that were skipped over to get there.
        """
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._move_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._move_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1

        return moves

    def _move_right(self, start: int, stop: int, step: int, color: str, right: int, skipped=[]):
        """
        Returns a dictionary of all valid moves that can be made by moving a piece to the right, with the keys being the
        coordinates of the destination squares and the values being lists of the pieces that were skipped over to get there.
        """
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._move_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._move_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1

        return moves
