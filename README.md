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