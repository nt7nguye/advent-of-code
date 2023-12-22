from functools import cmp_to_key

def get_hand_value(hand):
    m = {}
    for card in hand:
        if card not in m:
            m[card] = 0
        m[card] += 1
    
    multiples = sorted(list(m.values()), reverse=True)
    if multiples[0] == 3 and multiples[1] == 2:
        return 3.5 # fullhouse
    if multiples[0] == 2 and multiples[1] == 2:
        return 2.5 # 2 pairs
    return multiples[0]

def get_card_value(card):
    if card == 'T':
        return 10
    if card == 'J':
        return 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14
    return int(card)

def compare_play(play1, play2):
    hand1 = play1[0]
    hand2 = play2[0]
    val1 = get_hand_value(hand1)
    val2 = get_hand_value(hand2)
    if val1 != val2:
        return val1 - val2
    for i in range(5):
        card_val1 = get_card_value(hand1[i])
        card_val2 = get_card_value(hand2[i])
        if card_val1 != card_val2:
            return card_val1 - card_val2
    return 0
        
    
def solve(input):
    plays = []
    for line in input:
        tokens = line.split(' ')
        plays.append([tokens[0], int(tokens[1])])
    plays.sort(key=cmp_to_key(compare_play))
    return sum([(i + 1) * play[1] for i, play in enumerate(plays)])

