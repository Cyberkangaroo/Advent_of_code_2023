import utils
from math import lcm

input = utils.read_file('input.txt')


instructions = [steep for steep in input[0].strip()]

def get_nodes():
    nodes = {}
    for index in range(2, len(input)):
        name = input[index].strip().split('=')[0].strip()
        next = input[index].strip().split('=')[1].strip().replace('(', '').replace(')', '').replace(' ', '').split(',')
        nodes[name] = next
    return nodes


def make_step(instructions, starting, nodes):
    current_node = starting
    step_count = 0

    while not current_node.endswith('Z'):
        direction = instructions[step_count % len(instructions)]
        current_node = nodes[current_node][1 if direction == 'R' else 0]
        step_count += 1
    return step_count


def part1(instructions, nodes, starting):
    current_node = starting
    step_count = 0
    while current_node != 'ZZZ':
        direction = instructions[step_count%len(instructions)]
        current_node = nodes[current_node][1 if direction == 'R' else 0]
        step_count += 1
    return step_count


def part2(instructions, nodes):
    starting = [node for node in nodes.keys() if node[2] == 'A']
    steps = 1
    for node in starting:
       steps = lcm(steps, make_step(instructions, node, nodes))
    return steps
    #print(lcm(counts[0], counts[1], counts[2], counts[3], counts[4]))
    #print(lcm(counts[0], counts[1]))


print("Part 1: ", part1(instructions, get_nodes(), 'AAA'))
print("Part 2: ", part2(instructions, get_nodes()))
