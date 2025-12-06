with open("example.txt", "r") as file:
    data = file.read().split("\n\n")
    fresh_ranges = data[0].split("\n")
    ingredients = data[1].split("\n")

fresh = []
for fresh_range in fresh_ranges:
    start, end = fresh_range.split("-")
    fresh.append((int(start), int(end)))


count = 0
for ingredient in ingredients:
    ingredient = int(ingredient)
    for fresh_range in fresh:
        if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
            count += 1
            break

print(f"Part 1: {count}")

# Optimized Part 2
fresh.sort()
merged = []
if fresh:
    curr_start, curr_end = fresh[0]
    for start, end in fresh[1:]:
        if start <= curr_end + 1: # Overlapping or adjacent
            curr_end = max(curr_end, end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = start, end
    merged.append((curr_start, curr_end))

part2_count = sum(end - start + 1 for start, end in merged)
print(f"Part 2: {part2_count}")