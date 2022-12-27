import random
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# def player(prev_play, opponent_history=[], counter=[0], pattern=['R', 'P', 'S']):
def player(prev_play, opponent_history=[], counter=[0], pattern=[]):
    # reset counter if starting a new player
    if prev_play == '':
        # print('Resetting counter')
        pattern.clear()
        pattern.append('S')
        pattern.append('S')
        pattern.append('P')
        pattern.append('S')
        pattern.append('R')
        pattern.append('P')
        pattern.append('P')
        pattern.append('R')
        pattern.append('R')
        # pattern = ['S', 'S', 'P', 'S', 'R', 'P', 'P', 'R', 'R']
        counter[0] = 0
        opponent_history.clear()

    counter[0] += 1

    if prev_play != '' and len(opponent_history) < 2:
        # print(f'appending prev_play: {prev_play}')
        opponent_history.append(prev_play)

    # print(f'opponent_history: {opponent_history}')
    # print(f'using pattern: {pattern}')

    if counter[0] == 3:
        first_two = "".join(opponent_history)
        if first_two == 'RP':
            print('Playing quincy')
            pattern.clear()
            # RRPPS
            pattern.append('P')
            pattern.append('P')
            pattern.append('S')
            pattern.append('S')
            pattern.append('R')
        elif first_two == 'RR':
            print('Playing mrugesh')
            pattern.clear()
            pattern.append('R')
            pattern.append('S')
            pattern.append('P')
            # pattern = ['R', 'P', 'S']
        elif first_two == 'PR':
            print('Playing kris')
            pattern.clear()
            pattern.append('R')
            pattern.append('S')
            pattern.append('P')
            # pattern = ['R', 'P', 'S']
        elif first_two == 'PP':
            print('Playing abbey')
            # pattern = ['S', 'S', 'P' 'S', 'R', 'P', 'P', 'R', 'R']
        else:
            print('Playing unknown')

    return pattern[counter[0] % len(pattern)]


def abbey_player(prev_play, counter=[0]):

    counter[0] += 1
    choices = [x for x in 'SSPSRPPRR']
    return choices[counter[0] % len(choices)]


def rps_player(prev_play, counter=[0]):

    counter[0] += 1
    # choices = ['S', 'P', 'R']
    choices = ['R', 'S', 'P']
    return choices[counter[0] % len(choices)]
