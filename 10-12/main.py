import utils
import re

input_file = utils.read_file('input.txt')

def make_map():
    map = []
    row = []
    #for index in range(len(input_file[0].strip()) + 2):
        #row.append('.')
    map.append(row)
    for line in input_file:
        row = []
        for char in line.strip():
            row.append(char)
        #row.append('.')
        map.append(row)
    row = []
    #for index in range(len(input_file[0].strip()) + 2):
        #row.append('.')
    map.append(row)
    return map


def make_grahp(map):
    graph = {}
    for i in range(0, len(map)):                        # j = x, i = y
        for j in range(0, len(map[i])):
            if map[i][j] == '|':
                graph[str(j) + ',' + str(i)] = [str(j) + ',' + str(i-1), str(j) + ',' + str(i+1)]
            elif map[i][j] == '-':
                graph[str(j) + ',' + str(i)] = [str(j-1) + ',' + str(i), str(j+1) + ',' + str(i)]
            elif map[i][j] == 'L':
                graph[str(j) + ',' + str(i)] = [str(j) + ',' + str(i-1), str(j+1) + ',' + str(i)]
            elif map[i][j] == 'J':
                graph[str(j) + ',' + str(i)] = [str(j) + ',' + str(i-1), str(j-1) + ',' + str(i)]
            elif map[i][j] == '7':
                graph[str(j) + ',' + str(i)] = [str(j-1) + ',' + str(i), str(j) + ',' + str(i+1)]
            elif map[i][j] == 'F':
                graph[str(j) + ',' + str(i)] = [str(j + 1)+ ',' + str(i), str(j) + ',' + str(i + 1)]
            elif map[i][j] == '.':
                graph[str(j) + ',' + str(i)] = []
            elif map[i][j] == 'S':
                start = str(j) + ',' + str(i)
    start_neigbours = []
    for node in graph:
        if start in graph[node]:
            start_neigbours.append(node)
    graph[start] = start_neigbours
    return graph, start


def DFS(graph, node):
    visited = []
    queue = []

    queue.append(node)
    visited.append(node)

    while queue:
        s = queue.pop()
        for x in graph[s][::-1]:
            if x not in visited:
                visited.append(x)
                queue.append(x)
    return visited


def part1():
    graph, start = make_grahp(make_map())
    all_paths = DFS(graph, start)
    max_len = int(len(all_paths) / 2)
    return max_len


def part2():
    _map, _start, _loop_nodes = parse_map(input_file)
    row_counts = []

    for h, items in enumerate(_map):
        line = [v if (h, w) in _loop_nodes else "." for w, v in enumerate(items)]
        line = "".join(line)

        line = re.sub(r"L-*7", "|", line)
        line = re.sub(r"L-*J", "||", line)
        line = re.sub(r"F-*7", "||", line)
        line = re.sub(r"F-*J", "|", line)

        cross = 0
        inside = 0

        for c in line:
            if c == "." and cross % 2:
                inside += 1
            elif c in "F7LJ|":
                cross += 1
        row_counts.append(inside)
    return sum(row_counts)

def parse_map(data):
    start = None
    _map = []

    for h, line in enumerate(data):
        _map.append(list(line))
        if "S" in line:
            start = (h, line.index("S"))

    """ four adjacent directions """
    adj_dirs = [  # top, right, bottom, left
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]

    """ define the direction connected to the adjacent node for each symbol """
    symbol_connects = {  # top, right, bottom, left
        "|": (1, 0, 1, 0),
        "-": (0, 1, 0, 1),
        "L": (1, 1, 0, 0),
        "J": (1, 0, 0, 1),
        "7": (0, 0, 1, 1),
        "F": (0, 1, 1, 0),
    }

    """ define the types of adjacent nodes that can be connected for each direction """
    # adj_connect_types = {pos: [k for k, v in symbol_connects.items() if v[(i + 2) % 4]] for i, pos in enumerate(adj_dirs)}
    adj_connect_types = {
        (-1, 0): "F|7",
        (0, 1): "7-J",
        (1, 0): "L|J",
        (0, -1): "F-L",
    }

    adjs = [0, 0, 0, 0]  # top, right, bottom, left
    for i, adj in enumerate(adj_dirs):
        pos = tuple(a + b for a, b in zip(start, adj))
        if _map[pos[0]][pos[1]] in adj_connect_types[adj]:
            adjs[i] = 1

    _map[start[0]][start[1]] = {v: k for k, v in symbol_connects.items()}[tuple(adjs)]

    queue = [start]
    visited = set()

    while queue:
        pos = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if _map[pos[0]][pos[1]] in " .":
            continue

        sym = _map[pos[0]][pos[1]]
        _dirs = [adj_dirs[i] for i, v in enumerate(symbol_connects[sym]) if v == 1]
        for dy, dx in _dirs:
            queue.append((pos[0] + dy, pos[1] + dx))

    return _map, start, visited


#print("Part 1: ", part1())
print("Part 2: ", part2())
