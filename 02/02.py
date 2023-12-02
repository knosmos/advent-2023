games = open("02.txt","r").read().split("\n")
r = 0
for game in games:
    name, evs = game.split(": ")
    gid = name.split(" ")[1]
    evs = evs.split("; ")
    for ev in evs:
        a = ev.split(", ")
        b = {"red":0,"green":0,"blue":0}
        for i in a:
            b[i.split(" ")[1]] += int(i.split(" ")[0])
        if b["red"] > 12 or b["green"] > 13 or b["blue"] > 14:
            break
    else:
        r += int(gid)
print(r)