def get_steps(offsets, decrease):
    i = steps = 0
    while 0 <= i < len(offsets):
        jump = offsets[i]
        offsets[i] += 1 if jump < 3 or not decrease else -1
        i += jump
        steps += 1
    return steps


offsets = list(map(int, open("input/05.txt")))
print(get_steps(offsets.copy(), False))
print(get_steps(offsets.copy(), True))
