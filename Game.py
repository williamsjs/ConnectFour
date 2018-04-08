class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.players_turn = players[0]

    def start(self):
        while True:
            input_val = int(input('please enter x value: '))
            piece_placed = self.board.add_piece(self.players_turn, input_val)
            self.board.display()

            if piece_placed:
                self.players_turn = list(filter((lambda p: p != self.players_turn), self.players))[0]
