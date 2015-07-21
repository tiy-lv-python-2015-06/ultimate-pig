import random
from statistics import mean, pstdev


class Game:
    """
     Should print instructions
     Create and start the turn
     Adding turn score to player score
     End game when player reaches 100
    """

    def __init__(self, player1, player2):
        self.die = Die()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def start(self):
        while not self.winner():
            turn = Turn(self.current_player, self.die)
            turn.run()
            self.current_player.turns += 1
            self.current_player.score += turn.score
            # print("{}'s score is now {}".format(self.current_player,
            #                                     self.current_player.score))
            self.switch_player()
        return self.player2.score
        # if self.winner() == self.player1:
        #     return 1
        # else:
        #     return 2

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def winner(self):
        # if self.player1.score < 10 and self.player2.score < 10:
        #     return None
        if self.player2.turns == 7:
            return True
            # if self.player1.score > self.player2.score:
            #     return self.player1
            # else:
            #     return self.player2


class Turn:
    """
    Roll the die
    Record result
    Tell the player result
    Ask the player to roll again
    """

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
        # print("{} you rolled a {} and your turn score is {}".format(
        #     self.player.name, roll, self.score))
        if not self.turn_over:
            self.turn_over = not self.player.go_again(self.score)


class Player:
    """ Should decide whether to go again """

    def __init__(self, name='Bob'):
        self.name = name
        self.score = 0
        self.rolls = []
        self.turns = 0

    def record_roll(self, roll):
        self.rolls.append(roll)

    def go_again(self, score):
        answer = input("Roll again?").lower()
        if answer[0] == 'y':
            return True
        else:
            return False

    def __str__(self):
        return "Player: {}".format(self.name)


class ComputerPlayer(Player):
    def go_again(self, score):
        return False


class ExperimentalPlayer(Player):
    def __init__(self, name="Bob", sto`p_at=0):
        super(ExperimentalPlayer, self).__init__(name=name)
        self.stop_at = stop_at

    def go_again(self, score):
        if score >= self.stop_at:
            return False
        else:
            return True


class SmartPlayer(Player):
    def go_again(self, score):
        if score >= 24:
            return False
        else:
            return True


class Die:
    def roll(self):
        return random.randint(1, 6)


class Simulation:
    def __init__(self, stop_at=None, games=None):
        self.stop_at = stop_at
        self.games = games
        self.win_dict = {}
        self.run_simulation()

    def run_simulation(self):
        for y in range(self.stop_at):
            win_list = []
            for x in range(self.games):
                player1 = ComputerPlayer("1")
                player2 = ExperimentalPlayer("2", y)
                game = Game(player1, player2)
                win_list.append(game.start())
            self.win_dict[y] = win_list


# def run_sim(stop_at=None, games=None):
#     sim = Simulation(stop_at, games)
#     return sim


def get_mean_wins(sim):
    mean_dict = {}
    for x in sim.win_dict.keys():
        mean_dict[x] = mean(sim.win_dict.get(x))
    return mean_dict


def get_stddev(sim):
    stddev_dict = {}
    for x in sim.win_dict:
        stddev_dict[x] = pstdev(sim.win_dict.get(x))
    return stddev_dict


def get_highest_score(sim):
    high_score = {}
    for x in sim.win_dict:
        high_score[x] = max(sim.win_dict.get(x))
    return high_score


if __name__ == '__main__':
    """not very good right now, as the print statements are missing"""
    # player1 = Player()
    # player2 = SmartPlayer()
    # game = Game(player1, player2)
    # game.start()
    # sim1 = Simulation(5, 5)
    # # sim1.run_simulation()
    # print((get_mean_wins(sim1)))
    # print(get_highest_score(sim1))
    # print(get_stddev(sim1))
    # print(get_highest_score(sim1))
