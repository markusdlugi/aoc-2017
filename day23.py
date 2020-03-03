from collections import defaultdict


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def run_program(instructions, registers, stop_at_8):
    sp = 0
    mul_count = 0
    while sp < len(instructions):
        cmd, args = instructions[sp]
        if sp == 8 and stop_at_8:
            return
        if cmd == "set":
            x, y = args
            registers[x] = y if is_int(y) else registers[y]
        elif cmd == "sub":
            x, y = args
            registers[x] -= y if is_int(y) else registers[y]
        elif cmd == "mul":
            x, y = args
            registers[x] *= y if is_int(y) else registers[y]
            mul_count += 1
        elif cmd == "jnz":
            x, y = args
            value = x if is_int(x) else registers[x]
            value2 = y if is_int(y) else registers[y]
            if value != 0:
                sp += value2
                continue
        else:
            assert False

        sp += 1
    return mul_count


instructions = []
for line in open("input/23.txt"):
    instruction = line.strip().split(" ")
    args = instruction[1:]
    for i, arg in enumerate(args):
        args[i] = int(arg) if is_int(arg) else arg

    instructions.append((instruction[0], args))

# Part A
mul_count = run_program(instructions, defaultdict(int), False)
print(mul_count)

# Part B
registers = defaultdict(int)
registers['a'] = 1
run_program(instructions, registers, True)

h = 0
# Count non-prime numbers between b and c with step size 17
for num in range(registers['b'], registers['c'] + 1, 17):
    for i in range(2, num // 2):
        if (num % i) == 0:
            h += 1
            break
print(h)
