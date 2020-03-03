blocks = list(map(int, open("input/06.txt").read().split("\t")))
tup = tuple(blocks)
seen = {tup: 0}

cycles = 0
while True:
    cycles += 1
    count = max(blocks)
    bank = blocks.index(count)
    blocks[bank] = 0
    bank = (bank + 1) % len(blocks)
    for i in range(0, count):
        blocks[bank] += 1
        bank = (bank + 1) % len(blocks)
    tup = tuple(blocks)
    if tup in seen:
        break
    seen[tup] = cycles

print(cycles)
print(cycles - seen[tup])
