class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rows = self.__build_board()

    def display(self):
        print()
        for x in range(1, self.width + 1):
            print(' ', end="")
            print(str(x) + ' ', end="")
        print()

        for x in self.rows[::-1]:
            for y in x:
                print("|" + y + "|", end="")
            print()
        print(' ', end="")
        print('-' * 19)

    def add_piece(self, player, y):
        for row in self.rows:
            if row[y-1] == 'O':
                row[y-1] = player.color
                self.__check_score(player)
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
    
    def __check_score(self, player):
        for c in range(self.width - 3):
            for r in range(self.height):
                if self.rows[r][c] == player.color and self.rows[r][c+1] == player.color and self.rows[r][c+2] == player.color and self.rows[r][c+3] == player.color:
                    print(f"{player.name} wins Across!!!")
                    exit()

        for c in range(self.width):
            for r in range(self.height - 3):
                if self.rows[r][c] == player.color and self.rows[r+1][c] == player.color and self.rows[r+2][c] == player.color and self.rows[r+3][c] == player.color:
                    print(f"{player.name} wins Vertically!!!")
                    exit()

        for c in range(self.width - 3):
            for r in range(self.height - 3):
                if self.rows[r][c] == player.color and self.rows[r+1][c+1] == player.color and self.rows[r+2][c+2] == player.color and self.rows[r+3][c+3] == player.color:
                    print(f"{player.name} wins Diagonally!!!")
                    exit()

        for c in range(self.width - 3):
            for r in range(3, self.height):
                if self.rows[r][c] == player.color and self.rows[r-1][c+1] == player.color and self.rows[r-2][c+2] == player.color and self.rows[r-3][c+3] == player.color:
                    print(f"{player.name} wins Diagonally!!!")
                    exit()