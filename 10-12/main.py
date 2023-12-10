import utils

input_file = utils.read_file('input.txt')

def make_map():
    map = []
    row = []
    for index in range(len(input_file[0].strip()) + 2):
        row.append('.')
    map.append(row)
    for line in input_file:
        row = ['.']
        for char in line.strip():
            row.append(char)
        row.append('.')
        map.append(row)
    row = []
    for index in range(len(input_file[0].strip()) + 2):
        row.append('.')
    map.append(row)
    return map


def make_grahp(map):
    graph = {}
    for i in range(1, len(map) - 1):                        # j = x, i = y
        for j in range(1, len(map[i]) - 1):
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


def DFS(graph, node, seen=None, path=None):
    # node is the starting position
    # graph is the graph in dictionary format
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


print("Part 1: ", part1())
