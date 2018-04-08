class Piece:

    def __init__(self, player):
        self.display = '|X|' if player.player_one else '|Y|'
        self.player = player
        self.x = None
        self.y = None
