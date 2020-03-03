part_a = 0
part_b = 0
for line in open("input/04.txt"):
    words = line.strip().split(" ")
    a_set, b_set = set(), set()
    for word in words:
        a_set.add(word)
        b_set.add(str(sorted(word)))
    part_a += 1 if len(a_set) == len(words) else 0
    part_b += 1 if len(b_set) == len(words) else 0
print(part_a)
print(part_b)
