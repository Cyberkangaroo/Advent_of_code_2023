import utils

red_max = 12
green_max = 13
blue_max = 14


class Game:
    number = 0
    draws = []
    possible = True

    def __init__(self, number, draws):
        self.number = number
        self.draws = draws
        self.possible = True

    def is_possible(self):
        for draw in self.draws:
            if self.possible == False:
                return False
            elif draw['r'] > red_max: self.possible = False
            elif draw['g'] > green_max: self.possible = False
            elif draw['b'] > blue_max: self.possible = False
        return self.possible

    def min_needed(self):
        red_min = 0
        green_min = 0
        blue_min = 0
        for draw in self.draws:
            if draw['r'] > red_min: red_min = draw['r']
            if draw['g'] > green_min: green_min = draw['g']
            if draw['b'] > blue_min: blue_min = draw['b']
        return red_min, green_min, blue_min
def get_games():
    games = []

    input = utils.read_file('input.txt')
    for line in input:
        draws = []
        game_list = line.split(':')
        number = int(game_list[0].replace('Game ', ''))
        draw_list = game_list[1].split(';')
        for draw in draw_list:
            list = draw.strip().replace('red', 'r').replace('green', 'g').replace('blue', 'b').strip().split(', ')
            dict = {}
            for color in list:
                amount = int(color[0:-2])
                dict[color[-1]] = amount
            if 'r' not in dict.keys(): dict['r'] = 0
            if 'g' not in dict.keys(): dict['g'] = 0
            if 'b' not in dict.keys(): dict['b'] = 0

            draws.append(dict)

        game = Game(number, draws)
        games.append(game)
    return games


games = get_games()


def part1():
    sum = 0
    for game in games:
        if game.is_possible(): sum += game.number

    return sum


def part2():
    sum = 0
    for game in games:
        r_min, g_min, b_min = game.min_needed()
        pow = r_min * g_min * b_min
        sum += pow

    return sum


print("Part 1: ", part1())
print("Part 2: ", part2())
