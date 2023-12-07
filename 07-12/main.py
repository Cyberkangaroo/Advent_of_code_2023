import operator

import utils

input = utils.read_file('input.txt')


def get_hands():
    card_values = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1,
                   '2': 0}
    hands = []
    for line in input:
        hand = {}
        cards = [card for card in line.strip().split(' ')[0]]
        hand['cards'] = [card_values[card] for card in cards]
        hand['bid'] = int(line.strip().split(' ')[1])
        hand = check_value(hand)
        hands.append(hand)
    hands = sort_hands(hands)
    return hands


def check_value(hand):
    counts = {}
    pair_count = 0
    for card in hand['cards']:
        counts[card] = hand['cards'].count(card)
    for count in counts.values():
        if count == 5:
            hand['value'] = 6
            return hand
        elif count == 4:
            hand['value'] = 5
            return hand
        elif count == 3:
            if 2 in counts.values():
                hand['value'] = 4
                return hand
            else:
                hand['value'] = 3
                return hand
        elif count == 2:
            if pair_count == 1:
                hand['value'] = 2
                return hand
            else:
                pair_count += 1
    if pair_count == 1:
        hand['value'] = 1
    else:
        hand['value'] = 0
    return hand


def sort_hands(hands):
    final_sort = sorted(hands, key=operator.itemgetter('value', 'cards'))
    return final_sort


def calculate_winnings(hands):
    winnings = 0
    for i in range(len(hands)):
        winnings += (i + 1) * hands[i]['bid']
    return winnings


def get_hands_with_joker():
    card_values = {'A': 12, 'K': 11, 'Q': 10, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2,
                   '2': 1}
    hands = []
    for line in input:
        hand = {}
        cards = [card for card in line.strip().split(' ')[0]]
        hand['cards'] = [card_values[card] for card in cards]
        hand['bid'] = int(line.strip().split(' ')[1])
        if 0 in hand['cards']:
            hand = get_best_value(hand)
        else:
            hand = check_value(hand)
        hands.append(hand)
    hands = sort_hands(hands)
    return hands


def get_best_value(hand):
    counts = {}
    pair_count = 0
    for card in hand['cards']:
        if card != 0:
            counts[card] = hand['cards'].count(card)
    jocker_count = hand['cards'].count(0)
    if jocker_count == 5 or jocker_count == 4:
        hand['value'] = 6
        return hand
    elif jocker_count == 3:
        if 2 in counts.values():
            hand['value'] = 6
            return hand
        else:
            hand['value'] = 5
            return hand
    elif jocker_count == 2:
        if 3 in counts.values():
            hand['value'] = 6
            return hand
        elif 2 in counts.values():
            hand['value'] = 5
            return hand
        else:
            hand['value'] = 3
            return hand
    elif jocker_count == 1:
        if 4 in counts.values():
            hand['value'] = 6
            return hand
        elif 3 in counts.values():
            hand['value'] = 5
            return hand
        elif 2 in counts.values():
            if list(counts.values()).count(2) == 1:
                hand['value'] = 3
                return hand
            elif list(counts.values()).count(2) == 2:
                hand['value'] = 4
                return hand
        else:
            hand['value'] = 1
            return hand
    return hand


def part1(hands):
    return calculate_winnings(hands)



def part2(hands):
    return calculate_winnings(hands)


print("Part 1: ", part1(get_hands()))
print("Part 2: ", part2(get_hands_with_joker()))