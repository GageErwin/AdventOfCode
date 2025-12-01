with open("input.txt") as f:
    data = f.read().strip().split("\n")

safe = list(range(100))

# Part 1
index = 50
count = 0
for step in data:
    direction = step[0]
    times = int(step[1:])

    if direction == "L":
        index = (index - times) % 100
    else:  # direction == "R"
        index = (index + times) % 100

    index = safe[index]
    if index == 0:
        count += 1

print(f"Part 1: {count}")

# Part 2
index = 50
count = 0
for step in data:
    direction = step[0]
    times = int(step[1:])

    count += times // 100
    remaining = times % 100

    if direction == "L":
        if remaining >= index and index != 0:
            count += 1
        index = (index - times) % 100
    else:  # direction == "R"
        if index + remaining >= 100:
            count += 1
        index = (index + times) % 100

    index = safe[index]

print(f"Part 2: {count}")
