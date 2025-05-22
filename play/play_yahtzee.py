import random
from constants import N_DICE, SCORING_RULES
from utils import roll_die

class YahtzeeDice:
    def __init__(self):
        self.roll = [0] * N_DICE
        self.roll_num = 0

    def __str__(self):
        return f"Roll {self.roll_num}: {self.roll}"

    def reroll(self, rules):
        for die in range(N_DICE):
            self.roll[die] = roll_die() if rules[die] else self.roll[die]
        
        self.roll_num += 1

    def score(self, category):
        return SCORING_RULES[category](self.roll)
    