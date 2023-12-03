import utils


input_file = utils.read_file('input.txt')



nums_as_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_numbers():
    numbers = []
    lines = input_file
    for line in lines:
        line_list = list(line.strip())
        index = 0
        while len(line_list) > 0:
            char = line_list.pop(0)
            if char in nums_as_char:
                number = char
                starting_index = index
                end_index = index
                next = line_list.pop(0)
                while next in nums_as_char and len(line_list) != 0:
                    number += next
                    if len(line_list) > 0:
                        next = line_list.pop(0)
                    if len(line_list) == 0 and next in nums_as_char:
                        number += next
                        end_index += 1
                    end_index += 1
                numbers.append([lines.index(line), starting_index, end_index, number])
                index = end_index + 1
            index += 1
    return numbers


def get_symboles():
    lines = input_file
    symbols = []
    for line in lines:
        line_list = list(line.strip())
        for index in range(len(line_list)):
            char = line_list[index]
            if char != '.':
                symbols.append([lines.index(line), index])
    return symbols


def check_adjacent(numbers, symbols):
    parts = []
    for index in range(len(numbers)):
        neighbors = []
        if numbers[index][0] == 0:
            if numbers[index][1] == 0:                                         #links oben
                neighbors.append([numbers[index][0], numbers[index][2]+1])
                for i in range(0, numbers[index][2]+2):
                    neighbors.append([numbers[index][0]+1, i])
            elif numbers[index][2] == len(input_file[0].strip())-1:            #rechts oben
                neighbors.append([numbers[index][0], numbers[index][1]-1])
                for i in range(numbers[index][1]-1, numbers[index][2] + 1):
                    neighbors.append([numbers[index][0]+1, i])
            else:                                                               #obere kante
                neighbors.append([numbers[index][0], numbers[index][1]-1])
                neighbors.append([numbers[index][0], numbers[index][2] + 1])
                for i in range(numbers[index][1]-1, numbers[index][2]+2):
                    neighbors.append([numbers[index][0]+1, i])
        elif numbers[index][0] == len(input_file)-1:
            if numbers[index][1] == 0:                                         #links unten
                neighbors.append([numbers[index][0], numbers[index][2]+1])
                for i in range(0, numbers[index][2]+2):
                    neighbors.append([numbers[index][0]-1, i])
            elif numbers[index][2] == len(input_file[0].strip())-1:            #rechts unten
                neighbors.append([numbers[index][0], numbers[index][1]-1])
                for i in range(numbers[index][1]-1, numbers[index][2] + 1):
                    neighbors.append([numbers[index][0]-1, i])
            else:                                                               #untere kante
                neighbors.append([numbers[index][0], numbers[index][1]-1])
                neighbors.append([numbers[index][0], numbers[index][2] + 1])
                for i in range(numbers[index][1]-1, numbers[index][2]+2):
                    neighbors.append([numbers[index][0]-1, i])
        elif numbers[index][1] == 0:                                           #linke kante
            neighbors.append([numbers[index][0], numbers[index][2] + 1])
            for i in range(0, numbers[index][2] + 2):
                neighbors.append([numbers[index][0] + 1, i])
            for i in range(0, numbers[index][2] + 2):
                neighbors.append([numbers[index][0] - 1, i])
        elif numbers[index][2] == len(input_file[0].strip())-1:                #rechte kante
            neighbors.append([numbers[index][0], numbers[index][1] - 1])
            for i in range(numbers[index][1]-1, numbers[index][2] + 1):
                neighbors.append([numbers[index][0] + 1, i])
            for i in range(numbers[index][1] - 1, numbers[index][2] + 1):
                neighbors.append([numbers[index][0] - 1, i])
        else:
            neighbors.append([numbers[index][0], numbers[index][1] - 1])
            neighbors.append([numbers[index][0], numbers[index][2] + 1])
            for i in range(numbers[index][1] - 1, numbers[index][2] + 2):
                neighbors.append([numbers[index][0] - 1, i])
            for i in range(numbers[index][1] - 1, numbers[index][2] + 2):
                neighbors.append([numbers[index][0] + 1, i])
        for neighbor in neighbors:
            if neighbor in symbols:
                parts.append(int(numbers[index][3]))
    return parts


def find_gears():
    lines = input_file
    possible_gears = []
    for line in lines:
        line_list = list(line.strip())
        for index in range(len(line_list)):
            char = line_list[index]
            if char == '*':
                possible_gears.append([lines.index(line), index])
    print(possible_gears)
    gears = []
    for candidate in possible_gears:
        neighbors = []
        number_count = 0
        if candidate[0] == 0:                               #links oben
            if candidate[1] == 0:
                neighbors.append([0, 1])
                neighbors.append([1, 0])
                neighbors.append([1, 1])
            elif candidate[1] == len(input_file[0])-1:      #rechts oben
                neighbors.append([0, candidate[1]-1])
                neighbors.append([1, candidate[1]])
                neighbors.append([1, candidate[1] - 1])
            else:                                           #obere kante
                neighbors.append([0, candidate[1] - 1])
                neighbors.append([0, candidate[1]+1])
                neighbors.append([1, candidate[1]])
                neighbors.append([1, candidate[1] - 1])
                neighbors.append([1, candidate[1] + 1])
        elif candidate[0] == len(input_file)-1:
            if candidate[1] == 0:                           #links unten
                neighbors.append([candidate[0], 1])
                neighbors.append([candidate[0]-1, 0])
                neighbors.append([candidate[0] - 1, 1])
            elif candidate[1] == len(input_file[0])-1:      #rechts unten
                neighbors.append([candidate[0], candidate[1]-1])
                neighbors.append([candidate[0]-1, candidate[1]])
                neighbors.append([candidate[0] - 1, candidate[1] - 1])
            else:                                           #untere kante
                neighbors.append([candidate[0], candidate[1] - 1])
                neighbors.append([candidate[0], candidate[1] + 1])
                neighbors.append([candidate[0]-1, candidate[1]])
                neighbors.append([candidate[0] - 1, candidate[1] - 1])
                neighbors.append([candidate[0] - 1, candidate[1] + 1])
        elif candidate[1] == 0:                             #linke kante
            neighbors.append([candidate[0], candidate[1]+1])
            neighbors.append([candidate[0]-1, candidate[1]])
            neighbors.append([candidate[0]+1, candidate[1]])
            neighbors.append([candidate[0] - 1, candidate[1] + 1])
            neighbors.append([candidate[0] + 1, candidate[1] + 1])
        elif candidate[1] == len(input_file[0])-1:          #rechte kante
            neighbors.append([candidate[0], candidate[1] - 1])
            neighbors.append([candidate[0] - 1, candidate[1]])
            neighbors.append([candidate[0] + 1, candidate[1]])
            neighbors.append([candidate[0] - 1, candidate[1] - 1])
            neighbors.append([candidate[0] + 1, candidate[1] - 1])
        else:                                               #mitte
            neighbors.append([candidate[0], candidate[1] - 1])
            neighbors.append([candidate[0], candidate[1] + 1])
            neighbors.append([candidate[0] - 1, candidate[1]])
            neighbors.append([candidate[0] + 1, candidate[1]])
            neighbors.append([candidate[0] - 1, candidate[1] - 1])
            neighbors.append([candidate[0] + 1, candidate[1] - 1])
            neighbors.append([candidate[0] - 1, candidate[1] + 1])
            neighbors.append([candidate[0] + 1, candidate[1] + 1])
        numbers = get_numbers()
        numbers_pos = []
        for number in numbers:
            for index in range(number[1], number[2] + 1):
                if [number[0], index] in neighbors:
                    if number[3] not in numbers_pos:
                        number_count += 1
                        numbers_pos.append(number[3])
        if number_count == 2:
            gears.append([candidate, numbers_pos])
    return gears


def part1(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


def part2():
    sum = 0
    gears = find_gears()
    for gear in gears:
        sum += int(gear[1][0]) * int(gear[1][1])
    return sum


print("Part 1: ", part1(check_adjacent(get_numbers(), get_symboles())))
print("Part 2: ", part2())
