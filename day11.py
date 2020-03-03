path = open("input/11.txt").read().split(",")

start = pos = (0, 0, 0)
xyz = {'nw': (-1, 1, 0), 'n': (0, 1, -1), 'ne': (1, 0, -1), 'sw': (-1, 0, 1), 's': (0, -1, 1), 'se': (1, -1, 0)}
seen = {}
for d in path:
    pos = pos[0] + xyz[d][0], pos[1] + xyz[d][1], pos[2] + xyz[d][2]
    seen[pos] = (abs(pos[0] - start[0]) + abs(pos[1] - start[1]) + abs(pos[2] - start[2])) // 2

print(seen[pos])
print(max(seen.values()))
