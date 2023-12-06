def r(t, rec):
    ways = 0
    for i in range(t+1):
        if (t - i) * i > rec:
            ways += 1
    return ways

print(r(48,296) * r(93,1928) * r(85,1236) * r(95,1391))