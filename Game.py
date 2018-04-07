class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players

    def start(self):
        player_one_turn = True
        while True:
            input_val = int(input('please enter x value: '))
            player = self.players[0] if player_one_turn else self.players[1]
            self.board.add_piece(player, input_val)
            self.board.display()
            player_one_turn = not player_one_turn