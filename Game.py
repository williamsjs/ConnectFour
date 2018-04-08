class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.players_turn = players[0]

    def start(self):
        self.__display_board()

        while True:
            input_val = int(input(f"{self.players_turn.name}, please enter Y value: "))
            piece_placed = self.board.add_piece(self.players_turn, input_val)

            self.__display_board()

            if piece_placed:
                self.players_turn = list(filter((lambda p: p != self.players_turn), self.players))[0]

    def __display_board(self):
        self.board.display()