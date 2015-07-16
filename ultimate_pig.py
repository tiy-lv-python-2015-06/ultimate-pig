import random


class Game:

    def __init__(self, player, turn_count=0, total_score=0):
        self.die = Die()
        self.player = player
        self.turn_count = turn_count
        self.total_score = total_score

    def start(self):
        results = []
        while self.turn_count < 7:
            turn = Turn(self.player, self.die)
            turn.run()
            self.turn_count += 1
            self.total_score += turn.score
        if self.turn_count == 7:
            results = self.total_score
            # print(results)
        return results


class Turn:

    def __init__(self, player, die):
        self.score = 0
        self.player = player
        self.turn_over = False
        self.die = die

    def record_roll(self, roll):
        if roll == 1:
            self.turn_over = True
            self.score = 0
        else:
            self.score += roll

    def run(self):
        while not self.turn_over:
            self.go()

    def go(self):
        roll = self.die.roll()
        self.record_roll(roll)
        self.player.record_roll(roll)

        if not self.turn_over:
            self.turn_over = not self.player.go_again(self.score)


class Player:

    def __init__(self, name="Bob"):
        self.name = name
        self.rolls = []

    def record_roll(self, roll):
        self.rolls.append(roll)


    # def go_again(self, score):
    #     if score >= 11:
    #         return False
    #     else:
    #         return True

    def go_again(self, score):
        return False

    # def __str__(self):
    #     return "Player: {}".format(self.name)


# class ComputerPlayer(Player):
#
#     def go_again(self):
#         return False


class Die:
    def roll(self):
        return random.randint(1, 6)

if __name__ == '__main__':

    player = Player("Bitchin")
    game = Game(player)
    game.start()
