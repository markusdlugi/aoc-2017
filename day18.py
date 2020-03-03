from collections import defaultdict
from collections import deque


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def run_program(instructions, registers, queue, state):
    id, sp, send_count = state
    while sp < len(instructions):
        cmd, args = instructions[sp]
        if cmd == "snd":
            x = args[0]
            queue[(id + 1) % 2].append(x if is_int(x) else registers[x])
            send_count += 1
        elif cmd == "set":
            x, y = args
            registers[x] = y if is_int(y) else registers[y]
        elif cmd == "add":
            x, y = args
            registers[x] += y if is_int(y) else registers[y]
        elif cmd == "mul":
            x, y = args
            registers[x] *= y if is_int(y) else registers[y]
        elif cmd == "mod":
            x, y = args
            val = registers[x]
            registers[x] = val % y if is_int(y) else val % registers[y]
        elif cmd == "rcv":
            x = args[0]
            if not queue[id]:
                return id, sp, send_count
            registers[x] = queue[id].popleft()
        elif cmd == "jgz":
            x, y = args
            value = x if is_int(x) else registers[x]
            value2 = y if is_int(y) else registers[y]
            if value > 0:
                sp += value2
                continue
        else:
            assert False

        sp += 1
    return id, sp, send_count


instructions = []
for line in open("input/18.txt"):
    instruction = line.strip().split(" ")
    args = instruction[1:]
    for i, arg in enumerate(args):
        args[i] = int(arg) if is_int(arg) else arg

    instructions.append((instruction[0], args))

# Part A
queue = {0: deque(), 1: deque()}
run_program(instructions, defaultdict(int), queue, (0, 0, 0))
print(queue[1].pop())

# Part B
queue = {0: deque(), 1: deque()}
registers = (defaultdict(int), defaultdict(int))
registers[1]['p'] = 1
state = [(0, 0, 0), (1, 0, 0)]
while True:
    old_sent = (state[0][2], state[1][2])
    state[0] = run_program(instructions, registers[0], queue, state[0])
    state[1] = run_program(instructions, registers[1], queue, state[1])
    if state[0][2] == old_sent[0] and state[1][2] == old_sent[1]:
        break
print(state[1][2])
