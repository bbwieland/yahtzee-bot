####################
# Top-half scoring #
####################

def score_1s(roll):
    return roll.count(1) * 1

def score_2s(roll):
    return roll.count(2) * 2

def score_3s(roll):
    return roll.count(3) * 3

def score_4s(roll):
    return roll.count(4) * 4

def score_5s(roll):
    return roll.count(5) * 5

def score_6s(roll):
    return roll.count(6) * 6

####################################
# Other number-counting categories #
####################################

def score_3k(roll):
    for value in set(roll):
        if roll.count(value) >= 3:
            return sum(roll)
    return 0

def score_4k(roll):
    for value in set(roll):
        if roll.count(value) >= 4:
            return sum(roll)
    return 0

def score_yz(roll):
    for value in set(roll):
        if roll.count(value) == 5:
            return 50
    return 0

#############
# Straights #
#############

def score_ss(roll):
    unique = sorted(set(roll))
    straights = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    for straight in straights:
        if all(num in unique for num in straight):
            return 30
    return 0

def score_ls(roll):
    if len(set(roll)) == 5:
        return 40
    return 0

##############
# Full House #
##############

def score_fh(roll):
    counts = [roll.count(x) for x in set(roll)]
    if sorted(counts) == [2, 3]:
        return 25
    return 0

##########
# Chance #
##########

def score_ch(roll):
    return sum(roll)