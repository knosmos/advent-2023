# advent-2023
Yet another Advent of Code 2023 repository

## Solution Sketches
### Day 1
1. Straightforward implementation.
2. In addition to scanning for numbers, check if substring starting at current index starts with `one`, `two`, `three`, etc.

### Day 2
1. Only challenge is in parsing. Maintain dictionary to track occurrences.
2. Same code, but just take the maximum of the dictionary.

### Day 3
1. Scan through each line to build numbers. Once number is complete, iterate through the positions of its digits to check adjacency; I used a set to find adjacent symbols.
2. Straightforward implementation once we have Part 1.

### Day 4
1. For each card, take set intersection of winning numbers and numbers you have. If set has length `k > 0`, add `2 ^ (k-1)` to total.
2. Use a queue on which new cards are repeatedly added. Run until queue is exhausted.

### Day 5
1. For each seed `s`, for each map find the range that contains `s` and transform accordingly (or keep `s` constant if no range contains it).
2. For each seed range `r = [a, b]`, iterate through each map `m`. For each range in `m` that overlaps with `r`, find the intersection and transform it; add this to the set of ranges for the next map. Then take the parts of `r` that do not overlap with `m`, and add them to the set of ranges for the current map. Repeat for all maps.

### Day 6
1. Straightforward brute force.
2. We have quadratic equation `- i^2 + ti - r > 0` where `i` is the number of seconds to hold, `t` is the total time, and `r` is the record. Number of integers inside the range of the two solutions is the answer.

### Day 7
1. Generate a numerical score of each card by calculating hand type (mainly through finding number of unique items) and appending value of each card in order, then sort based on those scores.
2. Modify score calculation algorithm by running through all possible values of wildcard to find maximum hand type.

### Day 8
1. Simulate steps from `AAA`, terminate when `ZZZ` is reached.
2. Simulate each starting node independently (counting the number of steps taken to reach a destination node), then take the least common multiple of each node's period. The input is nicely constructed in such a way that this works (I'm pretty sure it would fail on a more general test case).

### Day 9
1. Calculate the differences as described in the problem statement. Then sum up the last item of each difference list.
2. Same thing, but in reverse.

### Day 10
1. Run BFS starting from `S`. The current character in each BFS step decides the possible directions for the next step.
2. After finding the loop, run a raycast-esque algorithm to find the number of times a ray pointing downwards hits a horizontal piece of the loop. There's an edge case where the ray hits the loop exactly on a vertical line of the loop: if the line ends up crossing the path of the ray (i.e. it goes from `F` to `J` or `7` to `L`, so the ray crosses a horizontal line of the loop), then we count it as a hit; otherwise we ignore it.

### Day 11
1. Find all the empty columns and rows. Then loop through the grid to find the actual position of each galaxy; to do this, we maintain two offset counters for the rows and columns, incrementing them each time we encounter an empty row or column. We then loop over all pairs of galaxies and sum the Manhattan distance between them.
2. Our solution for Part 1 makes this trivial: just increase the offset counters by 999999 each time.

### Day 12
1. Currently a brute-force solution.

### Day 13
1. Brute force over all possible lines of symmetry. The tricky part is establishing the bounds given the asymmetric folding; we iterate from `max(0, k - (len(p) - k))` (where `p` is the length of the input in the direction parallel to the line and `k` is the index right before the candidate line) to `k` inclusive.
2. Find the original line of reflection, then brute force over all possible smudges, testing to see if any result in a different line of reflection.

### Day 14
1. Scan through each column individually, storing the index of the last non-moving rock (including round rocks that are pushed against square ones). Calculate the load factor as we iterate.
2. Use the same approach, but also build the resulting string as we go. We don't need to simulate the full number of iterations; the grid settles after some number of cycles. I run 1000 cycles, but we can terminate as soon as the grid is unchanged after a cycle.

### Day 15
1. Straightforward implementation (use `ord` for ascii codes).
2. Straightforward implementation.

### Day 16
1. Maintain a stack of each beam (storing position and x/y velocity). Then run DFS; this makes the process very straightforward as we can just pop the next beam off the stack, calculate the next positions (admittedly a very tedious process), and push the resulting beam(s) onto the stack.
2. Run the above algorithm for all edge cells.

### Day 17
1. Dijkstra's algorithm, with each state storing not only position but the current direction and "streak".
2. Same algorithm, with different "neighbor" definitions. Mainly, we skip forward four cells whenever we change direction.