from timeit import default_timer as timer


def generate(num, mod, check_divisor):
    value, factor, divisor = num
    while True:
        value = (value * factor) % mod
        if not check_divisor or value % divisor == 0:
            yield value & 0xFFFF


# start, factor, divisor
a = (512, 16807, 4)
b = (191, 48271, 8)
mod = 2147483647

start = timer()
count = 0
a_gen, b_gen = generate(a, mod, False), generate(b, mod, False)
print(sum(next(a_gen) == next(b_gen) for i in range(40_000_000)))
end = timer()
#print(f'Took {end - start} s.')

start = timer()
a_gen, b_gen = generate(a, mod, True), generate(b, mod, True)
print(sum(next(a_gen) == next(b_gen) for i in range(5_000_000)))
end = timer()
#print(f'Took {end - start} s.')