from functools import reduce
from operator import xor
from collections import deque


def knot(lengths, repetitions):
    skip = pos = 0
    seq = list(range(0, 256))
    for rep in range(repetitions):
        for length in lengths:
            end = pos + length
            if end <= len(seq):
                part = seq[pos:end][::-1]
                seq = seq[:pos] + part + seq[end:]
            else:
                end = end % len(seq)
                part = seq[0:end][::-1] + seq[pos:][::-1]
                seq = part[-end:] + seq[end:pos] + part[0:-end]
            pos += length + skip
            pos = pos % len(seq)
            skip += 1
    return seq


def knot_hash(text):
    lengths = list(map(ord, text))
    lengths += [17, 31, 73, 47, 23]
    seq = knot(lengths, 64)

    result = ""
    for i in range(16):
        block = seq[i * 16:(i + 1) * 16]
        reduced_block = reduce(xor, block)
        result += f'{reduced_block:02x}'
    return result


def moves(pos):
    dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
    result = []
    for i in range(4):
        neighbor = (pos[0] + dr[i], pos[1] + dc[i])
        if neighbor in grid:
            result.append(neighbor)
    return result


puzzle_input = 'ljoxqyyw'
grid = set()
for row in range(128):
    hash_text = puzzle_input + '-' + str(row)
    hash_val = knot_hash(hash_text)
    binary_val = bin(int(hash_val, 16))[2:].zfill(128)
    for col, val in enumerate(binary_val):
        if val == '1':
            grid.add((row, col))

print(len(grid))

region_count = 0
region_dict = {}
for used in grid:
    queue, visited = deque(), set()
    queue.append(used)
    region = None
    while queue:
        curr = queue.popleft()
        if curr in region_dict:
            region = region_dict[curr]
            break
        for m in moves(curr):
            if m not in visited:
                queue.append(m)
                visited.add(m)
    if region is None:
        region = region_count
        region_count += 1
        for neighbor in visited:
            region_dict[neighbor] = region
    region_dict[used] = region

print(region_count)
