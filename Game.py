class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players

    def start(self):
        input_val = input('please enter x value: ')
        self.board.display()