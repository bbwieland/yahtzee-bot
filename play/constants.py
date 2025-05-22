import scoring_rules as sr

N_DICE = 5
N_DIE_FACES = 6

SCORING_CATEGORIES = [
    '1s', '2s', '3s', '4s', '5s', '6s',
    '3k', '4k', 'ss', 'ls', 'fh', 'ch', 'yz'
]

SCORING_RULES = {
    # Top Half
    '1s' : sr.score_1s,
    '2s' : sr.score_2s,
    '3s' : sr.score_3s,
    '4s' : sr.score_4s,
    '5s' : sr.score_5s,
    '6s' : sr.score_6s,
    # Bottom Half
    '3k' : sr.score_3k,
    '4k' : sr.score_4k,
    'fh' : sr.score_fh,
    'ss' : sr.score_ss,
    'ls' : sr.score_ls,
    'ch' : sr.score_ch,
    'yz' : sr.score_yz
}