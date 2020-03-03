from copy import copy

# 0: Clean, 1: Weakened, 2: Infected, 3: Flagged
nodes = {}

for row, line in enumerate(open("input/22.txt")):
    for col, char in enumerate(list(line.strip())):
        if char == '#':
            nodes[(row, col)] = 2


# Part A
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
nodes_copy = copy(nodes)
pos = ((row + 1)//2, (col + 1)//2)
d = 0
infections = 0
for i in range(10000):
    if pos in nodes:
        d = (d + 1) % 4
        nodes.pop(pos)
    else:
        d = (d + 3) % 4
        nodes[pos] = 2
        infections += 1
    pos = (pos[0] + dr[d], pos[1] + dc[d])
print(infections)

# Part B
nodes = nodes_copy
pos = ((row + 1)//2, (col + 1)//2)
d = 0
infections = 0
for i in range(10000000):
    if pos in nodes:
        if nodes[pos] == 1:
            # Weakened
            nodes[pos] = 2
            infections += 1
        elif nodes[pos] == 2:
            # Infected
            nodes[pos] = 3
            d = (d + 1) % 4
        elif nodes[pos] == 3:
            # Flagged
            nodes.pop(pos)
            d = (d + 2) % 4
    else:
        # Clean
        d = (d + 3) % 4
        nodes[pos] = 1
    pos = (pos[0] + dr[d], pos[1] + dc[d])
print(infections)
