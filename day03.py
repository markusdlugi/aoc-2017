from collections import defaultdict

puzzle = 265149

# Part A
width = 0
for i in range(puzzle//2):
    if i * i >= puzzle:
        width = i - 1 if (i - 1) % 2 == 1 else i - 2
        break

pos = (width // 2 + 1, width // 2)
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
curr = width * width + 1
for d in range(4):
    max_dist = width + 1 if d != 0 else width
    dist = min(puzzle - curr, max_dist)
    pos = (pos[0] + dx[d] * dist, pos[1] + dy[d] * dist)
    curr += max_dist
    if curr > puzzle:
        break
print(abs(pos[0]) + abs(pos[1]))

# Part B
values = defaultdict(int)
pos = (0, 0)
values[pos] = 1
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
for width in range(1, puzzle//2, 2):
    for d in range(4):
        for i in range(width + 1):
            pos = (pos[0] + 1, pos[1]) if d == 0 and i == 0 else (pos[0] + dx[d], pos[1] + dy[d])
            neighbors = [-1, 0, 1]
            values[pos] = sum(values[(pos[0] + x, pos[1] + y)] for x in neighbors for y in neighbors)
            if values[pos] > puzzle:
                print(values[pos])
                break
        else:
            continue
        break
    else:
        continue
    break
