from copy import deepcopy

particles = []
for line in open("input/20.txt"):
    components = line.strip().split(", ")
    particles.append([list(map(int, c[3:-1].split(","))) for c in components])

# Part A
particles_copy = deepcopy(particles)
min_particle = None
for i in range(500):
    min_dist = None
    for num, particle in enumerate(particles):
        dist = 0
        for x in range(3):
            particle[1][x] += particle[2][x]
            particle[0][x] += particle[1][x]
            dist += abs(particle[0][x])
        if min_dist is None or dist < min_dist:
            min_dist = dist
            min_particle = num
print(min_particle)

# Part B
particles = particles_copy
for i in range(500):
    positions = {}
    collided = []
    for num, particle in enumerate(particles):
        for x in range(3):
            particle[1][x] += particle[2][x]
            particle[0][x] += particle[1][x]
        pos = tuple(particle[0])
        if pos in positions:
            collided.append(particle)
            if positions[pos] not in collided:
                collided.append(positions[pos])
        else:
            positions[pos] = particle
    for particle in collided:
        particles.remove(particle)
print(len(particles))
