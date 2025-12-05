from collections import deque

with open("input.txt", "r") as file:
    data = [list(line) for line in file.read().split("\n") if line]

rows = len(data)
cols = len(data[0])


def count_neighbors(r, c, grid):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == "@":
                    count += 1
    return count


queue = deque()
part1_count = 0

# Initial scan
for r in range(rows):
    for c in range(cols):
        if data[r][c] == "@":
            if count_neighbors(r, c, data) < 4:
                queue.append((r, c))

# Part 1 is just the set of papers removable in the first pass
part1_count = len(queue)
print(f"Part 1: {part1_count}")

# Part 2: Process the queue
total_removed = 0

# We need to keep track of what's effectively removed to avoid double counting
# if we added duplicates (though logic shouldn't add duplicates if we check state).
# But since the 'state' changes to '.', we can just check that.
# However, for the 'neighbor count check' to be fast, we just re-check the count.
# A small optimization: we don't need to re-scan neighbors of X, we scan neighbors OF neighbors.
# Wait, no. When we remove X, we check X's neighbors. If neighbor Y now has <4 neighbors, Y is queued.

while queue:
    r, c = queue.popleft()

    # If already removed (handled), skip
    if data[r][c] != "@":
        continue

    # Remove it
    data[r][c] = "."
    total_removed += 1

    # Check its neighbors
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if data[nr][nc] == "@":
                    # Re-evaluate this neighbor
                    # This localized check is O(1) (8 checks)
                    if count_neighbors(nr, nc, data) < 4:
                        queue.append((nr, nc))

print(f"Part 2: {total_removed}")
