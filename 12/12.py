def permute(s, i=0):
    # find all possible replacements of ?
    if i == len(s):
        return [s]
    if s[i] == "?":
        return permute(s[:i] + "#" + s[i+1:]) + permute(s[:i] + "." + s[i+1:])
    return permute(s, i+1)

def match(s, seq):
    s = [i for i in s.split(".") if i]
    if len(s) != len(seq):
        return False
    for i in range(len(s)):
        if len(s[i]) != seq[i]:
            return False
    return True

r = 0
for i in open("12.txt", "r").read().split("\n"):
    a, seq = i.split()
    seq = list(map(int, seq.split(",")))
    a = permute(a)
    k = 0
    for j in a:
        if match(j, seq):
            k += 1
            print(j)
    print(k)
    r += k
print(r)