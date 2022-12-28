import random


def player(prev_play, opponent_history=[], counter=[0], pattern=[]):
    # reset counter and pattern if starting a new player
    if prev_play == '':
        # default pattern, tailored for abbey
        reset_pattern(pattern, 'SSPSRPPRR')
        counter[0] = 0
        opponent_history.clear()

    counter[0] += 1

    # keep track of the opponent's first two plays
    if prev_play != '' and len(opponent_history) < 2:
        opponent_history.append(prev_play)

    # quincy starts with RP, mrugesh with RR, kris with PR, abbey with PP
    if counter[0] == 3:
        first_two = "".join(opponent_history)
        if first_two == 'RP':  # quincy
            reset_pattern(pattern, 'PPSSR')
        elif first_two == 'RR':  # mrugesh
            reset_pattern(pattern, 'RSP')
        elif first_two == 'PR':  # kris
            reset_pattern(pattern, 'RSP')

    return pattern[counter[0] % len(pattern)]


def reset_pattern(pattern, string):
    """ resets pattern to a list of characters in string """
    pattern.clear()
    for letter in string:
        pattern.append(letter)
