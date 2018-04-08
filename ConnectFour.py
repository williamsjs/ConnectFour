import Player as p
import Board as b
import Game as g

player_one = p.Player(True)
player_two = p.Player(False)
board = b.Board(7, 6)
game = g.Game(board, [player_one, player_two])
game.start()