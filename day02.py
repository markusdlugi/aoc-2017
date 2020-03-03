from itertools import combinations

part_a = 0
part_b = 0
for line in open("input/02.txt"):
    numbers = list(map(int, line.split("\t")))
    part_a += max(numbers) - min(numbers)
    for (a, b) in combinations(numbers, 2):
        a, b = max(a, b), min(a, b)
        if a % b == 0:
            part_b += a // b
            break
print(part_a)
print(part_b)
