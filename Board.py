import Piece as p

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spots = self.__build_board()

    def display(self):
        print()
        for x in range(1, self.width + 1):
            print(' ', end="")
            print(str(x) + ' ', end="")
        print('\n')

        for x in self.spots[::-1]:
            for y in x:
                disp = y.display if isinstance(y, p.Piece) else '|O|'
                print(disp, end="")
            print()
        print(' ', end="")
        print('-' * 19)

    def add_piece(self, player, y):
        piece = p.Piece(player)

        for i, row in enumerate(self.spots):
            if row[y-1] == 'O':
                self.__place_piece(piece, i, y - 1)
                return True
        print('spaces filled :/.  Please select another column')
        return False

    def __build_board(self):
        board = []
        for x in range(0, self.height):
            board.append([])
            for y in range(0, self.width):
                board[x].append('O')
        return board

    def __place_piece(self, piece, x, y):
        piece.x = x
        piece.y = y
        print('x: ', x, 'y: ', y)
        self.spots[x][y] = piece
        print(self.spots)
