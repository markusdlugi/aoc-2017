grid = set()
letters = {}
pos = None
for row, line in enumerate(open("input/19.txt")):
    for col, char in enumerate(line):
        if char in (' ', '\n'):
            continue
        grid.add((row, col))
        if row == 0:
            pos = (row, col)
        if char not in ('|', '-', '+'):
            letters[(row, col)] = char

dr, dc, d = (-1, 0, 1, 0), (0, 1, 0, -1), 2
order = []
steps = 1
while True:
    new_pos = (pos[0] + dr[d], pos[1] + dc[d])
    if new_pos not in grid:
        for i in range(4):
            if i == (d + 2) % 4:
                continue
            new_pos = (pos[0] + dr[i], pos[1] + dc[i])
            if new_pos in grid:
                break
        else:
            break
        d = i
    if new_pos in letters:
        order.append(letters[new_pos])
    pos = new_pos
    steps += 1

print("".join(order))
print(steps)
