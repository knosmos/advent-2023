def solve(row):
    curr_offset = 0
    r = 0
    for i in range(len(row)):
        if row[i] == "#":
            curr_offset = i + 1
        elif row[i] == "O":
            r += len(row) - curr_offset
            curr_offset += 1
    return r

p = open("14.txt","r").read().split("\n")
# transpose
p = list(map(list, zip(*p)))

r = 0
for row in p:
    r += solve(row)
print(r)