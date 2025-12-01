data = open("./input.txt", "r").read().split("\n")


safe = list(x for x in range(0, 100))

# Part 1
index = 50
count = 0
for step in data:
    if step.startswith("L"):
        times = step.replace("L", "")
        index = index - int(times)
        index = index % 100
    elif step.startswith("R"):
        times = step.replace("R", "")
        index = index + int(times)
        index = index % 100
    index = safe[index]
    if index == 0:
        count += 1

print(f"Part 1: {count}")

# Part 2
index = 50
count = 0
for step in data:
    if step.startswith("L"):
        times = int(step.replace("L", ""))
        count += times // 100
        remaining = times % 100
        if remaining >= index and index != 0:
            count += 1
        index = (index - times) % 100

    elif step.startswith("R"):
        times = int(step.replace("R", ""))
        count += times // 100
        remaining = times % 100
        if index + remaining >= 100:
            count += 1
        index = (index + times) % 100
    index = safe[index]

print(f"Part 2: {count}")
