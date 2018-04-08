class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.players_turn = players[0]

    def start(self):
        while True:
            input_val = int(input('please enter x value: '))
            self.board.add_piece(self.players_turn, input_val)
            self.board.display()
            self.players_turn = self.players[0] if self.players_turn == self.players[1] else self.players[1]