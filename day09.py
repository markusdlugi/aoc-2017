stream = open("input/09.txt").read()
score = 1
curr = group_score = garbage_count = 0
garbage = -1
while curr < len(stream):
    if garbage >= 0:
        if stream[curr] == '>':
            garbage_count += curr - garbage - 1
            garbage = -1
        elif stream[curr] == '!':
            stream = stream[:curr] + stream[curr + 2:]
            curr -= 1
    else:
        if stream[curr] == '{':
            score += 1
        elif stream[curr] == '}':
            score -= 1
            group_score += score
        elif stream[curr] == '<':
            garbage = curr

    curr += 1

print(group_score)
print(garbage_count)
