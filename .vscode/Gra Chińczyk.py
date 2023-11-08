import random

class Chińczyk:
    def __init__(self):
        self.players = ['A', 'B', 'C', 'D']
        self.positions = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0,
            'a1': None, 'a2': None, 'a3': None, 'a4': None,
            'b1': None, 'b2': None, 'b3': None, 'b4': None,
            'c1': None, 'c2': None, 'c3': None, 'c4': None,
            'd1': None, 'd2': None, 'd3': None, 'd4': None
        }
        self.safe_spots = {
            'a1': 1, 'a2': 9, 'a3': 14, 'a4': 22,
            'b1': 5, 'b2': 12, 'b3': 17, 'b4': 24,
            'c1': 6, 'c2': 13, 'c3': 18, 'c4': 25,
            'd1': 10, 'd2': 15, 'd3': 21, 'd4': 28
        }
        self.winner = None

    def play(self):
        while not self.winner:
            for player in self.players:
                print(f"Player {player}'s turn!")
                dice = random.randint(1, 6)
                print(f"Dice roll: {dice}")
                self.move(player, dice)
                if self.check_winner(player):
                    self.winner = player
                    break
        print(f"Player {self.winner} wins!")

    def move(self, player, steps):
        if self.positions[player] == 0 and steps != 1:
            print("Can't move!")
            return
        new_pos = (self.positions[player] + steps) % 40
        if new_pos in self.positions.values() and new_pos != self.positions[player]:
            print("Can't move!")
            return
        self.positions[player] = new_pos
        if new_pos in self.safe_spots.values():
            return
        for key, value in self.safe_spots.items():
            if value == new_pos:
                self.positions[key] = None
                return
        for other_player, pos in self.positions.items():
            if pos == new_pos and other_player != player:
                self.positions[other_player] = 0
                return

    def check_winner(self, player):
        if all(pos is not None and pos in self.safe_spots.values() for pos in self.positions.values() if pos != 0):
            return True
        return False

game = Chińczyk()
game.play()