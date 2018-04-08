class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.__build_board()

    def display(self):
        print()
        for x in range(1, self.width + 1):
            print(' ', end="")
            print(str(x) + ' ', end="")
        print('\n')

        for x in range(0, self.height):
            for y in range(0, self.width):
                print('|' + self.board[x][y] + '|', end="")
            print()
        print(' ', end="")
        print('-' * 19)

    def add_piece(self, player, x):
        color = 'X' if player.player_one else 'Y'

        for i in range(-1, -self.width, -1):
            if self.board[i][x-1] == 'O':
                self.board[i][x-1] = color
                self.__check_score()
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

    def __check_score(self):

