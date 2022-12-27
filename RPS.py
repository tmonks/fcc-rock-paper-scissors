import random


def player(prev_play, opponent_history=[], counter=[0], pattern=[]):
    # reset counter and pattern if starting a new player
    if prev_play == '':
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
        if first_two == 'RP':
            print('Playing quincy')
            reset_pattern(pattern, 'PPSSR')
        elif first_two == 'RR':
            print('Playing mrugesh')
            reset_pattern(pattern, 'RSP')
        elif first_two == 'PR':
            print('Playing kris')
            reset_pattern(pattern, 'RSP')
        else:
            print('Playing unknown')

    return pattern[counter[0] % len(pattern)]


def reset_pattern(list, pattern):
    list.clear()
    for letter in pattern:
        list.append(letter)
