step = 314

buffer = [0]
pos = 0
for i in range(1, 2018):
    pos = (pos + step + 1) % len(buffer)
    buffer.insert(pos, i)
print(buffer[buffer.index(2017) + 1])

pos = 0
start = 0
for i in range(1, 50_000_000):
    pos = (pos + step + 1) % i
    if pos == 0:
        start = i
print(start)
