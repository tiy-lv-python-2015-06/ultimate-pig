import random

class SolitaireGame:
    """
     Should print instructions
     Create and start the turn
     Adding turn score to player score
     End game when player reaches 100
    """
    def __init__(self, player1):
        self.die = Die()
        self.player1 = player1
        self.num_turns = 0

    def start(self):

        while self.num_turns < 7:

            turn = Turn(self.player1, self.die)
            while not turn.turn_over:
                turn.run()
                self.player1.score += turn.turn_score
                #print("{} Your score is now {}".format(self.player1.name,
                #                                       self.player1.score))
                self.num_turns += 1

        return self.player1.score

    def done(self):
        # this is solitaire version so just return true if the player wants
        #  to hold
        return self.player1


class Turn:
    """
    Roll the die
    Record result
    Tell the player result
    Ask the player to roll again
    """
    def __init__(self, player, die):
        self.turn_score = 0
        self.player = player
        self.turn_over = False
        self.die = die

    def record_roll(self, roll):
        if roll == 1:
            self.turn_over = True
            self.turn_score = 0
        else:
            self.turn_score += roll

    def run(self):
        #print('in run self.turn_over {}'.format(self.turn_over))
        while not self.turn_over:
            self.go()

    def go(self):
        roll = self.die.roll()
        self.record_roll(roll)
        self.player.record_roll(roll)
        #print("You rolled a {} and your turn score is {}".
        #      format(roll, self.turn_score))
        if not self.turn_over:
            self.turn_over = not self.player.go_again(self.turn_score)


class Player:
    """ Should decide whether to go again """

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rolls = []

    def record_roll(self, roll):
        self.rolls.append(roll)

    def go_again(self, turn_score):
        # this base player always returns false and therefore only goes once
        # per turn
        return False

    def __str__(self):
        return "Player: {}".format(self.name)


# class BetterPlayer(Player):
#     """
#         Should decide whether to go again
#         This is the hold at 30 player
#     """
#     def go_again(self, turn_score):
#         # lets come up with some algorithm to decide to go again or not
#         if turn_score < 30:
#             return True
#         else:
#             return False


# class BestPlayer(Player):
#     """
#         Should decide whether to go again
#         This is the player that tries to calculate to hold or roll
#         based on score and number of rolls
#     """
#     def go_again(self, turn_score):
#         return (turn_score + 11*len(self.rolls)) <= 500
#         # s + 11t ≤ 200, where s is
#         # the player score and t is the turn total.


class Die:
    def roll(self):
        return random.randint(1,6)

if __name__ == '__main__':


    player = Player('Basic')
    game = SolitaireGame(player)
    print(game.start())
    print("===============================================")

    player1 = BetterPlayer('Better')
    game = SolitaireGame(player1)
    print(game.start())
    print("===============================================")

    player2 = BestPlayer('Best')
    game = SolitaireGame(player2)
    print(game.start())