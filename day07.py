import re
from collections import Counter


def find_wrong_weight(program):
    sub_weights = {}
    if program in programs:
        sub_weights = {}
        for p in programs[program]:
            sub_weight = find_wrong_weight(p)
            if sub_weight is None:
                return None
            sub_weights[p] = sub_weight
        weight_count = Counter(sub_weights.values()).most_common()
        if len(weight_count) != 1:
            right_weight, wrong_weight = weight_count[0][0], weight_count[-1][0]
            diff = right_weight - wrong_weight
            for k, v in sub_weights.items():
                if v == wrong_weight:
                    print(weights[k] + diff)
            return None
    return weights[program] + sum(sub_weights.values())


programs = {}
weights = {}
for line in open("input/07.txt"):
    program, weight, _, tower = re.findall(r'(\w*) \((\d*)\)( -> (.*))?', line.strip())[0]
    if tower != '':
        programs[program] = tower.split(", ")
    weights[program] = int(weight)

leafs = set()
root = None
for k, v in programs.items():
    leafs.update(v)
for program in programs:
    if program not in leafs:
        root = program
        break

print(root)
find_wrong_weight(root)
