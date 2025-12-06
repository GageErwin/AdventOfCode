with open("input.txt", "r") as file:
    data = file.read().split("\n\n")
    fresh_ranges = data[0].split("\n")
    ingredients = data[1].split("\n")


print(ingredients)

fresh = []
for fresh_range in fresh_ranges:
    start, end = fresh_range.split("-")


count = 0
for ingredient in ingredients:
    ingredient = int(ingredient)
    if ingredient in fresh:
        count += 1

print(f"Part 1: {count}")
