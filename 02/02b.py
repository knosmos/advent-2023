games = open("02.txt","r").read().split("\n")
r = 0
for game in games:
    name, evs = game.split(": ")
    evs = evs.split("; ")
    bmax = {"red":0,"green":0,"blue":0}
    for ev in evs:
        a = ev.split(", ")
        b = {"red":0,"green":0,"blue":0}
        for i in a:
            b[i.split(" ")[1]] += int(i.split(" ")[0])
        for i in b:
            if b[i] > bmax[i]:
                bmax[i] = b[i]
    r += bmax["red"]*bmax["green"]*bmax["blue"]
print(r)