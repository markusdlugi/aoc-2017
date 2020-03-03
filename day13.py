layers = {}
for line in open("input/13.txt"):
    depth, range_ = map(int, line.strip().split(": "))
    layers[depth] = range_

# Part A
severity = 0
for depth, range_ in layers.items():
    if depth % (2 * (range_ - 1)) == 0:
        severity += depth * range_
print(severity)

# Part B
delay = 0
while True:
    for depth, range_ in layers.items():
        if (depth + delay) % (2 * (range_ - 1)) == 0:
            delay += 1
            break
    else:
        break
print(delay)
