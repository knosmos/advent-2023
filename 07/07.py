cards = [[i.split()[0], int(i.split()[1])] for i in open("07.txt","r").read().split("\n")]

def rank(j):
    i = j[0]
    # T1122334455
    # five of kind
    c = len(set(list(i)))
    if c == 1:
        t = 6
    elif c == 2:
        # four of kind
        if i.count(i[0]) == 1 or i.count(i[0]) == 4:
            t = 5
        # full house
        else:
            t = 4
    elif c == 3:
        # three of kind
        for k in range(5):
            if i.count(i[k]) == 3:
                t = 3
                break
        # two pair
        else:
            t = 2
    # one pair
    elif c == 4:
        t = 1
    # high card
    else:
        t = 0
    t *= 100
    for k in range(5):
        t += "AKQJT98765432"[::-1].index(i[k])
        t *= 100
    print(t)
    return t

cards.sort(key = rank)
r = 0
print(cards)
for i in range(len(cards)):
    r += (i+1) * cards[i][1]
print(r)