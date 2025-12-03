with open("input.txt", "r") as file:
  content = file.read().split(",")


# Part 1
values = []
for line in content:
  start, end = line.split("-")
  num_range = list(range(int(start), int(end) + 1))
  for num in num_range:
    num_len = len(str(num))
    num = str(num)
    first_half = num[:(num_len//2)]
    last_half = num[(num_len//2):]
    if first_half == last_half:
      values.append(int(num))
print("total pairs found: ", sum(values))



# Part 2
values = []
for line in content:
  start, end = line.split("-")
  num_range = list(range(int(start), int(end) + 1))
  for num in num_range:
    num_len = len(str(num))
    num = str(num)
    slice = num[:(num_len//2)]
    while len(slice) > 0:
      # if num.count(slice) % num_len == 0:
      if num_len % len(slice) == 0 and num.count(slice) == num_len // len(slice):
        print("found: ", slice, " in ", num)
        # Remove last digit
        slice = slice[:-1]
        values.append(int(num))
        break
      else:
        slice = slice[:-1]
      
print("Part 2: ", sum(values))