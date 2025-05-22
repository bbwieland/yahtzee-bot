import random

from constants import N_DIE_FACES

def roll_die() -> int:
    return random.randint(1, N_DIE_FACES)
