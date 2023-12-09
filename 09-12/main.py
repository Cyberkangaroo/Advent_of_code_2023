import utils

histories = [line.strip().split(' ') for line in utils.read_file('input.txt')]


def find_sequence(row):
    sequence = []
    for index in range(len(row) - 1):
        sequence.append(int(row[index + 1]) - int(row[index]))
    return sequence


def part1(histories):
    sum = 0
    for history in histories:
        rows = []
        rows.append([int(char) for char in history])
        while not all(v == 0 for v in rows[-1]):
            rows.append(find_sequence(rows[-1]))
        for row in rows:
            row.append(0)
        for index in range(1, len(rows)):
            rows[-(index+1)][-1] = rows[-(index+1)][-2] + rows[-index][-1]
        sum += rows[0][-1]
    return sum


def part2(histories):
    sum = 0
    for history in histories:
        rows = []
        rows.append([int(char) for char in history])
        while not all(v == 0 for v in rows[-1]):
            rows.append(find_sequence(rows[-1]))
        for row in rows:
            row.insert(0, 0)
        for index in range(1, len(rows)):
            rows[-(index + 1)][0] = rows[-(index + 1)][1] - rows[-index][0]
        sum += rows[0][0]
    return sum


print("Part1 : ", part1(histories))
print("Part 2: ", part2(histories))
