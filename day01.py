line = list(map(int, open("input/01.txt").read()))
fwd = len(line)//2

a = sum(d for i, d in enumerate(line) if d == line[(i + 1) % len(line)])
b = sum(d for i, d in enumerate(line) if d == line[(i + fwd) % len(line)])

print(a)
print(b)
