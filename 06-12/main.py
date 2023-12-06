import utils


input = utils.read_file('input.txt')


def get_races():
    times = []
    records = []
    for time in input[0].split(':')[1].strip().split():
        times.append(int(time))
        records.append(int(input[1].split(':')[1].strip().split()[times.index(int(time))]))
    return times, records


def get_single_race():
    time = ''
    record = ''
    for string in input[0].split(':')[1].strip().split():
        time += string
    for string in input[1].split(':')[1].strip().split():
        record += string
    return int(time), int(record)

def part1():
    times, records = get_races()
    win_count = []
    while len(times) > 0:
        wins = 0
        time = times.pop(0)
        record = records.pop(0)
        for i in range(time + 1):
            distance = (time - i) * i
            if distance > record:
                wins += 1
        win_count.append(wins)

    result = win_count.pop(0)
    for win in win_count:
        result *= win
    return result


def part2():
    time, record = get_single_race()
    wins = 0
    for i in range(time + 1):
        distance = (time - i) * i
        if distance > record:
            wins += 1
    return wins

print("Part 1: ", part1())

print("Part 2: ", part2())
