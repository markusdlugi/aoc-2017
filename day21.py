def split(grid, size):
    for row_off in range(0, len(grid), size):
        for col_off in range(0, len(grid), size):
            new_grid = []
            for row in range(size):
                new_row = []
                for col in range(size):
                    new_row.append(grid[row_off + row][col_off + col])
                new_grid.append(new_row)
            yield (new_grid)


def mirror(grid):
    return [row[::-1] for row in grid]


def rotate(grid):
    return [[grid[r][c] for r in range(len(grid))] for c in range(len(grid) - 1, -1, -1)]


def transform(grid):
    for i in range(4):
        grid = rotate(grid)
        yield grid
        yield mirror(grid)


def enhance_section(grid, rules):
    grid_tuple = tuple([tuple(row) for row in grid])
    if grid_tuple in rules:
        return rules[grid_tuple]
    assert False


def enhance(grid, iterations):
    for iteration in range(iterations):
        size = 2 if len(grid) % 2 == 0 else 3
        sections = split(grid, size)
        new_grid = []
        for count, section in enumerate(sections):
            new_section = enhance_section(section, rules)
            new_size = len(new_section)
            r = count // (len(grid) // size)
            for i, row in enumerate(new_section):
                while len(new_grid) <= new_size * r + i:
                    new_grid.append([])
                new_grid[new_size * r + i].extend(row)
        grid = new_grid
    return grid


rules = {}

for line in open("input/21.txt"):
    in_rows, out_rows = line.strip().split(" => ")
    in_split = [list(row) for row in in_rows.split("/")]
    out_split = [list(row) for row in out_rows.split("/")]
    for transformation in transform(in_split):
        grid_tuple = tuple([tuple(row) for row in transformation])
        rules[grid_tuple] = out_split

grid = [list('.#.'), list('..#'), list('###')]

# Part A
part_a = enhance(grid, 5)
print(sum([i == '#' for r in part_a for c in r for i in c]))

# Part B
part_b = enhance(grid, 18)
print(sum([i == '#' for r in part_b for c in r for i in c]))
