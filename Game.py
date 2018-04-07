class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players

    def start(self):
        input_val = int(input('please enter x value: '))
        self.board.add_piece(self.players[0], input_val)
        self.board.display()