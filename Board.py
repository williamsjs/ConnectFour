class Board:

    def display():
        for x in range(1, 7):
            for y in range(1, 8):
                print('|0|', end="")
            print()
        print(' ', end="")
        print('-' * 19)

board = Board
board.display()