import random


class Game:
    """Should print instructions.  Create and start the turn.  Adding turn score to player score.
       End game when player reaches 100.
    """
    def __init__(self, player_1):
        """Initializes Game class and sets initial values."""
        self.die = Die()
        self.player_1 = player_1
        self.current_player = self.player_1
        self.turns = 1

    def start(self):
        """Starts game and controls the flow."""
        while self.turns <= 7:
            # print()
            # print("This is turn {}.".format(self.turns))
            turn = Turn(self.current_player, self.die)
            turn.run()
            self.current_player.score += turn.score
            # print("{}'s score is now {}".format(self.current_player, self.current_player.score))
            self.turns += 1
        # print()
        # print("You have reached 7 turns.  Game over.")
        # print("Your total score is {}.".format(self.current_player.score))


class Turn:
    """Roll the die. Record result. Tell the player result. Ask the player to roll again."""
    def __init__(self, player, die):
        """Initializes turn elements for game."""
        self.score = 0
        self.player = player
        self.turn_over = False
        self.die = die

    def record_roll(self, roll):
        """Method to keep track of the turn score and player roll."""
        if roll == 1:
            self.turn_over = True
            self.score = 0
        else:
            self.score += roll

    def run(self):
        """Method for running turn when player turn not over."""
        while not self.turn_over:
            self.go()

    def go(self):
        """Method for rolling the die for the player in a turn."""
        roll = self.die.roll()
        self.record_roll(roll)
        self.player.record_roll(roll)
        # print("{} you rolled a {} and your turn score is {}".format(self.player.name, roll, self.score))
        if not self.turn_over:
            self.turn_over = not self.player.go_again()


class Die:
    """Class for rolling the die"""
    def roll(self):
        """Rolls one die"""
        return random.randint(1, 6)


class Player:
    """The Base Player class for players of the game."""
    def __init__(self, name="Bob"):
        """Initializes Player class with values."""
        self.name = name
        self.score = 0
        self.rolls = []

    def record_roll(self, roll):
        """Records the results of a roll."""
        self.rolls.append(roll)

    def go_again(self):
        """Method to decide whether to choose again.  Returns True to choose, False otherwise"""
        return False

    def __str__(self):
        """For outputting player information."""
        return "Player: {}".format(self.name)


class PlayerAlwaysRoles(Player):
    """Player that always chooses to role dice.  Inherits from Player."""
    def go_again(self):
        """Method to decide whether to choose again.  Returns True to choose, False otherwise"""
        return True


class PlayerRandomGuess(Player):
    """Player that randomly chooses whether to role dice.  Inherits from Player."""
    def go_again(self):
        """Method to decide whether to choose again.  Returns True to choose, False otherwise"""
        num = random.randint(1, 2)
        if num == 1:
            return True
        else:
            return False


class AggressivePlayer(Player):
    """Player that chooses more aggressively the lower score they have."""
    def go_again(self):
        """Method to decide whether to choose again.  Returns True to choose, False otherwise."""
        num = random.randint(1, 50)
        if (self.score < 50) and (num <= 40):
            return True
        elif (self.score < 60) and (num <= 30):
            return True
        elif (self.score < 70) and (num <= 20):
            return True
        elif (self.score < 80) and (num <= 10):
            return True
        else:
            return False


class TimidPlayer(Player):
    """Player that chooses less aggressively the more points they have."""
    def go_again(self):
        """Method to decide whether to choose again.  Returns True to choose, False otherwise."""
        num = random.randint(1, 50)
        if (self.score < 80) and (num <= 40):
            return False
        elif (self.score < 70) and (num <= 30):
            return False
        elif (self.score < 60) and (num <= 20):
            return False
        elif (self.score < 50) and (num <= 10):
            return False
        else:
            return True


class MiddlePlayer(Player):
    """Player that chooses at a mid level of risk."""
    def go_again(self):
        """Method to decide whether to choose again.  Returns True to choose, False otherwise."""
        num = random.randint(1, 50)
        if (self.score < 60) and (num <= 20):
            return True
        elif (self.score < 50) and (num <= 30):
            return True
        elif (self.score < 40) and (num <= 40):
            return True
        elif (self.score < 30) and (num <= 20):
            return True
        else:
            return False


if __name__ == '__main__':
    player1 = MiddlePlayer("ENIAC")
    game = Game(player1)
    game.start()
    # print(player1.score)
