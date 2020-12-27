from timeit import default_timer as timer
from collections import defaultdict

tape = defaultdict(int)
states = {'a': ((1, 1, 'b'), (0, -1, 'e')), 'b': ((1, -1, 'c'), (0, 1, 'a')),
          'c': ((1, -1, 'd'), (0, 1, 'c')), 'd': ((1, -1, 'e'), (0, -1, 'f')),
          'e': ((1, -1, 'a'), (1, -1, 'c')), 'f': ((1, -1, 'e'), (1, 1, 'a'))}

start = timer()

pos = 0
state = 'a'
for i in range(12_386_363):
    actions_0, actions_1 = states[state]
    write, direction, next_state = actions_0 if tape[pos] == 0 else actions_1
    tape[pos] = write
    pos += direction
    state = next_state

print(sum(x for x in tape.values()))

end = timer()
#print(f'Took {end - start} seconds.')
