with open("input.txt", "r") as file:
  content = file.read().split("\n")


part1_sum = 0
for num in content:
    if not num: continue
    prefix = num[:-1]
    d1 = max(prefix)
    d2 = max(num[prefix.index(d1) + 1:])
    part1_sum += int(d1 + d2)

print(f"Part 1: {part1_sum}")


values_part2 = []
for num_str in content:
    if not num_str: continue
    digits = [int(d) for d in num_str]
    k = 12
    drop = len(digits) - k
    stack = []
    for digit in digits:
        while drop > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop -= 1
        stack.append(digit)
    
    result_digits = stack[:k]
    result_val = int("".join(map(str, result_digits)))
    values_part2.append(result_val)
print(f"Part 2: {sum(values_part2)}")
