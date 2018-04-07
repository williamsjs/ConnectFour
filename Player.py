class Player:

    def __init__(self, player_one):
        address_player = 'One' if player_one else 'Two'
        self.name = input(f"Player {address_player}, please enter your name: ")
        self.player_one = player_one