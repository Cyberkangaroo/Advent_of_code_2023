numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers_as_chars = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def part1():
    summe = 0
    values = []
    with open('input.txt', 'r') as file:
        for line in file:
            numbers_in_line = []
            for char in line:
                if char in numbers:
                    numbers_in_line.append(char)
            value = numbers_in_line[0] + numbers_in_line[-1]
            values.append(int(value))

    summe = sum(values)
    return summe


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


def part2():
    values = []
    with open('input.txt', 'r') as file:
        for line in file:
            ones = find_all(line, "one")
            twos = find_all(line, "two")
            threes = find_all(line, "three")
            fours = find_all(line, "four")
            fives = find_all(line, "five")
            sixes = find_all(line, "six")
            sevens = find_all(line, "seven")
            eights = find_all(line, "eight")
            nines = find_all(line, "nine")
            numbers_in_line = {}
            for i in range(len(line)):
                char = line[i]
                if char in numbers:
                    numbers_in_line[i] = char
            for one in ones:
                if one != -1:
                    numbers_in_line[one] = "1"
            for two in twos:
                if two != -1:
                    numbers_in_line[two] = "2"
            for three in threes:
                if three != -1:
                    numbers_in_line[three] = "3"
            for four in fours:
                if four != -1:
                    numbers_in_line[four] = "4"
            for five in fives:
                if five != -1:
                    numbers_in_line[five] = "5"
            for six in sixes:
                if six != -1:
                    numbers_in_line[six] = "6"
            for seven in sevens:
                if seven != -1:
                    numbers_in_line[seven] = "7"
            for eight in eights:
                if eight != -1:
                    numbers_in_line[eight] = "8"
            for nine in nines:
                if nine != -1:
                    numbers_in_line[nine] = "9"
            numbers_in_line = dict(sorted(numbers_in_line.items()))


            value = list(numbers_in_line.values())[0] + list(numbers_in_line.values())[-1]

            values.append(int(value))

    summe = sum(values)
    return summe

# print("part 1: ", part1())
print("part 2: ", part2())