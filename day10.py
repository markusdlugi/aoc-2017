from functools import reduce
from operator import xor


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


# Part A
lengths = list(map(int, open("input/10.txt").read().split(",")))
seq = knot(lengths, 1)
print(seq[0] * seq[1])

# Part B
lengths = list(map(ord, open("input/10.txt").read()))
lengths += [17, 31, 73, 47, 23]
seq = knot(lengths, 64)

knot_hash = ""
for i in range(16):
    block = seq[i * 16:(i+1) * 16]
    result = reduce(xor, block)
    knot_hash += f'{result:02x}'
print(knot_hash)
