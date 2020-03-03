import re
from collections import defaultdict

registers = defaultdict(int)
highest = 0
for line in open("input/08.txt"):
    register, inc_dec, count, cond_reg, cond = re.findall(r'(\w*) (inc|dec) ([-]?\d*) if (\w*) (.*)', line.strip())[0]
    count = int(count) if inc_dec == 'inc' else int(count) * -1
    if eval("registers[cond_reg]" + cond):
        registers[register] += count
        highest = max(highest, registers[register])

print(max(registers.values()))
print(highest)
