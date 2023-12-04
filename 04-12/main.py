import utils

input_cards = utils.read_file('input.txt')

def pars_cards(input_cards):
    cards = []
    for card in input_cards:
        winning = []
        have = []
        number = card.split(':')[0]
        number = number.replace('Card ', '')
        number = int(number)
        for winning_number in card.split(':')[1].split('|')[0].strip().split(' '):
            if winning_number != '':
                winning.append(int(winning_number))
        for having in card.split(':')[1].split('|')[1].strip().split(' '):
            if having != '':
                have.append(int(having))
        card = {'number': number, 'winning': winning, 'have': have, 'copies': 1}
        cards.append(card)
    return cards


def get_card_score(card):
    score = 0
    for number in card['winning']:
        if number in card['have']:
            if score == 0:
                score += 1
            else:
                score *= 2
    return score


def count_matching(card):
    matching = 0
    for winning in card['winning']:
        if winning in card['have']:
            matching += 1
    return matching


def part1():
    sum = 0
    for card in pars_cards(input_cards):
        sum += get_card_score(card)
    return sum


def part2(cards):
    total = 0
    playset = cards
    while len(playset) > 0:
        card = playset.pop(0)
        total += card['copies']
        matching = count_matching(card)
        for i in range(matching):
            playset[i]['copies'] += card['copies']
    return total


print("Part 1: ", part1())
print("Part 2: ", part2(pars_cards(input_cards)))
