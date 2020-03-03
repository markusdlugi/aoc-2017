def dance(p, moves, repetitions):
    seen = ["".join(p)]
    for i in range(repetitions):
        for move in moves:
            instruction, params = (move[0], move[1:])
            if instruction == 's':
                num = int(params)
                p = p[-num:] + p[:-num]
            elif instruction == 'x':
                a, b = map(int, params.split('/'))
                p[a], p[b] = (p[b], p[a])
            elif instruction == 'p':
                a, b = params.split('/')
                ai = p.index(a)
                bi = p.index(b)
                p[ai], p[bi] = (b, a)
            else:
                assert False
        result = "".join(p)
        if result in seen:
            return seen[(repetitions % (i + 1))]
        seen.append(result)
    return result


moves = open("input/16.txt").read().strip().split(",")
print(dance(list('abcdefghijklmnop'), moves, 1))
print(dance(list('abcdefghijklmnop'), moves, 1_000_000_000))
