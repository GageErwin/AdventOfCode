def solve():
    """
    Solves both parts of the Advent of Code problem in a single pass.
    """
    with open("input.txt") as f:
        data = f.read().strip().split("\n")

    # Variables for Part 1
    index1 = 50
    count1 = 0

    # Variables for Part 2
    index2 = 50
    count2 = 0

    for step in data:
        direction = step[0]
        times = int(step[1:])

        # --- Part 1 logic ---
        if direction == "L":
            index1 = (index1 - times) % 100
        else:  # direction == "R"
            index1 = (index1 + times) % 100

        if index1 == 0:
            count1 += 1

        # --- Part 2 logic ---
        # Count full circles
        count2 += times // 100
        remaining = times % 100

        # Check if the remaining movement crosses the zero point
        if direction == "L":
            if index2 != 0 and remaining >= index2:
                count2 += 1
            index2 = (index2 - times) % 100
        else:  # direction == "R"
            if index2 + remaining >= 100:
                count2 += 1
            index2 = (index2 + times) % 100

    print(f"Part 1: {count1}")
    print(f"Part 2: {count2}")


if __name__ == "__main__":
    solve()
