from copy import copy
from collections import defaultdict, deque
from timeit import default_timer as timer


def moves(state, ports):
    strength, visited, current = state
    result = []
    for i, port in enumerate(ports):
        if i in visited or (port[0] != current and port[1] != current):
            continue
        new_visited = copy(visited)
        new_visited.add(i)
        new_current = port[0] if port[1] == current else port[1]
        result.append((strength + port[0] + port[1], new_visited, new_current))
    return result


ports = []

for line in open("input/24.txt"):
    a, b = map(int, line.strip().split("/"))
    ports.append((a, b))


start = timer()
queue = deque()
visited = set()
# Strength, visited, current
state = (0, set(), 0)
queue.append(state)
max_strength = defaultdict(int)
while queue:
    curr = queue.pop()
    if curr[0] > max_strength[len(curr[1])]:
        max_strength[len(curr[1])] = curr[0]
    for move in moves(curr, ports):
        move_tuple = (tuple(sorted(move[1])), move[2])
        if move_tuple not in visited:
            visited.add(move_tuple)
            queue.append(move)

print(max(max_strength.values()))
print(max_strength[max(max_strength.keys())])

end = timer()
print(f'Took {end - start} seconds.')
